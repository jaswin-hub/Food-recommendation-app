package com.foodapp.service;

import com.foodapp.data.RecipeDataStore;
import com.foodapp.dto.RecommendationRequest;
import com.foodapp.dto.ScoredRecipe;
import com.foodapp.filter.*;
import com.foodapp.model.Recipe;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.stream.Collectors;

@Service
public class RecipeRecommendationService implements RecommendationService {

    private final RecipeDataStore dataStore;

    @Autowired
    public RecipeRecommendationService(RecipeDataStore dataStore) {
        this.dataStore = dataStore;
    }

    @Override
    public List<Recipe> getAllRecipes() {
        return dataStore.getAllRecipes();
    }

    @Override
    public Recipe getRecipeById(String id) {
        return dataStore.getAllRecipes().stream()
                .filter(r -> r.getId().equals(id))
                .findFirst()
                .orElse(null);
    }

    @Override
    public List<ScoredRecipe> recommend(RecommendationRequest request) {
        List<ScoredRecipe> scoredRecipes = getScoredAndFilteredRecipes(request, false);

        // Fallback Logic: If fewer than 3 results pass filters, relax filters
        if (scoredRecipes.size() < 3) {
            // Relax taste by setting it to null
            request.setTaste(null);
            scoredRecipes = getScoredAndFilteredRecipes(request, true);
        }
        
        if (scoredRecipes.size() < 3) {
            // Relax cuisine
            request.setCuisine(null);
            scoredRecipes = getScoredAndFilteredRecipes(request, true);
        }

        if (scoredRecipes.size() < 3) {
            // Relax diet
            request.setDiet(null);
            scoredRecipes = getScoredAndFilteredRecipes(request, true);
        }

        // Return top 10 results sorted by score descending
        return scoredRecipes.stream()
                .sorted(Comparator.comparingInt(ScoredRecipe::getScore).reversed())
                .limit(10)
                .collect(Collectors.toList());
    }

    private List<ScoredRecipe> getScoredAndFilteredRecipes(RecommendationRequest request, boolean isFallback) {
        // Initialize all recipes with a score of 0
        List<ScoredRecipe> currentList = new ArrayList<>();
        for (Recipe r : dataStore.getAllRecipes()) {
            currentList.add(new ScoredRecipe(r, 0, isFallback));
        }

        /**
         * POLYMORPHISM IN ACTION: 
         * We hold different filter objects (DietFilter, CuisineFilter, etc.) 
         * in a list of their common parent type (FoodFilter).
         * Calling applyFilter() on them executes their specific overridden method.
         */
        List<FoodFilter> filters = new ArrayList<>();
        filters.add(new DietFilter(request.getDiet()));
        filters.add(new CuisineFilter(request.getCuisine()));
        filters.add(new TasteFilter(request.getTaste()));
        filters.add(new IngredientFilter(request.getIngredients(), request.getAllergies()));
        filters.add(new GoalFilter(request.getGoal()));
        filters.add(new MealTypeFilter(request.getMealType()));

        for (FoodFilter filter : filters) {
            currentList = filter.applyFilter(currentList);
        }

        // Apply Hard Cutoffs and filter out 0 score (unless no filters provided)
        List<ScoredRecipe> finalList = new ArrayList<>();
        
        boolean noFilters = request.getDiet() == null && 
                            (request.getCuisine() == null || request.getCuisine().isEmpty()) && 
                            (request.getTaste() == null || request.getTaste().isEmpty()) && 
                            (request.getIngredients() == null || request.getIngredients().isEmpty());

        for (ScoredRecipe sr : currentList) {
            boolean passesTime = request.getMaxCookTimeMinutes() == null || sr.getCookTimeMinutes() <= request.getMaxCookTimeMinutes();
            boolean passesCalories = request.getMaxCalories() == null || sr.getCalories() <= request.getMaxCalories();
            boolean passesBudget = request.getMaxBudget() == null || sr.getBudget() <= request.getMaxBudget();

            if (passesTime && passesCalories && passesBudget) {
                if (sr.getScore() > 0 || noFilters) {
                    finalList.add(sr);
                }
            }
        }

        return finalList;
    }
}
