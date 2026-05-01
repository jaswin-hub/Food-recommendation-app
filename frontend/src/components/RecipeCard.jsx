import React, { useState } from 'react';
import { Clock, Flame, Info, CheckCircle2 } from 'lucide-react';
import { motion } from 'framer-motion';

const RecipeCard = ({ recipe }) => {
    const [showDetails, setShowDetails] = useState(false);

    // Calculate score color
    const getScoreColor = (score) => {
        if (!score) return 'bg-gray-200';
        if (score > 70) return 'bg-green-500';
        if (score > 40) return 'bg-yellow-500';
        return 'bg-red-500';
    };

    return (
        <motion.div 
            initial={{ opacity: 0, y: 10 }}
            animate={{ opacity: 1, y: 0 }}
            className="bg-white dark:bg-gray-800 rounded-xl overflow-hidden shadow-sm border border-gray-100 dark:border-gray-700 hover:shadow-md transition-shadow"
        >
            <div className="p-5">
                <div className="flex justify-between items-start mb-2">
                    <h3 className="text-xl font-bold text-gray-800 dark:text-gray-100">{recipe.name}</h3>
                    {recipe.fallbackSuggestion && (
                        <span className="bg-yellow-100 text-yellow-800 text-xs px-2 py-1 rounded font-medium">
                            Fallback Match
                        </span>
                    )}
                </div>
                
                <div className="flex flex-wrap gap-2 mb-4">
                    <span className="bg-orange-100 text-orange-800 text-xs px-2 py-1 rounded">{recipe.cuisine}</span>
                    <span className="bg-green-100 text-green-800 text-xs px-2 py-1 rounded">{recipe.diet}</span>
                    <span className="bg-blue-100 text-blue-800 text-xs px-2 py-1 rounded">{recipe.taste}</span>
                </div>

                <div className="flex items-center gap-4 text-sm text-gray-600 dark:text-gray-400 mb-4">
                    <div className="flex items-center gap-1">
                        <Clock size={16} />
                        <span>{recipe.cookTimeMinutes} mins</span>
                    </div>
                    <div className="flex items-center gap-1">
                        <Flame size={16} />
                        <span>{recipe.calories} kcal</span>
                    </div>
                </div>

                {recipe.score !== undefined && recipe.score > 0 && (
                    <div className="mb-4">
                        <div className="flex justify-between text-xs mb-1">
                            <span className="text-gray-600 dark:text-gray-400">Match Score</span>
                            <span className="font-bold">{recipe.score} pts</span>
                        </div>
                        <div className="w-full bg-gray-200 rounded-full h-2">
                            <div className={`h-2 rounded-full ${getScoreColor(recipe.score)}`} style={{ width: `${Math.min(recipe.score, 100)}%` }}></div>
                        </div>
                    </div>
                )}

                <button 
                    onClick={() => setShowDetails(!showDetails)}
                    className="w-full mt-2 py-2 text-primary border border-primary rounded-md hover:bg-orange-50 dark:hover:bg-gray-700 transition-colors flex items-center justify-center gap-2"
                >
                    <Info size={18} /> {showDetails ? 'Hide Details' : 'View Recipe'}
                </button>

                {/* Expanded Details */}
                {showDetails && (
                    <motion.div 
                        initial={{ height: 0, opacity: 0 }}
                        animate={{ height: 'auto', opacity: 1 }}
                        className="mt-4 pt-4 border-t dark:border-gray-700"
                    >
                        <div className="mb-4">
                            <h4 className="font-semibold text-gray-800 dark:text-gray-200 mb-2 text-sm uppercase tracking-wider">Ingredients</h4>
                            <ul className="text-sm space-y-1">
                                {recipe.ingredients.map((ing, idx) => (
                                    <li key={idx} className="flex justify-between text-gray-600 dark:text-gray-400">
                                        <span className="flex items-center gap-1">
                                            {ing.allergen && <span className="w-2 h-2 rounded-full bg-red-500 inline-block mr-1" title="Allergen"></span>}
                                            {ing.name}
                                        </span>
                                        <span className="font-medium text-gray-500">{ing.quantity}</span>
                                    </li>
                                ))}
                            </ul>
                        </div>
                        
                        <div>
                            <h4 className="font-semibold text-gray-800 dark:text-gray-200 mb-2 text-sm uppercase tracking-wider">Instructions</h4>
                            <ol className="text-sm space-y-2">
                                {recipe.steps.map((step, idx) => (
                                    <li key={idx} className="flex items-start gap-2 text-gray-600 dark:text-gray-400">
                                        <CheckCircle2 size={16} className="text-primary mt-0.5 flex-shrink-0" />
                                        <span>{step}</span>
                                    </li>
                                ))}
                            </ol>
                        </div>
                    </motion.div>
                )}
            </div>
        </motion.div>
    );
};

export default RecipeCard;
