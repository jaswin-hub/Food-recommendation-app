import React from 'react';

const FilterBadge = ({ label, active, onClick }) => {
    return (
        <button
            type="button"
            onClick={onClick}
            className={`px-3 py-1 rounded-full text-sm font-medium transition-colors ${
                active 
                ? 'bg-primary text-white' 
                : 'bg-gray-200 text-gray-700 hover:bg-gray-300 dark:bg-gray-700 dark:text-gray-200 dark:hover:bg-gray-600'
            }`}
        >
            {label}
        </button>
    );
};

export default FilterBadge;
