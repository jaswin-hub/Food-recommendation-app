import axios from 'axios';

const api = axios.create({
    baseURL: 'http://localhost:8080/api',
});

export const getRecipes = async () => {
    const response = await api.get('/recipes');
    return response.data;
};

export const getRecommendations = async (filters) => {
    const response = await api.post('/recommend', filters);
    return response.data;
};
