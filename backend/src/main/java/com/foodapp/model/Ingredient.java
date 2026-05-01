package com.foodapp.model;

/**
 * ENCAPSULATION: We hide the internal state by making fields private.
 * Access to these fields is provided via public getters and setters.
 */
public class Ingredient {
    private String name;
    private String quantity;
    private boolean isAllergen;

    public Ingredient() {}

    public Ingredient(String name, String quantity, boolean isAllergen) {
        this.name = name;
        this.quantity = quantity;
        this.isAllergen = isAllergen;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getQuantity() {
        return quantity;
    }

    public void setQuantity(String quantity) {
        this.quantity = quantity;
    }

    public boolean isAllergen() {
        return isAllergen;
    }

    public void setAllergen(boolean allergen) {
        isAllergen = allergen;
    }
}
