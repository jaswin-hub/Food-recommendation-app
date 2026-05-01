package com.foodapp.filter;

import com.foodapp.dto.ScoredRecipe;
import java.util.List;

/**
 * INHERITANCE: DietFilter inherits from FoodFilter.
 * POLYMORPHISM: It overrides the applyFilter method to provide specific behavior.
 */
public class DietFilter extends FoodFilter {
    
    private String targetDiet;

    public DietFilter(String targetDiet) {
        super("Diet Filter");
        this.targetDiet = targetDiet;
    }

    @Override
    public List<ScoredRecipe> applyFilter(List<ScoredRecipe> recipes) {
        if (targetDiet == null || targetDiet.isEmpty()) {
            return recipes; // No filter applied
        }

        for (ScoredRecipe recipe : recipes) {
            // Give +30 points if diet matches exactly
            if (recipe.getDiet() != null && recipe.getDiet().equalsIgnoreCase(targetDiet)) {
                recipe.setScore(recipe.getScore() + 30);
            }
        }
        return recipes;
    }
}
