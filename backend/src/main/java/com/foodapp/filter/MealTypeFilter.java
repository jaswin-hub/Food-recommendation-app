package com.foodapp.filter;

import com.foodapp.dto.ScoredRecipe;
import java.util.List;

public class MealTypeFilter extends FoodFilter {
    private String mealType;

    public MealTypeFilter(String mealType) {
        super("MealType");
        this.mealType = mealType;
    }

    @Override
    public List<ScoredRecipe> applyFilter(List<ScoredRecipe> recipes) {
        if (mealType == null || mealType.isEmpty() || mealType.equalsIgnoreCase("All")) {
            return recipes;
        }

        for (ScoredRecipe sr : recipes) {
            if (sr.getMealType() != null && sr.getMealType().equalsIgnoreCase(mealType)) {
                sr.setScore(sr.getScore() + 40);
            }
        }
        return recipes;
    }
}
