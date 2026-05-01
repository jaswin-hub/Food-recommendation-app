import re

filepath = r'c:\for 2nd sem related things\New folder (2)\app\backend\src\main\java\com\foodapp\data\RecipeDataStore.java'

# Reconstruct 61-100 with correct ingredients and images
RECIPES_61_100 = """
        // New Recipes 61-100 (Focusing on Diet-Friendly majority)
        recipes.add(new Recipe("61", "Grilled Salmon with Asparagus", "American", "Keto", "Savory",
                Arrays.asList(new Ingredient("salmon fillet", "200g", false), new Ingredient("asparagus", "1 bunch", false), new Ingredient("olive oil", "1 tbsp", false), new Ingredient("lemon", "1/2", false)),
                420, 20, Arrays.asList("Preheat oven to 400°F (200°C).", "Place salmon and snapped asparagus on a baking sheet.", "Drizzle with olive oil, salt, and pepper.", "Bake for 12-15 minutes.", "Serve with fresh lemon wedges."), 15.0, "https://www.themealdb.com/images/media/meals/1548772327.jpg", "Dinner"));

        recipes.add(new Recipe("62", "Chicken Quinoa Bowl", "American", "High Protein", "Savory",
                Arrays.asList(new Ingredient("chicken breast", "150g", false), new Ingredient("quinoa", "1/2 cup cooked", false), new Ingredient("kale", "1 cup", false), new Ingredient("avocado", "1/2", false)),
                550, 25, Arrays.asList("Season and grill chicken breast until cooked through.", "Massage kale with a little olive oil and lemon juice.", "Combine cooked quinoa and kale in a bowl.", "Top with sliced chicken and avocado.", "Drizzle with tahini or balsamic glaze."), 10.0, "https://www.themealdb.com/images/media/meals/vtqxtu1511784197.jpg", "Lunch"));

        recipes.add(new Recipe("63", "Lentil Soup", "Indian", "Vegan", "Savory",
                Arrays.asList(new Ingredient("brown lentils", "1 cup", false), new Ingredient("carrot", "1 chopped", false), new Ingredient("celery", "1 stalk", false), new Ingredient("onion", "1 small", false)),
                280, 35, Arrays.asList("Sauté onion, carrots, and celery in a pot until soft.", "Add lentils, water or vegetable broth, and spices.", "Bring to a boil then simmer for 25-30 minutes.", "Blend a portion of the soup for creaminess.", "Garnish with fresh parsley and serve hot."), 5.0, "https://www.themealdb.com/images/media/meals/58o7id1593912466.jpg", "Dinner"));

        recipes.add(new Recipe("64", "Zucchini Lasagna", "Italian", "Keto", "Savory",
                Arrays.asList(new Ingredient("zucchini", "2 large", false), new Ingredient("ricotta cheese", "1 cup", true), new Ingredient("ground turkey", "200g", false), new Ingredient("marinara sauce", "1 cup", false)),
                380, 45, Arrays.asList("Slice zucchini into thin wide strips using a mandolin.", "Cook ground turkey with marinara sauce.", "Layer zucchini strips, turkey sauce, and ricotta in a baking dish.", "Repeat layers and top with mozzarella cheese.", "Bake at 375°F for 30 minutes until bubbling."), 12.0, "https://www.themealdb.com/images/media/meals/vuyvrt1468710501.jpg", "Dinner"));

        recipes.add(new Recipe("65", "Roasted Chickpeas", "Mexican", "Vegan", "Spicy",
                Arrays.asList(new Ingredient("canned chickpeas", "1 can", false), new Ingredient("olive oil", "1 tbsp", false), new Ingredient("chili powder", "1 tsp", false), new Ingredient("cumin", "1 tsp", false)),
                210, 30, Arrays.asList("Drain and pat chickpeas completely dry with paper towels.", "Toss with olive oil, chili powder, and cumin.", "Spread in a single layer on a baking sheet.", "Roast at 400°F for 25-30 minutes until crunchy.", "Let cool slightly for maximum crispness."), 3.0, "https://www.themealdb.com/images/media/meals/wxyvqq1511723401.jpg", "Snack"));

        recipes.add(new Recipe("66", "Egg White Omelet", "American", "Low Calorie", "Mild",
                Arrays.asList(new Ingredient("egg whites", "4", false), new Ingredient("spinach", "1/2 cup", false), new Ingredient("mushrooms", "1/4 cup", false), new Ingredient("onions", "1 tbsp", false)),
                120, 10, Arrays.asList("Sauté mushrooms and onions in a non-stick pan.", "Add spinach until wilted then remove veggies.", "Whisk egg whites and pour into the hot pan.", "When set, add veggies back and fold the omelet.", "Slide onto a plate and serve immediately."), 4.0, "https://www.themealdb.com/images/media/meals/1529446137.jpg", "Breakfast"));

        recipes.add(new Recipe("67", "Tofu Stir Fry", "Chinese", "Vegan", "Savory",
                Arrays.asList(new Ingredient("firm tofu", "200g", false), new Ingredient("broccoli", "1 cup", false), new Ingredient("bell peppers", "1 cup", false), new Ingredient("soy sauce", "2 tbsp", true)),
                310, 20, Arrays.asList("Press tofu to remove excess water and cut into cubes.", "Pan-fry tofu until golden brown on all sides.", "Add broccoli and peppers, stir-frying on high heat.", "Pour in soy sauce and a splash of sesame oil.", "Serve hot over brown rice or cauliflower rice."), 7.0, "https://www.themealdb.com/images/media/meals/minfsc1763766806.jpg", "Dinner"));

        recipes.add(new Recipe("68", "Greek Yogurt Parfait", "American", "High Protein", "Sweet",
                Arrays.asList(new Ingredient("greek yogurt", "1 cup", true), new Ingredient("berries", "1/2 cup", false), new Ingredient("honey", "1 tsp", false), new Ingredient("granola", "2 tbsp", true)),
                280, 5, Arrays.asList("Spoon half of the yogurt into a glass or bowl.", "Add a layer of fresh berries.", "Top with the remaining yogurt and berries.", "Drizzle with honey for natural sweetness.", "Sprinkle with granola right before serving for crunch."), 6.0, "https://www.themealdb.com/images/media/meals/uvuyxu1503067369.jpg", "Breakfast"));

        recipes.add(new Recipe("69", "Cauliflower Crust Pizza", "Italian", "Keto", "Savory",
                Arrays.asList(new Ingredient("cauliflower", "1 head", false), new Ingredient("egg", "1", false), new Ingredient("mozzarella", "1/2 cup", true), new Ingredient("tomato sauce", "1/4 cup", false)),
                350, 40, Arrays.asList("Process cauliflower into rice and steam until soft.", "Squeeze out all moisture using a kitchen towel.", "Mix cauliflower with egg and mozzarella to form a dough.", "Flatten on a baking sheet and bake until golden.", "Add toppings and bake again until cheese melts."), 11.0, "https://www.themealdb.com/images/media/meals/x0lkpx1587239132.jpg", "Dinner"));

        recipes.add(new Recipe("70", "Turkey Lettuce Wraps", "American", "Low Calorie", "Savory",
                Arrays.asList(new Ingredient("ground turkey", "200g", false), new Ingredient("lettuce leaves", "4 large", false), new Ingredient("water chestnuts", "1/4 cup", false), new Ingredient("hoisin sauce", "1 tbsp", false)),
                240, 15, Arrays.asList("Brown the ground turkey in a pan over medium heat.", "Stir in chopped water chestnuts and hoisin sauce.", "Cook for 5 minutes until flavors combine.", "Spoon the turkey mixture into large lettuce leaves.", "Top with green onions and serve as hand-held wraps."), 9.0, "https://www.themealdb.com/images/media/meals/pk8wtn1763758591.jpg", "Lunch"));

        recipes.add(new Recipe("71", "Berry Spinach Salad", "American", "Vegan", "Sweet",
                Arrays.asList(new Ingredient("fresh spinach", "2 cups", false), new Ingredient("strawberries", "1/2 cup", false), new Ingredient("blueberries", "1/4 cup", false), new Ingredient("walnuts", "2 tbsp", true)),
                180, 10, Arrays.asList("Wash and dry spinach leaves thoroughly.", "Slice strawberries and combine with blueberries in a bowl.", "Toss spinach with berries and toasted walnuts.", "Drizzle with a light balsamic vinaigrette.", "Serve immediately as a refreshing lunch."), 6.0, "https://www.themealdb.com/images/media/meals/fqpqml1764359125.jpg", "Lunch"));

        recipes.add(new Recipe("72", "Beef and Cabbage Stir Fry", "Chinese", "Keto", "Savory",
                Arrays.asList(new Ingredient("ground beef", "200g", false), new Ingredient("shredded cabbage", "2 cups", false), new Ingredient("garlic", "2 cloves", false), new Ingredient("ginger", "1 tsp", false)),
                450, 15, Arrays.asList("Brown the ground beef in a large skillet.", "Add minced garlic and ginger, sautéing until fragrant.", "Stir in the shredded cabbage and cook until wilted.", "Season with soy sauce or coconut aminos.", "Serve hot, garnished with sesame seeds."), 12.0, "https://www.themealdb.com/images/media/meals/z0ageb1583189517.jpg", "Dinner"));

        recipes.add(new Recipe("73", "Chia Seed Pudding", "American", "Vegan", "Sweet",
                Arrays.asList(new Ingredient("chia seeds", "3 tbsp", false), new Ingredient("almond milk", "1 cup", false), new Ingredient("vanilla extract", "1/2 tsp", false), new Ingredient("maple syrup", "1 tsp", false)),
                220, 120, Arrays.asList("Whisk chia seeds, almond milk, and vanilla in a jar.", "Let sit for 10 minutes then whisk again to prevent clumps.", "Cover and refrigerate for at least 2 hours or overnight.", "The seeds will swell and create a thick pudding texture.", "Top with fresh fruit or nuts before serving."), 5.0, "https://www.themealdb.com/images/media/meals/uvuyxu1503067369.jpg", "Dinner"));

        recipes.add(new Recipe("74", "Grilled Shrimp Skewers", "American", "High Protein", "Savory",
                Arrays.asList(new Ingredient("shrimp", "200g", false), new Ingredient("lemon juice", "2 tbsp", false), new Ingredient("garlic", "2 cloves", false), new Ingredient("parsley", "1 tbsp", false)),
                210, 15, Arrays.asList("Marinate shrimp in lemon juice, minced garlic, and salt.", "Thread shrimp onto wooden or metal skewers.", "Grill over medium-high heat for 2-3 minutes per side.", "Shrimp should be pink and opaque when done.", "Sprinkle with fresh parsley and serve hot."), 14.0, "https://www.themealdb.com/images/media/meals/1529442454.jpg", "Dinner"));

        recipes.add(new Recipe("75", "Eggplant Parmesan", "Italian", "Veg", "Savory",
                Arrays.asList(new Ingredient("eggplant", "1 large", false), new Ingredient("marinara sauce", "1 cup", false), new Ingredient("parmesan", "1/4 cup", true), new Ingredient("mozzarella", "1/2 cup", true)),
                320, 40, Arrays.asList("Slice eggplant into rounds and salt to remove moisture.", "Bake eggplant slices until tender.", "Layer eggplant, sauce, and cheeses in a baking dish.", "Bake at 375°F until the cheese is bubbly and golden.", "Let rest for 5 minutes before serving."), 10.0, "https://www.themealdb.com/images/media/meals/vuyvrt1468710501.jpg", "Breakfast"));

        recipes.add(new Recipe("76", "Tempeh Tacos", "Mexican", "Vegan", "Spicy",
                Arrays.asList(new Ingredient("tempeh", "150g", false), new Ingredient("taco shells", "3", true), new Ingredient("cabbage slaw", "1 cup", false), new Ingredient("avocado", "1/2", false)),
                380, 20, Arrays.asList("Crumble tempeh and sauté with taco spices and a little water.", "Warm the taco shells in the oven.", "Fill shells with the seasoned tempeh.", "Top with fresh cabbage slaw and sliced avocado.", "Serve with a squeeze of lime juice."), 8.0, "https://www.themealdb.com/images/media/meals/6g3rso1763486069.jpg", "Lunch"));

        recipes.add(new Recipe("77", "Avocado Egg Salad", "American", "Keto", "Savory",
                Arrays.asList(new Ingredient("hard boiled eggs", "3", false), new Ingredient("avocado", "1 ripe", false), new Ingredient("lemon juice", "1 tsp", false), new Ingredient("dill", "1 tsp", false)),
                350, 10, Arrays.asList("Mash the avocado in a bowl with lemon juice.", "Chop the hard-boiled eggs into small pieces.", "Fold the eggs into the mashed avocado.", "Stir in fresh dill, salt, and pepper.", "Serve on lettuce wraps or as is."), 5.0, "https://www.themealdb.com/images/media/meals/1529446137.jpg", "Breakfast"));

        recipes.add(new Recipe("78", "Black Bean Burger", "American", "Vegan", "Savory",
                Arrays.asList(new Ingredient("black beans", "1 can", false), new Ingredient("breadcrumbs", "1/2 cup", true), new Ingredient("onion", "1/4 cup", false), new Ingredient("corn", "1/4 cup", false)),
                320, 25, Arrays.asList("Mash black beans in a large bowl, leaving some texture.", "Stir in breadcrumbs, diced onion, and corn.", "Form into 4 patties of even thickness.", "Grill or pan-fry for 5 minutes per side.", "Serve on a bun or over a salad."), 6.0, "https://www.themealdb.com/images/media/meals/z458v91763817681.jpg", "Lunch"));

        recipes.add(new Recipe("79", "Lemon Herb Roasted Chicken", "American", "High Protein", "Savory",
                Arrays.asList(new Ingredient("chicken thighs", "2", false), new Ingredient("lemon", "1", false), new Ingredient("rosemary", "1 sprig", false), new Ingredient("thyme", "1 sprig", false)),
                480, 50, Arrays.asList("Preheat oven to 400°F (200°C).", "Place chicken in a roasting pan with lemon slices.", "Tuck rosemary and thyme around the chicken.", "Roast for 45-50 minutes until skin is crispy.", "Let rest before serving to retain juices."), 12.0, "https://www.themealdb.com/images/media/meals/1529444107.jpg", "Dinner"));

        recipes.add(new Recipe("80", "Spaghetti Squash Marinara", "Italian", "Vegan", "Savory",
                Arrays.asList(new Ingredient("spaghetti squash", "1", false), new Ingredient("marinara sauce", "1 cup", false), new Ingredient("garlic", "1 clove", false), new Ingredient("basil", "1 tbsp", false)),
                180, 45, Arrays.asList("Cut squash in half and roast face down until tender.", "Use a fork to scrape out the squash strands.", "Heat marinara sauce with minced garlic in a pan.", "Toss the squash 'noodles' with the sauce.", "Top with fresh basil and serve warm."), 7.0, "https://www.themealdb.com/images/media/meals/1525873040.jpg", "Dinner"));

        recipes.add(new Recipe("81", "Mediterranean Bowl", "American", "Veg", "Savory",
                Arrays.asList(new Ingredient("hummus", "1/4 cup", false), new Ingredient("falafel", "3", false), new Ingredient("cucumber", "1/2", false), new Ingredient("kalamata olives", "5", false)),
                420, 15, Arrays.asList("Start with a base of mixed greens or rice.", "Add a large scoop of hummus in the center.", "Arrange falafel, sliced cucumber, and olives around it.", "Top with a sprinkle of feta cheese if desired.", "Drizzle with a simple lemon and olive oil dressing."), 9.0, "https://www.themealdb.com/images/media/meals/zry07j1763779321.jpg", "Lunch"));

        recipes.add(new Recipe("82", "Tuna Salad Lettuce Boats", "American", "Keto", "Savory",
                Arrays.asList(new Ingredient("canned tuna", "1 can", false), new Ingredient("mayonnaise", "2 tbsp", true), new Ingredient("celery", "1 stalk", false), new Ingredient("romaine lettuce", "4 leaves", false)),
                310, 10, Arrays.asList("Drain the tuna and place in a small bowl.", "Mix with mayonnaise and finely chopped celery.", "Season with salt and plenty of black pepper.", "Spoon the tuna mixture into crisp romaine leaves.", "Serve cold as a light and healthy snack."), 4.0, "https://www.themealdb.com/images/media/meals/7n8su21699013057.jpg", "Lunch"));

        recipes.add(new Recipe("83", "Roasted Vegetables", "American", "Vegan", "Savory",
                Arrays.asList(new Ingredient("broccoli", "1 head", false), new Ingredient("carrots", "2", false), new Ingredient("bell peppers", "2", false), new Ingredient("olive oil", "2 tbsp", false)),
                180, 25, Arrays.asList("Cut all vegetables into uniform bite-sized pieces.", "Toss in a bowl with olive oil, salt, and pepper.", "Spread on a large baking sheet in a single layer.", "Roast at 425°F for 20-25 minutes.", "Vegetables should be tender and lightly charred."), 5.0, "https://www.themealdb.com/images/media/meals/tvtxpq1511464705.jpg", "Dinner"));

        recipes.add(new Recipe("84", "Almond Flour Pancakes", "American", "Keto", "Sweet",
                Arrays.asList(new Ingredient("almond flour", "1 cup", false), new Ingredient("eggs", "2", false), new Ingredient("almond milk", "1/4 cup", false), new Ingredient("baking powder", "1/2 tsp", false)),
                380, 15, Arrays.asList("Whisk together almond flour, eggs, and milk.", "The batter should be thick but pourable.", "Cook small portions on a greased griddle over medium heat.", "Flip when bubbles appear on the surface.", "Serve with sugar-free syrup or fresh berries."), 11.0, "https://www.themealdb.com/images/media/meals/rwuyqx1511383174.jpg", "Breakfast"));

        recipes.add(new Recipe("85", "Seared Scallops", "American", "High Protein", "Savory",
                Arrays.asList(new Ingredient("scallops", "200g", false), new Ingredient("butter", "1 tbsp", true), new Ingredient("garlic", "1 clove", false), new Ingredient("lemon", "1/2", false)),
                240, 10, Arrays.asList("Pat scallops completely dry with paper towels.", "Season with salt and pepper.", "Sear in a very hot pan with butter for 2 minutes per side.", "Scallops should have a golden-brown crust.", "Finish with a squeeze of lemon juice and serve immediately."), 18.0, "https://www.themealdb.com/images/media/meals/1529442454.jpg", "Dinner"));

        recipes.add(new Recipe("86", "Buddha Bowl", "American", "Vegan", "Savory",
                Arrays.asList(new Ingredient("sweet potato", "1 roasted", false), new Ingredient("chickpeas", "1/2 cup", false), new Ingredient("kale", "1 cup", false), new Ingredient("tahini", "2 tbsp", false)),
                450, 30, Arrays.asList("Roast sweet potato cubes until tender.", "Combine with massaged kale and cooked chickpeas.", "Arrange neatly in a wide bowl.", "Add any other fresh veggies you have.", "Drizzle with a creamy tahini-lemon dressing."), 8.0, "https://www.themealdb.com/images/media/meals/k29viq1585565980.jpg", "Lunch"));

        recipes.add(new Recipe("87", "Pesto Zoodles", "Italian", "Keto", "Savory",
                Arrays.asList(new Ingredient("zucchini", "2", false), new Ingredient("basil pesto", "3 tbsp", true), new Ingredient("cherry tomatoes", "1/2 cup", false), new Ingredient("pine nuts", "1 tbsp", false)),
                290, 10, Arrays.asList("Spiralize zucchini into long noodles.", "Sauté zoodles in a pan for only 2-3 minutes.", "Remove from heat and toss with pesto sauce.", "Top with halved cherry tomatoes and pine nuts.", "Serve immediately before the zoodles release water."), 9.0, "https://www.themealdb.com/images/media/meals/minfsc1763766806.jpg", "Dinner"));

        recipes.add(new Recipe("88", "Hummus and Veggies", "American", "Vegan", "Mild",
                Arrays.asList(new Ingredient("hummus", "1/2 cup", false), new Ingredient("carrots", "2", false), new Ingredient("cucumber", "1/2", false), new Ingredient("bell peppers", "1", false)),
                200, 10, Arrays.asList("Slice all vegetables into long, even sticks.", "Arrange the veggie sticks on a platter.", "Place the hummus in a small bowl in the center.", "Optionally sprinkle hummus with paprika and olive oil.", "Perfect as a healthy snack or appetizer."), 4.0, "https://upload.wikimedia.org/wikipedia/commons/3/3b/Hummus_Veggies.jpg", "Breakfast"));

        recipes.add(new Recipe("89", "Smoked Salmon Cucumber Bites", "American", "High Protein", "Savory",
                Arrays.asList(new Ingredient("smoked salmon", "100g", false), new Ingredient("cucumber", "1", false), new Ingredient("cream cheese", "2 tbsp", true), new Ingredient("dill", "1 tsp", false)),
                180, 15, Arrays.asList("Slice cucumber into thick rounds.", "Top each round with a dollop of cream cheese.", "Add a small piece of smoked salmon on top.", "Garnish with a tiny sprig of fresh dill.", "Serve chilled as a high-protein keto snack."), 13.0, "https://www.themealdb.com/images/media/meals/1549542994.jpg", "Snack"));

        recipes.add(new Recipe("90", "Falafel Wrap", "Indian", "Vegan", "Savory",
                Arrays.asList(new Ingredient("falafel", "4", false), new Ingredient("pita bread", "1", true), new Ingredient("tahini sauce", "2 tbsp", false), new Ingredient("tomato", "1/2", false)),
                450, 10, Arrays.asList("Warm the pita bread slightly.", "Smear with a generous amount of tahini sauce.", "Place the falafel in the center and crush slightly.", "Add sliced tomatoes, onions, and pickles.", "Wrap tightly and serve with extra sauce."), 7.0, "https://www.themealdb.com/images/media/meals/7169.jpg", "Lunch"));

        recipes.add(new Recipe("91", "Paneer Tikka", "Indian", "Veg", "Spicy",
                Arrays.asList(new Ingredient("paneer", "200g", false), new Ingredient("yogurt", "1/4 cup", true), new Ingredient("bell peppers", "1", false), new Ingredient("onions", "1", false)),
                350, 30, Arrays.asList("Marinate paneer and veggie cubes in spiced yogurt.", "Thread onto skewers alternating paneer and veggies.", "Grill or bake until the edges are charred.", "Squeeze fresh lemon juice over the hot skewers.", "Serve with mint chutney and onion rings."), 8.0, "https://upload.wikimedia.org/wikipedia/commons/f/f6/Paneer_Tikka.jpg", "Dinner"));

        recipes.add(new Recipe("92", "Shrimp Scampi with Zoodles", "Italian", "Keto", "Savory",
                Arrays.asList(new Ingredient("shrimp", "200g", false), new Ingredient("zucchini", "2", false), new Ingredient("garlic", "3 cloves", false), new Ingredient("butter", "2 tbsp", true)),
                320, 20, Arrays.asList("Spiralize zucchini into noodles and set aside.", "Sauté minced garlic in butter until fragrant.", "Add shrimp and cook until pink (2-3 mins).", "Add zoodles to the pan and toss for 2 minutes.", "Finish with lemon juice and red pepper flakes."), 15.0, "https://www.themealdb.com/images/media/meals/minfsc1763766806.jpg", "Dinner"));

        recipes.add(new Recipe("93", "Vegetable Korma", "Indian", "Vegan", "Savory",
                Arrays.asList(new Ingredient("mixed veggies", "2 cups", false), new Ingredient("coconut milk", "1 cup", false), new Ingredient("cashews", "2 tbsp", false), new Ingredient("onions", "1", false)),
                380, 35, Arrays.asList("Sauté onions and spices in a large pot.", "Add mixed vegetables and stir-fry for 5 minutes.", "Pour in coconut milk and add cashew paste.", "Simmer until vegetables are tender and sauce is thick.", "Garnish with cilantro and serve with rice."), 9.0, "https://www.themealdb.com/images/media/meals/58o7id1593912466.jpg", "Dinner"));

        recipes.add(new Recipe("94", "Egg Salad Sandwich", "American", "Veg", "Savory",
                Arrays.asList(new Ingredient("eggs", "2", false), new Ingredient("whole wheat bread", "2 slices", true), new Ingredient("mayo", "1 tbsp", true), new Ingredient("mustard", "1 tsp", false)),
                400, 15, Arrays.asList("Hard boil eggs and cool in ice water.", "Peel and mash eggs in a bowl.", "Mix with mayonnaise, mustard, salt, and pepper.", "Spread the mixture onto whole wheat bread.", "Add lettuce and serve as a quick lunch."), 5.0, "https://upload.wikimedia.org/wikipedia/commons/7/7b/Egg_Salad_Sandwich.jpg", "Breakfast"));

        recipes.add(new Recipe("95", "Grilled Veggie Burger", "American", "Veg", "Savory",
                Arrays.asList(new Ingredient("veggie patty", "1", false), new Ingredient("burger bun", "1", true), new Ingredient("lettuce", "1 leaf", false), new Ingredient("tomato", "1 slice", false)),
                350, 20, Arrays.asList("Grill the veggie patty on medium heat.", "Toast the burger buns until golden.", "Assemble the burger with lettuce, tomato, and patty.", "Add your favorite condiments like ketchup or mayo.", "Serve hot with a side of sweet potato fries."), 7.0, "https://upload.wikimedia.org/wikipedia/commons/a/a2/Veggie_Burger.jpg", "Breakfast"));

        recipes.add(new Recipe("96", "Chicken Pho", "Vietnamese", "Non-Veg", "Savory",
                Arrays.asList(new Ingredient("chicken broth", "3 cups", false), new Ingredient("rice noodles", "1 portion", true), new Ingredient("shredded chicken", "1 cup", false), new Ingredient("ginger", "1 knob", false)),
                420, 30, Arrays.asList("Simmer chicken broth with charred ginger and onions.", "Cook rice noodles according to package directions.", "Place noodles and shredded chicken in a deep bowl.", "Pour the hot, fragrant broth over the noodles.", "Serve with bean sprouts, basil, lime, and chili."), 12.0, "https://www.themealdb.com/images/media/meals/6f830.jpg", "Dinner"));

        recipes.add(new Recipe("97", "Sushi Platter", "Japanese", "Non-Veg", "Savory",
                Arrays.asList(new Ingredient("sushi rice", "1 cup", false), new Ingredient("raw salmon", "100g", false), new Ingredient("nori", "2 sheets", false), new Ingredient("wasabi", "1 tsp", false)),
                550, 45, Arrays.asList("Prepare vinegared sushi rice and let cool.", "Slice fresh salmon into thin strips.", "Form small mounds of rice and top with salmon.", "Or roll rice and salmon in nori sheets.", "Serve with pickled ginger, soy sauce, and wasabi."), 25.0, "https://www.themealdb.com/images/media/meals/g046bb1663960946.jpg", "Dinner"));

        recipes.add(new Recipe("98", "Ratatouille", "French", "Vegan", "Savory",
                Arrays.asList(new Ingredient("eggplant", "1", false), new Ingredient("zucchini", "1", false), new Ingredient("tomatoes", "2", false), new Ingredient("bell peppers", "1", false)),
                250, 60, Arrays.asList("Slice all vegetables into thin, even rounds.", "Arrange the slices in an overlapping pattern in a dish.", "Pour a seasoned tomato sauce over the vegetables.", "Cover and bake until the vegetables are tender.", "Uncover and bake for another 10 minutes to brown."), 10.0, "https://www.themealdb.com/images/media/meals/vuyvrt1468710501.jpg", "Dinner"));

        recipes.add(new Recipe("99", "Chicken Caesar Wrap", "American", "Non-Veg", "Savory",
                Arrays.asList(new Ingredient("grilled chicken", "1 cup", false), new Ingredient("romaine", "1 cup", false), new Ingredient("tortilla", "1", true), new Ingredient("caesar dressing", "2 tbsp", true)),
                480, 10, Arrays.asList("Toss sliced grilled chicken with romaine and dressing.", "Add a sprinkle of parmesan cheese and croutons.", "Place the mixture in the center of a large tortilla.", "Fold in the sides and roll tightly.", "Cut in half and serve as a quick meal."), 8.0, "https://upload.wikimedia.org/wikipedia/commons/e/e8/Chicken_Caesar_Wrap.jpg", "Lunch"));

        recipes.add(new Recipe("100", "Shepherd's Pie", "British", "Non-Veg", "Savory",
                Arrays.asList(new Ingredient("ground lamb", "250g", false), new Ingredient("mashed potatoes", "2 cups", false), new Ingredient("peas and carrots", "1 cup", false), new Ingredient("onion", "1", false)),
                650, 45, Arrays.asList("Sauté ground lamb with onions and mixed veggies.", "Stir in a little flour and broth to make a gravy.", "Transfer the meat mixture to a baking dish.", "Spread mashed potatoes evenly over the top.", "Bake at 400°F until the potatoes are golden and crusty."), 15.0, "https://www.themealdb.com/images/media/meals/1525873040.jpg", "Dinner"));
"""

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. First, fix the corrupted ingredients globally (same as before, it worked for most)
content = re.sub(r'new Ingredient\("(.*?)",\s*"https?://.*?",\s*"(.*?)",', r'new Ingredient("\1", "\2",', content)

# 2. Replace the 61-100 block entirely to be sure
# Find the start of the 61-100 block
start_marker = "// New Recipes 61-100"
end_marker = "    public List<Recipe> getAllRecipes()"

parts = content.split(start_marker)
if len(parts) == 2:
    suffix = parts[1].split(end_marker)
    if len(suffix) == 2:
        new_content = parts[0] + start_marker + RECIPES_61_100 + "    }\n\n" + end_marker + suffix[1]
        content = new_content

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Restored 61-100 and fixed 1-60 ingredients.")
