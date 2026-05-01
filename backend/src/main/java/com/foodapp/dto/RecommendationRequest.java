package com.foodapp.dto;

import java.util.List;

public class RecommendationRequest {
    private String diet;
    private List<String> cuisine; // Changed to List to support multi-select chips as per spec
    private List<String> taste;   // Changed to List to support multi-select chips as per spec
    private List<String> ingredients;
    private List<String> allergies;
    private Integer maxCookTimeMinutes;
    private Integer maxCalories;
    private Double maxBudget;
    private String goal;
    private String mealType;

    public RecommendationRequest() {}

    public String getDiet() { return diet; }
    public void setDiet(String diet) { this.diet = diet; }

    public List<String> getCuisine() { return cuisine; }
    public void setCuisine(List<String> cuisine) { this.cuisine = cuisine; }

    public List<String> getTaste() { return taste; }
    public void setTaste(List<String> taste) { this.taste = taste; }

    public List<String> getIngredients() { return ingredients; }
    public void setIngredients(List<String> ingredients) { this.ingredients = ingredients; }

    public List<String> getAllergies() { return allergies; }
    public void setAllergies(List<String> allergies) { this.allergies = allergies; }

    public Integer getMaxCookTimeMinutes() { return maxCookTimeMinutes; }
    public void setMaxCookTimeMinutes(Integer maxCookTimeMinutes) { this.maxCookTimeMinutes = maxCookTimeMinutes; }

    public Integer getMaxCalories() { return maxCalories; }
    public void setMaxCalories(Integer maxCalories) { this.maxCalories = maxCalories; }

    public Double getMaxBudget() { return maxBudget; }
    public void setMaxBudget(Double maxBudget) { this.maxBudget = maxBudget; }

    public String getGoal() { return goal; }
    public void setGoal(String goal) { this.goal = goal; }

    public String getMealType() { return mealType; }
    public void setMealType(String mealType) { this.mealType = mealType; }
}
