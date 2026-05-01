package com.foodapp.model;

import java.util.List;

/**
 * ENCAPSULATION: All fields are private, with public getters and setters.
 */
public class Recipe {
    private String id;
    private String name;
    private String cuisine;
    private String diet;
    private String taste;
    
    /**
     * COMPOSITION: A Recipe HAS-A list of Ingredients. 
     * We don't just use strings; we compose complex objects.
     */
    private List<Ingredient> ingredients;
    
    private int calories;
    private int cookTimeMinutes;
    private List<String> steps;
    private double budget;
    private String mealType;
    private String imageUrl;

    public Recipe() {}

    public Recipe(String id, String name, String cuisine, String diet, String taste, List<Ingredient> ingredients, int calories, int cookTimeMinutes, List<String> steps, double budget, String imageUrl, String mealType) {
        this.id = id;
        this.name = name;
        this.cuisine = cuisine;
        this.diet = diet;
        this.taste = taste;
        this.ingredients = ingredients;
        this.calories = calories;
        this.cookTimeMinutes = cookTimeMinutes;
        this.steps = steps;
        this.budget = budget;
        this.imageUrl = imageUrl;
        this.mealType = mealType;
    }

    public String getId() { return id; }
    public void setId(String id) { this.id = id; }

    public String getName() { return name; }
    public void setName(String name) { this.name = name; }

    public String getCuisine() { return cuisine; }
    public void setCuisine(String cuisine) { this.cuisine = cuisine; }

    public String getDiet() { return diet; }
    public void setDiet(String diet) { this.diet = diet; }

    public String getTaste() { return taste; }
    public void setTaste(String taste) { this.taste = taste; }

    public List<Ingredient> getIngredients() { return ingredients; }
    public void setIngredients(List<Ingredient> ingredients) { this.ingredients = ingredients; }

    public int getCalories() { return calories; }
    public void setCalories(int calories) { this.calories = calories; }

    public int getCookTimeMinutes() { return cookTimeMinutes; }
    public void setCookTimeMinutes(int cookTimeMinutes) { this.cookTimeMinutes = cookTimeMinutes; }

    public List<String> getSteps() { return steps; }
    public void setSteps(List<String> steps) { this.steps = steps; }

    public double getBudget() { return budget; }
    public void setBudget(double budget) { this.budget = budget; }

    public String getImageUrl() { return imageUrl; }
    public void setImageUrl(String imageUrl) { this.imageUrl = imageUrl; }

    public String getMealType() { return mealType; }
    public void setMealType(String mealType) { this.mealType = mealType; }
}
