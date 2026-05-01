package com.foodapp.service;

import com.foodapp.dto.RecommendationRequest;
import com.foodapp.dto.ScoredRecipe;
import com.foodapp.model.Recipe;
import java.util.List;

/**
 * ABSTRACTION: This interface hides the implementation details of how recommendations are made.
 * It provides a clean API for the controller to use.
 */
public interface RecommendationService {
    List<ScoredRecipe> recommend(RecommendationRequest request);
    List<Recipe> getAllRecipes();
    Recipe getRecipeById(String id);
}
