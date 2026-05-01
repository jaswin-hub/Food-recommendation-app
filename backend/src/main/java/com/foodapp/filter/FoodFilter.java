package com.foodapp.filter;

import com.foodapp.dto.ScoredRecipe;
import java.util.List;

/**
 * ABSTRACTION & INHERITANCE: 
 * This is an abstract base class. It defines the structure for all filters.
 * Subclasses will inherit from this and provide specific implementations.
 */
public abstract class FoodFilter {
    protected String filterName;

    public FoodFilter(String filterName) {
        this.filterName = filterName;
    }

    /**
     * Abstract method that must be implemented by subclasses.
     * This defines the contract.
     */
    public abstract List<ScoredRecipe> applyFilter(List<ScoredRecipe> recipes);

    public String getFilterName() {
        return filterName;
    }
}
