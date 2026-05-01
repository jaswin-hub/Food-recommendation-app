import React, { useState, useEffect, useRef } from 'react';
import './App.css';

/* ─── Custom Dropdown ─────────────────────────────────────── */
const CustomDropdown = ({ value, onChange, options, placeholder }) => {
  const [open, setOpen] = useState(false);
  const ref = useRef(null);

  // Close on outside click
  useEffect(() => {
    const handler = (e) => {
      if (ref.current && !ref.current.contains(e.target)) setOpen(false);
    };
    document.addEventListener('mousedown', handler);
    return () => document.removeEventListener('mousedown', handler);
  }, []);

  const selected = options.find((o) => o === value) || null;

  return (
    <div className="cdd" ref={ref}>
      <button
        type="button"
        className={`cdd__trigger${open ? ' cdd__trigger--open' : ''}`}
        onClick={() => setOpen((prev) => !prev)}
        aria-haspopup="listbox"
        aria-expanded={open}
      >
        <span className={`cdd__trigger-label${!selected ? ' cdd__trigger-label--placeholder' : ''}`}>
          {selected || placeholder}
        </span>
        <span className={`cdd__chevron${open ? ' cdd__chevron--open' : ''}`}>
          <svg width="12" height="8" viewBox="0 0 12 8" fill="none" aria-hidden="true">
            <path d="M1 1L6 6L11 1" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round"/>
          </svg>
        </span>
      </button>

      <div className={`cdd__menu${open ? ' cdd__menu--open' : ''}`} role="listbox">
        {/* "Any" option */}
        <div
          role="option"
          aria-selected={value === ''}
          className={`cdd__option${value === '' ? ' cdd__option--selected' : ''}`}
          onMouseDown={() => { onChange(''); setOpen(false); }}
        >
          {placeholder}
        </div>
        {options.map((opt) => (
          <div
            key={opt}
            role="option"
            aria-selected={value === opt}
            className={`cdd__option${value === opt ? ' cdd__option--selected' : ''}`}
            onMouseDown={() => { onChange(opt); setOpen(false); }}
          >
            {opt}
          </div>
        ))}
      </div>
    </div>
  );
};
/* ─────────────────────────────────────────────────────────── */

const App = () => {
  const [recipes, setRecipes] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  
  // Navigation State
  const [selectedRecipe, setSelectedRecipe] = useState(null);
  const savedScrollY = useRef(0);

  // Form State
  const [diet, setDiet] = useState('');
  const [cuisine, setCuisine] = useState('');
  const [taste, setTaste] = useState('');
  const [ingredientInput, setIngredientInput] = useState('');
  const [goal, setGoal] = useState('');
  const [mealType, setMealType] = useState('');
  const [quickOnly, setQuickOnly] = useState(false);

  // Dropdown Options
  const DIETS = ['Veg', 'Non-Veg', 'Vegan', 'Keto', 'High Protein', 'Low Calorie'];
  const CUISINES = ['Indian', 'Chinese', 'Italian', 'Korean', 'Mexican', 'Japanese', 'American'];
  const TASTES = ['Spicy', 'Sweet', 'Sour', 'Salty', 'Savory', 'Mild'];
  const GOALS = ['Fat Loss', 'Muscle Gain', 'Maintenance'];
  const MEAL_TYPES = ['Breakfast', 'Lunch', 'Dinner', 'Snack'];

  useEffect(() => {
    fetchAllRecipes();
  }, []);

  const fetchAllRecipes = async () => {
    setLoading(true);
    setError(null);
    try {
      const response = await fetch('http://localhost:8080/api/recipes');
      if (!response.ok) throw new Error('Failed to fetch recipes');
      const data = await response.json();
      setRecipes(data || []);
    } catch (err) {
      setError('Error loading recipes');
    } finally {
      setLoading(false);
    }
  };

  const handleSearch = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null);

    const payload = {
      diet: diet || null,
      cuisine: cuisine ? [cuisine] : [],
      taste: taste ? [taste] : [],
      ingredients: ingredientInput
          .split(",")
          .map(i => i.trim())
          .filter(i => i.length > 0),
      allergies: [],
      maxCookTimeMinutes: quickOnly ? 20 : null,
      maxCalories: null,
      maxBudget: null,
      goal: goal || null,
      mealType: mealType || null
    };

    try {
      const response = await fetch('http://localhost:8080/api/recommend', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(payload),
      });
      if (!response.ok) throw new Error('Failed to fetch recommendations');
      const data = await response.json();
      setRecipes(data || []);
    } catch (err) {
      setError('Error loading recipes');
    } finally {
      setLoading(false);
    }
  };

  const handleReset = () => {
    setDiet('');
    setCuisine('');
    setTaste('');
    setIngredientInput('');
    setGoal('');
    setMealType('');
    setQuickOnly(false);
    fetchAllRecipes();
  };

  // Safe Extraction Logic to handle both Recipe and ScoredRecipe
  const getSafeRecipe = (r) => {
    if (!r) return null;
    return r.recipe ? r.recipe : r;
  };

  // --- DETAIL VIEW ---
  if (selectedRecipe) {
    const r = getSafeRecipe(selectedRecipe);
    return (
      <div className="detail-page">

        {/* ── Hero banner ── */}
        <div className="detail-page__hero">
          {r.imageUrl
            ? <img src={r.imageUrl} alt={r.name} className="detail-page__hero-img" />
            : <div className="detail-page__hero-placeholder" />}
          <div className="detail-page__hero-overlay">
            {/* Back button — top-left frosted glass */}
            <button
              onClick={() => {
                setSelectedRecipe(null);
                requestAnimationFrame(() => window.scrollTo(0, savedScrollY.current));
              }}
              className="detail-page__back-btn"
              aria-label="Back to results">
              ←
            </button>
            {/* Recipe name — bottom-left */}
            <h1 className="detail-page__title">{r.name}</h1>
          </div>
        </div>

        {/* ── Content body ── */}
        <div className="detail-page__body">

          {/* Row 1 — pill badges + stat cards */}
          <div className="detail-page__meta-row">
            <div className="detail-page__badges">
              {r.cuisine && <span className="detail-page__tag detail-page__tag--cuisine">{r.cuisine}</span>}
              {r.diet    && <span className="detail-page__tag detail-page__tag--diet">{r.diet}</span>}
              {r.taste   && <span className="detail-page__tag detail-page__tag--taste">{r.taste}</span>}
              {selectedRecipe.matchPercentage > 0 && (
                <span className="detail-page__tag detail-page__tag--match">
                  🎯 {selectedRecipe.matchPercentage}% match
                </span>
              )}
            </div>
            <div className="detail-page__stats">
              <div className="detail-page__stat-card">
                <span className="detail-page__stat-icon">🕒</span>
                <span className="detail-page__stat-value">{r.cookTimeMinutes}</span>
                <span className="detail-page__stat-label">mins</span>
              </div>
              <div className="detail-page__stat-card">
                <span className="detail-page__stat-icon">🔥</span>
                <span className="detail-page__stat-value">{r.calories}</span>
                <span className="detail-page__stat-label">kcal</span>
              </div>
              {selectedRecipe.score > 0 && (
                <div className="detail-page__stat-card">
                  <span className="detail-page__stat-icon">🏆</span>
                  <span className="detail-page__stat-value">{selectedRecipe.score}</span>
                  <span className="detail-page__stat-label">pts</span>
                </div>
              )}
            </div>
          </div>

          {/* Row 2 — Ingredients card */}
          <div className="detail-page__card">
            <h2 className="detail-page__card-title">Ingredients</h2>
            {r.ingredients && r.ingredients.length > 0 ? (
              <ul className="detail-page__ingredients">
                {r.ingredients.map((ing, idx) => (
                  <li key={idx} className="detail-page__ingredient">
                    <span className="detail-page__ingredient-qty">{ing.quantity}</span>
                    <span className="detail-page__ingredient-name">{ing.name}</span>
                  </li>
                ))}
              </ul>
            ) : (
              <p className="detail-page__empty">No ingredients listed.</p>
            )}
          </div>

          {/* Row 3 — Steps card */}
          <div className="detail-page__card">
            <h2 className="detail-page__card-title">Cooking Steps</h2>
            {r.steps && r.steps.length > 0 ? (
              <ol className="detail-page__steps">
                {r.steps.map((step, idx) => (
                  <li key={idx} className="detail-page__step">
                    <span className="detail-page__step-num">{idx + 1}</span>
                    <span className="detail-page__step-text">{step}</span>
                  </li>
                ))}
              </ol>
            ) : (
              <p className="detail-page__empty">No steps listed.</p>
            )}
          </div>

        </div>
      </div>
    );
  }

  // --- LIST VIEW ---
  return (
    <div className="app-shell">
      {/* HERO SECTION */}
      <div className="hero-section">
        <h1 className="hero-section__title">Smart Food Recommender</h1>
        <p className="hero-section__subtitle">Eat Healthy. Cook Smart.</p>
      </div>
      
      {/* FILTER FORM */}
      <div className="filter-card">
        <h2 className="filter-card__heading">🔍 Find Your Perfect Meal</h2>
        <form onSubmit={handleSearch} className="filter-form">

          {/* Row 1: Custom Dropdowns */}
          <div className="filter-form__row">
            <div className="filter-form__field">
              <label className="filter-form__label">Diet</label>
              <CustomDropdown
                value={diet}
                onChange={setDiet}
                options={DIETS}
                placeholder="Any Diet"
              />
            </div>
            <div className="filter-form__field">
              <label className="filter-form__label">Cuisine</label>
              <CustomDropdown
                value={cuisine}
                onChange={setCuisine}
                options={CUISINES}
                placeholder="Any Cuisine"
              />
            </div>
            <div className="filter-form__field">
              <label className="filter-form__label">Taste</label>
              <CustomDropdown
                value={taste}
                onChange={setTaste}
                options={TASTES}
                placeholder="Any Taste"
              />
            </div>
          </div>

          {/* Row 2: Ingredients */}
          <div className="filter-form__field">
            <label className="filter-form__label">Ingredients you have</label>
            <input 
              type="text" 
              placeholder="e.g. paneer, tomato, onion" 
              value={ingredientInput} 
              onChange={(e) => setIngredientInput(e.target.value)} 
              className="filter-form__input"
            />
          </div>

          {/* Row 3: Chips */}
          <div className="filter-form__row">
            <div className="filter-form__field">
              <label className="filter-form__label">Health Goal</label>
              <div className="filter-form__chips">
                {GOALS.map(g => (
                  <button
                    key={g}
                    type="button"
                    onClick={() => setGoal(goal === g ? '' : g)}
                    className={`filter-form__chip filter-form__chip--goal ${goal === g ? 'active' : ''}`}
                  >
                    {g}
                  </button>
                ))}
              </div>
            </div>

            <div className="filter-form__field">
              <label className="filter-form__label">Meal Type</label>
              <div className="filter-form__chips">
                {MEAL_TYPES.map(m => (
                  <button
                    key={m}
                    type="button"
                    onClick={() => setMealType(mealType === m ? '' : m)}
                    className={`filter-form__chip filter-form__chip--meal ${mealType === m ? 'active' : ''}`}
                  >
                    {m}
                  </button>
                ))}
              </div>
            </div>
          </div>

          {/* Row 4: Quick toggle */}
          <label className="filter-form__checkbox-wrap" htmlFor="quick">
            <input 
              type="checkbox" 
              id="quick" 
              checked={quickOnly} 
              onChange={(e) => setQuickOnly(e.target.checked)} 
              className="filter-form__checkbox"
            />
            <span className="filter-form__checkbox-label">⚡ Quick meals only (≤ 20 min)</span>
          </label>

          {/* Row 5: Actions */}
          <div className="filter-form__actions">
            <button type="submit" className="filter-form__btn filter-form__btn--primary">
              Find Recipes
            </button>
            <button type="button" onClick={handleReset} className="filter-form__btn filter-form__btn--secondary">
              Reset
            </button>
          </div>
        </form>
      </div>

      {/* RESULTS GRID */}
      <div className="results-section">
        {loading && (
          <div className="state-msg state-msg--loading">
            <div className="state-msg__spinner"></div>
            <p className="state-msg__text">Finding delicious recipes for you…</p>
          </div>
        )}
        {error && (
          <div className="state-msg state-msg--error">
            <span className="state-msg__icon">⚠️</span>
            <p className="state-msg__text">{error}</p>
          </div>
        )}
        
        {!loading && !error && recipes.length === 0 && (
          <div className="state-msg state-msg--empty">
            <span className="state-msg__icon">🍽️</span>
            <h2 className="state-msg__title">No recipes found</h2>
            <p className="state-msg__text">Try adjusting your filters or explore a different cuisine.</p>
          </div>
        )}

        {!loading && !error && recipes.length > 0 && (
          <div className="recipe-grid">
            {recipes.map((item, index) => {
              const recipe = getSafeRecipe(item);
              if (!recipe || !recipe.name) return null;

              return (
                <div 
                  key={recipe.id || index} 
                  className="recipe-card"
                  onClick={() => {
                    savedScrollY.current = window.scrollY;
                    setSelectedRecipe(item);
                    window.scrollTo(0, 0);
                  }}
                >
                  {/* Image with zoom + overlay */}
                  <div className="recipe-card__img-wrap">
                    <img 
                      className="recipe-card__img"
                      src={recipe.imageUrl || "https://placehold.co/600x400/eee/999?text=No+Image"} 
                      alt={recipe.name} 
                    />
                    <div className="recipe-card__overlay">{recipe.name}</div>

                    {/* Match percentage badge */}
                    {item.matchPercentage > 0 && (
                      <div className="recipe-card__match-badge">
                        {item.matchPercentage}% match
                      </div>
                    )}
                  </div>

                  {/* Card body */}
                  <div className="recipe-card__body">
                    <div className="recipe-card__tags">
                      {recipe.diet === 'Low Calorie' && (
                        <span className="recipe-card__tag recipe-card__tag--low-cal">Low Cal</span>
                      )}
                      {recipe.diet === 'High Protein' && (
                        <span className="recipe-card__tag recipe-card__tag--high-protein">High Protein</span>
                      )}
                      {recipe.steps && recipe.steps.length < 5 && (
                        <span className="recipe-card__tag recipe-card__tag--easy">✨ Easy</span>
                      )}
                    </div>

                    <div className="recipe-card__meta">
                      <span>🕒 {recipe.cookTimeMinutes}m</span>
                      <span>🔥 {recipe.calories} kcal</span>
                    </div>
                  </div>
                </div>
              );
            })}
          </div>
        )}
      </div>
    </div>
  );
};

export default App;