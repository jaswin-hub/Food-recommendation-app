import React, { useState } from 'react';
import FilterBadge from './FilterBadge';
import { Search } from 'lucide-react';

const DIETS = ['Veg', 'Non-Veg', 'Vegan', 'Keto', 'High Protein', 'Low Calorie'];
const CUISINES = ['Indian', 'Chinese', 'Italian', 'Korean', 'Mexican', 'Japanese', 'American'];
const TASTES = ['Spicy', 'Sweet', 'Sour', 'Salty', 'Savory', 'Mild'];

const FilterForm = ({ onSubmit, onReset }) => {
    const [diet, setDiet] = useState('');
    const [cuisine, setCuisine] = useState([]);
    const [taste, setTaste] = useState([]);
    
    const [ingredientInput, setIngredientInput] = useState('');
    const [ingredients, setIngredients] = useState([]);
    
    const [allergyInput, setAllergyInput] = useState('');
    const [allergies, setAllergies] = useState([]);

    const [maxCookTime, setMaxCookTime] = useState(120);
    const [maxCalories, setMaxCalories] = useState(1000);
    const [maxBudget, setMaxBudget] = useState('');

    const handleArrayToggle = (item, array, setArray) => {
        if (array.includes(item)) {
            setArray(array.filter(i => i !== item));
        } else {
            setArray([...array, item]);
        }
    };

    const handleAddTag = (e, input, setInput, array, setArray) => {
        if (e.key === 'Enter' && input.trim() !== '') {
            e.preventDefault();
            if (!array.includes(input.trim())) {
                setArray([...array, input.trim()]);
            }
            setInput('');
        }
    };

    const removeTag = (index, array, setArray) => {
        setArray(array.filter((_, i) => i !== index));
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        onSubmit({
            diet: diet || null,
            cuisine: cuisine.length > 0 ? cuisine : null,
            taste: taste.length > 0 ? taste : null,
            ingredients: ingredients.length > 0 ? ingredients : null,
            allergies: allergies.length > 0 ? allergies : null,
            maxCookTimeMinutes: maxCookTime,
            maxCalories: maxCalories,
            maxBudget: maxBudget ? parseFloat(maxBudget) : null
        });
    };

    const handleReset = () => {
        setDiet('');
        setCuisine([]);
        setTaste([]);
        setIngredients([]);
        setAllergies([]);
        setMaxCookTime(120);
        setMaxCalories(1000);
        setMaxBudget('');
        onReset();
    };

    return (
        <form onSubmit={handleSubmit} className="bg-white dark:bg-gray-800 p-6 rounded-xl shadow-sm border border-gray-100 dark:border-gray-700">
            <h2 className="text-xl font-bold mb-4 text-gray-800 dark:text-gray-100">Find Your Perfect Meal</h2>
            
            <div className="space-y-6">
                {/* Diet */}
                <div>
                    <h3 className="text-sm font-semibold text-gray-700 dark:text-gray-300 mb-2">Diet Type</h3>
                    <div className="flex flex-wrap gap-2">
                        {DIETS.map(d => (
                            <FilterBadge 
                                key={d} 
                                label={d} 
                                active={diet === d} 
                                onClick={() => setDiet(diet === d ? '' : d)} 
                            />
                        ))}
                    </div>
                </div>

                {/* Cuisine */}
                <div>
                    <h3 className="text-sm font-semibold text-gray-700 dark:text-gray-300 mb-2">Cuisine</h3>
                    <div className="flex flex-wrap gap-2">
                        {CUISINES.map(c => (
                            <FilterBadge 
                                key={c} 
                                label={c} 
                                active={cuisine.includes(c)} 
                                onClick={() => handleArrayToggle(c, cuisine, setCuisine)} 
                            />
                        ))}
                    </div>
                </div>

                {/* Taste */}
                <div>
                    <h3 className="text-sm font-semibold text-gray-700 dark:text-gray-300 mb-2">Taste Profile</h3>
                    <div className="flex flex-wrap gap-2">
                        {TASTES.map(t => (
                            <FilterBadge 
                                key={t} 
                                label={t} 
                                active={taste.includes(t)} 
                                onClick={() => handleArrayToggle(t, taste, setTaste)} 
                            />
                        ))}
                    </div>
                </div>

                {/* Ingredients & Allergies */}
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div>
                        <h3 className="text-sm font-semibold text-gray-700 dark:text-gray-300 mb-2">I have these ingredients</h3>
                        <input 
                            type="text" 
                            placeholder="Type and press Enter..." 
                            value={ingredientInput}
                            onChange={(e) => setIngredientInput(e.target.value)}
                            onKeyDown={(e) => handleAddTag(e, ingredientInput, setIngredientInput, ingredients, setIngredients)}
                            className="w-full p-2 border border-gray-300 dark:border-gray-600 rounded-md bg-transparent dark:text-white"
                        />
                        <div className="flex flex-wrap gap-2 mt-2">
                            {ingredients.map((ing, idx) => (
                                <span key={idx} className="bg-green-100 text-green-800 text-xs px-2 py-1 rounded flex items-center">
                                    {ing}
                                    <button type="button" onClick={() => removeTag(idx, ingredients, setIngredients)} className="ml-1 font-bold">&times;</button>
                                </span>
                            ))}
                        </div>
                    </div>
                    <div>
                        <h3 className="text-sm font-semibold text-gray-700 dark:text-gray-300 mb-2">Allergies / Dislikes</h3>
                        <input 
                            type="text" 
                            placeholder="Type and press Enter..." 
                            value={allergyInput}
                            onChange={(e) => setAllergyInput(e.target.value)}
                            onKeyDown={(e) => handleAddTag(e, allergyInput, setAllergyInput, allergies, setAllergies)}
                            className="w-full p-2 border border-gray-300 dark:border-gray-600 rounded-md bg-transparent dark:text-white"
                        />
                        <div className="flex flex-wrap gap-2 mt-2">
                            {allergies.map((alg, idx) => (
                                <span key={idx} className="bg-red-100 text-red-800 text-xs px-2 py-1 rounded flex items-center">
                                    {alg}
                                    <button type="button" onClick={() => removeTag(idx, allergies, setAllergies)} className="ml-1 font-bold">&times;</button>
                                </span>
                            ))}
                        </div>
                    </div>
                </div>

                {/* Sliders & Numbers */}
                <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                    <div>
                        <h3 className="text-sm font-semibold text-gray-700 dark:text-gray-300 mb-2">Max Time: {maxCookTime} mins</h3>
                        <input type="range" min="5" max="120" value={maxCookTime} onChange={(e) => setMaxCookTime(e.target.value)} className="w-full" />
                    </div>
                    <div>
                        <h3 className="text-sm font-semibold text-gray-700 dark:text-gray-300 mb-2">Max Calories: {maxCalories} kcal</h3>
                        <input type="range" min="100" max="1000" step="50" value={maxCalories} onChange={(e) => setMaxCalories(e.target.value)} className="w-full" />
                    </div>
                    <div>
                        <h3 className="text-sm font-semibold text-gray-700 dark:text-gray-300 mb-2">Max Budget ($)</h3>
                        <input type="number" min="0" step="0.5" value={maxBudget} onChange={(e) => setMaxBudget(e.target.value)} placeholder="Optional" className="w-full p-2 border border-gray-300 dark:border-gray-600 rounded-md bg-transparent dark:text-white" />
                    </div>
                </div>

                {/* Buttons */}
                <div className="flex gap-4 pt-4 border-t dark:border-gray-700">
                    <button type="submit" className="flex-1 bg-primary hover:bg-orange-600 text-white font-semibold py-2 px-4 rounded-md flex items-center justify-center gap-2 transition-colors">
                        <Search size={18} /> Get Recommendations
                    </button>
                    <button type="button" onClick={handleReset} className="px-4 py-2 border border-gray-300 dark:border-gray-600 text-gray-700 dark:text-gray-300 rounded-md hover:bg-gray-50 dark:hover:bg-gray-700 transition-colors">
                        Reset
                    </button>
                </div>
            </div>
        </form>
    );
};

export default FilterForm;
