package com.foodapp.dto;

import com.foodapp.model.Recipe;

/**
 * INHERITANCE: ScoredRecipe extends the base Recipe class to add scoring properties
 * specifically for recommendations without modifying the core Recipe model.
 */
public class ScoredRecipe extends Recipe {
    private int score;
    private double matchPercentage;
    private boolean fallbackSuggestion;

    public ScoredRecipe(Recipe recipe, int score, boolean fallbackSuggestion) {
        super(recipe.getId(), recipe.getName(), recipe.getCuisine(), recipe.getDiet(), recipe.getTaste(), 
              recipe.getIngredients(), recipe.getCalories(), recipe.getCookTimeMinutes(), 
              recipe.getSteps(), recipe.getBudget(), recipe.getImageUrl(), recipe.getMealType());
        this.score = score;
        this.fallbackSuggestion = fallbackSuggestion;
        this.matchPercentage = 0.0;
    }

    public int getScore() {
        return score;
    }

    public void setScore(int score) {
        this.score = score;
    }

    public boolean isFallbackSuggestion() {
        return fallbackSuggestion;
    }

    public void setFallbackSuggestion(boolean fallbackSuggestion) {
        this.fallbackSuggestion = fallbackSuggestion;
    }

    public double getMatchPercentage() {
        return matchPercentage;
    }

    public void setMatchPercentage(double matchPercentage) {
        this.matchPercentage = matchPercentage;
    }
}
