# Create the recipe dictionary
recipe = {"olive_oil": 30, 
# Add garlic
          "garlic": 15,
# Add tomatoes
          "tomatoes": 400}

print(recipe)

# Add 'basil' as a new key to the recipe dictionary with a value of 20.
# Create the recipe dictionary
recipe = {"olive_oil": 30,
# Add garlic
          "garlic": 15,
# Add tomatoes
          "tomatoes": 400}

# Add basil to the recipe dictionary
recipe["basil"] = 20

print(recipe)

# Use a method to retrieve all the keys from the recipe dictionary and assign the result to ingredient_names.
# Use a method to retrieve all the values from the recipe dictionary and assign the result to quantities.
# Use a method to retrieve all key-value pairs from the recipe dictionary and assign the result to recipe_items.
# Get all ingredient names
ingredient_names = recipe.keys()

# Get all quantities
quantities = recipe.values()

# Get all key-value pairs
recipe_items =recipe.items()

print("Ingredient names:", ingredient_names)
print("Quantities:", quantities)
print("Recipe items:", recipe_items)