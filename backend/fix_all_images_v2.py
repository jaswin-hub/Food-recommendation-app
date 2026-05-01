import re
import requests

filepath = r'c:\for 2nd sem related things\New folder (2)\app\backend\src\main\java\com\foodapp\data\RecipeDataStore.java'

with open(filepath, 'r', encoding='utf-8') as f:
    lines = f.readlines()

FALLBACKS = {
    "Veg": "https://www.themealdb.com/images/media/meals/wxyvqq1511723401.jpg",
    "Non-Veg": "https://www.themealdb.com/images/media/meals/1529444107.jpg",
    "Vegan": "https://www.themealdb.com/images/media/meals/vuyvrt1468710501.jpg",
    "Keto": "https://www.themealdb.com/images/media/meals/1548772327.jpg",
    "High Protein": "https://www.themealdb.com/images/media/meals/1529442454.jpg",
    "Low Calorie": "https://www.themealdb.com/images/media/meals/fqpqml1764359125.jpg"
}

OVERRIDES = {
    "Chicken Quinoa Bowl": "https://www.themealdb.com/images/media/meals/vtqxtu1511784197.jpg",
    "Lentil Soup": "https://www.themealdb.com/images/media/meals/58o7id1593912466.jpg",
    "Zucchini Lasagna": "https://upload.wikimedia.org/wikipedia/commons/1/15/Vegan_Lasagna_made_w_zucchini_%2842356067310%29.jpg",
    "Roasted Chickpeas": "https://upload.wikimedia.org/wikipedia/commons/3/30/Roasted_chickpeas.jpg",
    "Egg White Omelet": "https://upload.wikimedia.org/wikipedia/commons/2/24/Five_egg_white_fluffy_omlette.jpg",
    "Tofu Stir Fry": "https://www.themealdb.com/images/media/meals/minfsc1763766806.jpg",
    "Greek Yogurt Parfait": "https://upload.wikimedia.org/wikipedia/commons/5/5b/Yogurt_Parfait.jpg",
    "Cauliflower Crust Pizza": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Cauliflower_Pizza.jpg/800px-Cauliflower_Pizza.jpg",
    "Turkey Lettuce Wraps": "https://www.themealdb.com/images/media/meals/pk8wtn1763758591.jpg",
    "Berry Spinach Salad": "https://www.themealdb.com/images/media/meals/fqpqml1764359125.jpg",
    "Beef and Cabbage Stir Fry": "https://www.themealdb.com/images/media/meals/z0ageb1583189517.jpg",
    "Chia Seed Pudding": "https://upload.wikimedia.org/wikipedia/commons/b/b9/Chia_Seed_Pudding.jpg",
    "Paneer Butter Masala": "https://upload.wikimedia.org/wikipedia/commons/1/19/Paneer_butter_masala_2.jpg",
    "Dal Tadka": "https://upload.wikimedia.org/wikipedia/commons/b/b5/Dal_Tadka_at_29%2C_Vaikunthlal_Mehta_Rd%2C_Navpada%2C_Vile_Parle_West%2C_Mumbai.jpg",
    "Chicken Tikka Masala": "https://upload.wikimedia.org/wikipedia/commons/4/44/Chicken_Tikka_Masala_KellySue.JPG",
    "Paneer Tikka": "https://upload.wikimedia.org/wikipedia/commons/6/66/Paneer_tikka_1.jpg",
    "Sushi Platter": "https://www.themealdb.com/images/media/meals/g046bb1663960946.jpg",
    "Veggie Burger": "https://upload.wikimedia.org/wikipedia/commons/4/41/The_ultimate_veggie_burger.jpg",
    "Chicken Pho": "https://theyummybowl.com/wp-content/uploads/kung-pao-chicken-n-10-of-11.jpg",
    "Ratatouille": "https://www.themealdb.com/images/media/meals/vuyvrt1468710501.jpg",
    "Butter Chicken": "https://upload.wikimedia.org/wikipedia/commons/3/3c/Chicken_makhani.jpg"
}

def get_best_image(name, diet):
    if name in OVERRIDES:
        return OVERRIDES[name]
    
    # Try MealDB
    try:
        search_url = f"https://www.themealdb.com/api/json/v1/1/search.php?s={name.replace(' ', '%20')}"
        r = requests.get(search_url, timeout=3).json()
        if r['meals']:
            return r['meals'][0]['strMealThumb']
    except:
        pass
    
    return FALLBACKS.get(diet, FALLBACKS["Non-Veg"])

new_lines = []
for line in lines:
    # 1. Fix corrupted ingredients in the line
    line = re.sub(r'new Ingredient\("(.*?)",\s*"https?://.*?",\s*"(.*?)",', r'new Ingredient("\1", "\2",', line)
    
    # 2. Fix the recipe image URL (last string but one)
    if 'recipes.add(new Recipe(' in line:
        strings = re.findall(r'"(.*?)"', line)
        if len(strings) >= 11:
            name = strings[1]
            diet = strings[3]
            old_url = strings[-2]
            meal_type = strings[-1]
            
            new_url = get_best_image(name, diet)
            
            # Replace the old_url precisely
            line = line.replace(f'"{old_url}", "{meal_type}"', f'"{new_url}", "{meal_type}"')
            
    new_lines.append(line)

with open(filepath, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Fixed RecipeDataStore.java: Restored ingredients and updated all 100 images.")
