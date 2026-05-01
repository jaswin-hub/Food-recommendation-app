package com.foodapp.filter;

import com.foodapp.dto.ScoredRecipe;
import com.foodapp.model.Ingredient;
import java.util.List;

/**
 * INHERITANCE: IngredientFilter inherits from FoodFilter.
 * POLYMORPHISM: Overrides applyFilter for complex ingredient scoring and allergy checks.
 */
public class IngredientFilter extends FoodFilter {
    
    private List<String> userIngredients;
    private List<String> userAllergies;

    public IngredientFilter(List<String> userIngredients, List<String> userAllergies) {
        super("Ingredient & Allergy Filter");
        this.userIngredients = userIngredients;
        this.userAllergies = userAllergies;
    }

    @Override
    public List<ScoredRecipe> applyFilter(List<ScoredRecipe> recipes) {
        for (ScoredRecipe recipe : recipes) {
            
            // 1. Check Allergies First
            boolean hasAllergen = false;
            if (userAllergies != null && !userAllergies.isEmpty()) {
                for (Ingredient recipeIngredient : recipe.getIngredients()) {
                    for (String allergy : userAllergies) {
                        if (recipeIngredient.getName().toLowerCase().contains(allergy.toLowerCase())) {
                            hasAllergen = true;
                            break;
                        }
                    }
                    if (hasAllergen) break;
                }
            }

            if (hasAllergen) {
                recipe.setScore(0); // Disqualify
                continue; // Move to next recipe
            }

            // 2. Score Ingredient Overlap
            if (userIngredients != null && !userIngredients.isEmpty()) {
                int matchCount = 0;
                for (Ingredient recipeIngredient : recipe.getIngredients()) {
                    String recipeIngName = recipeIngredient.getName().toLowerCase();
                    for (String userIngredient : userIngredients) {
                        String userIngName = userIngredient.toLowerCase();
                        if (recipeIngName.contains(userIngName) || userIngName.contains(recipeIngName)) {
                            matchCount++;
                            break; // matched this recipe ingredient
                        }
                    }
                }

                // Calculate match percentage based on recipe's ingredients
                if (!recipe.getIngredients().isEmpty()) {
                    double percentage = ((double) matchCount / recipe.getIngredients().size()) * 100;
                    recipe.setMatchPercentage(Math.round(percentage * 10.0) / 10.0); // Round to 1 decimal
                }

                // Recipes with more matching ingredients get higher scores
                // Each matching ingredient adds 100 points
                if (matchCount > 0) {
                    int bonus = 0;
                    // Easy to make highlight: Bonus if steps are fewer than 5
                    if (recipe.getSteps() != null && recipe.getSteps().size() < 5) {
                        bonus = 50;
                    }
                    recipe.setScore(recipe.getScore() + (matchCount * 100) + bonus);
                }
            }
        }
        return recipes;
    }
}
