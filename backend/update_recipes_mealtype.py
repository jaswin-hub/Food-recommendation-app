import re

filepath = r'c:\for 2nd sem related things\New folder (2)\app\backend\src\main\java\com\foodapp\data\RecipeDataStore.java'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

def get_meal_type(name):
    name = name.lower()
    if any(x in name for x in ['omelet', 'parfait', 'pancake', 'breakfast', 'smoothie', 'cereal', 'toast', 'egg']):
        return "Breakfast"
    if any(x in name for x in ['salad', 'wrap', 'bowl', 'sandwich', 'burger', 'taco', 'hummus', 'snack', 'bites', 'chickpeas', 'popcorn', 'nuts']):
        if any(x in name for x in ['hummus', 'bites', 'chickpeas', 'popcorn', 'nuts']):
            return "Snack"
        return "Lunch"
    return "Dinner"

# Match new Recipe(...) calls that only have 11 arguments
# We look for calls that don't already have the 12th argument (mealType)
# A simple way is to match until the closing ));

# Match new Recipe(...)
def process_content(text):
    results = []
    pos = 0
    pattern = re.compile(r'new Recipe\(')
    while True:
        match = pattern.search(text, pos)
        if not match:
            break
        
        # Find the end of this call by matching parentheses
        start = match.start()
        end = -1
        depth = 1
        i = match.end()
        while i < len(text):
            if text[i] == '(':
                depth += 1
            elif text[i] == ')':
                depth -= 1
                if depth == 0:
                    end = i + 1
                    break
            i += 1
        
        if end != -1:
            call = text[start:end]
            # Check number of top-level commas
            # This is hard because of nested lists and Arrays.asList
            # But we can check if it already has 11 commas at top level
            # Actually, let's just check if the last argument is a string (imageUrl) or something else
            
            # Find the recipe name
            name_match = re.search(r'new Recipe\(".*?",\s*"(.*?)",', call)
            name = name_match.group(1) if name_match else ""
            meal_type = get_meal_type(name)
            
            # If the call ends with "));" then it's 11 args
            # If we already updated it, it might end with , "MealType"));
            if not re.search(r', "(Breakfast|Lunch|Dinner|Snack)"\)$', call):
                new_call = call[:-1] + ', "' + meal_type + '")'
                text = text[:start] + new_call + text[end:]
                pos = start + len(new_call)
            else:
                pos = end
        else:
            pos = match.end()
    return text

new_content = process_content(content)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Updated RecipeDataStore.java with mealType")
