package com.foodapp.filter;

import com.foodapp.dto.ScoredRecipe;
import java.util.List;

public class GoalFilter extends FoodFilter {
    private String goal;

    public GoalFilter(String goal) {
        super("Goal");
        this.goal = goal;
    }

    @Override
    public List<ScoredRecipe> applyFilter(List<ScoredRecipe> recipes) {
        if (goal == null || goal.isEmpty()) {
            return recipes;
        }

        for (ScoredRecipe sr : recipes) {
            String diet = sr.getDiet();
            int score = sr.getScore();

            if (goal.equalsIgnoreCase("Fat Loss")) {
                if (diet.equalsIgnoreCase("Low Calorie") || diet.equalsIgnoreCase("Keto")) {
                    sr.setScore(score + 50);
                }
            } else if (goal.equalsIgnoreCase("Muscle Gain")) {
                if (diet.equalsIgnoreCase("High Protein")) {
                    sr.setScore(score + 50);
                }
            } else if (goal.equalsIgnoreCase("Maintenance")) {
                if (diet.equalsIgnoreCase("Veg") || diet.equalsIgnoreCase("Non-Veg")) {
                    sr.setScore(score + 20);
                }
            }
        }
        return recipes;
    }
}
