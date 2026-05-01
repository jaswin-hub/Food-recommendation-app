package com.foodapp.filter;

import com.foodapp.dto.ScoredRecipe;
import java.util.List;

/**
 * INHERITANCE: CuisineFilter inherits from FoodFilter.
 * POLYMORPHISM: It overrides applyFilter for specific cuisine scoring.
 */
public class CuisineFilter extends FoodFilter {
    
    private List<String> targetCuisines;

    public CuisineFilter(List<String> targetCuisines) {
        super("Cuisine Filter");
        this.targetCuisines = targetCuisines;
    }

    @Override
    public List<ScoredRecipe> applyFilter(List<ScoredRecipe> recipes) {
        if (targetCuisines == null || targetCuisines.isEmpty()) {
            return recipes;
        }

        for (ScoredRecipe recipe : recipes) {
            // Give +20 points if cuisine is in the target list
            if (recipe.getCuisine() != null) {
                for (String targetCuisine : targetCuisines) {
                    if (recipe.getCuisine().equalsIgnoreCase(targetCuisine)) {
                        recipe.setScore(recipe.getScore() + 20);
                        break; // Stop checking once matched
                    }
                }
            }
        }
        return recipes;
    }
}
