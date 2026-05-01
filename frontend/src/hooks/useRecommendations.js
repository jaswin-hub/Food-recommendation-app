import { useState } from 'react';
import { getRecommendations, getRecipes } from '../api/recipeApi';

export const useRecommendations = () => {
    const [recipes, setRecipes] = useState([]);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    const fetchAllRecipes = async () => {
        setLoading(true);
        setError(null);
        try {
            const data = await getRecipes();
            // Wrap in scored recipe format for consistency if needed, or just set
            setRecipes(data.map(r => ({ ...r, score: 0, fallbackSuggestion: false })));
        } catch (err) {
            setError(err.message || 'Failed to fetch recipes');
        } finally {
            setLoading(false);
        }
    };

    const fetchRecommendations = async (filters) => {
        setLoading(true);
        setError(null);
        try {
            const data = await getRecommendations(filters);
            setRecipes(data);
        } catch (err) {
            setError(err.message || 'Failed to fetch recommendations');
        } finally {
            setLoading(false);
        }
    };

    return { recipes, loading, error, fetchAllRecipes, fetchRecommendations };
};
