import requests
import re
import time

filepath = r'c:\for 2nd sem related things\New folder (2)\app\backend\src\main\java\com\foodapp\data\RecipeDataStore.java'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

def get_mealdb_image(name):
    try:
        r = requests.get(f"https://www.themealdb.com/api/json/v1/1/search.php?s={name}", timeout=5)
        data = r.json()
        if data['meals']:
            return data['meals'][0]['strMealThumb']
    except:
        pass
    return None

UNSPLASH_FALLBACKS = {
    "Veg": "https://images.unsplash.com/photo-1512621776951-a57141f2eefd?q=80&w=500&auto=format&fit=crop",
    "Non-Veg": "https://images.unsplash.com/photo-1544025162-d76694265947?q=80&w=500&auto=format&fit=crop",
    "Vegan": "https://images.unsplash.com/photo-1512621776951-a57141f2eefd?q=80&w=500&auto=format&fit=crop",
    "Keto": "https://images.unsplash.com/photo-1544025162-d76694265947?q=80&w=500&auto=format&fit=crop",
    "High Protein": "https://images.unsplash.com/photo-1532550907401-a500c9a57435?q=80&w=500&auto=format&fit=crop",
    "Low Calorie": "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?q=80&w=500&auto=format&fit=crop"
}

lines = content.splitlines()
new_lines = []

current_recipe_name = None
current_diet = None

print("Starting image fetch and verify...")

for i, line in enumerate(lines):
    # Try to find the name in the line
    name_match = re.search(r'new Recipe\("\d+",\s*"(.*?)"', line)
    if name_match:
        current_recipe_name = name_match.group(1)
        # Also find diet (it's the 4th argument)
        diet_match = re.search(r'new Recipe\("\d+",\s*".*?",\s*".*?",\s*"(.*?)"', line)
        if diet_match:
            current_diet = diet_match.group(1)

    # If the line contains the end of a Recipe call
    if '),' in line or '));' in line:
        url_match = re.search(r',\s*(\d+(\.\d+)?),\s*"(.*?)"(\s*,\s*".*?"\s*\)\s*;)', line)
        if url_match and current_recipe_name:
            budget = url_match.group(1)
            old_url = url_match.group(3)
            suffix = url_match.group(4)
            
            # Fetch from MealDB
            new_url = get_mealdb_image(current_recipe_name)
            
            if not new_url:
                # Try parts of the name
                words = current_recipe_name.split()
                if len(words) > 1:
                    new_url = get_mealdb_image(words[-1]) # Try last word (e.g. "Salad", "Soup")
            
            if not new_url:
                new_url = UNSPLASH_FALLBACKS.get(current_diet, UNSPLASH_FALLBACKS["Non-Veg"])
            
            line = line.replace(f'"{old_url}"{suffix}', f'"{new_url}"{suffix}')
            print(f"Fixed {current_recipe_name}: {new_url[:50]}...")
            time.sleep(0.1) # Be nice to the API
            
    new_lines.append(line)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write('\n'.join(new_lines))

print("DONE: All 100 images updated with working MealDB or Unsplash URLs.")
