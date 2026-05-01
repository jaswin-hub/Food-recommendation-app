package com.foodapp.controller;

import com.foodapp.dto.RecommendationRequest;
import com.foodapp.dto.ScoredRecipe;
import com.foodapp.model.Recipe;
import com.foodapp.service.RecommendationService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api")
public class RecipeController {

    private final RecommendationService recommendationService;

    @Autowired
    public RecipeController(RecommendationService recommendationService) {
        this.recommendationService = recommendationService;
    }

    @PostMapping("/recommend")
    public List<ScoredRecipe> recommend(@RequestBody RecommendationRequest request) {
        return recommendationService.recommend(request);
    }

    @GetMapping("/recipes")
    public List<Recipe> getAllRecipes() {
        return recommendationService.getAllRecipes();
    }

    @GetMapping("/recipes/{id}")
    public Recipe getRecipeById(@PathVariable String id) {
        return recommendationService.getRecipeById(id);
    }
}
