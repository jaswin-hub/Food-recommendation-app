package com.foodapp.filter;

import com.foodapp.dto.ScoredRecipe;
import java.util.List;

/**
 * INHERITANCE: TasteFilter inherits from FoodFilter.
 * POLYMORPHISM: It overrides applyFilter.
 */
public class TasteFilter extends FoodFilter {
    
    private List<String> targetTastes;

    public TasteFilter(List<String> targetTastes) {
        super("Taste Filter");
        this.targetTastes = targetTastes;
    }

    @Override
    public List<ScoredRecipe> applyFilter(List<ScoredRecipe> recipes) {
        if (targetTastes == null || targetTastes.isEmpty()) {
            return recipes;
        }

        for (ScoredRecipe recipe : recipes) {
            // Give +20 points if taste is in the target list
            if (recipe.getTaste() != null) {
                for (String targetTaste : targetTastes) {
                    if (recipe.getTaste().equalsIgnoreCase(targetTaste)) {
                        recipe.setScore(recipe.getScore() + 20);
                        break;
                    }
                }
            }
        }
        return recipes;
    }
}
