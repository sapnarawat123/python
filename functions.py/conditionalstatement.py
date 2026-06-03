# Check if you have enough tomatoes for the full party
if pantry_stock["tomatoes"] >= ingredients_needed["tomatoes"]:
    print("Enough tomatoes for the party!")

# Check if you have enough for a smaller gathering
elif pantry_stock["tomatoes"] >= 800:
    print("Only enough tomatoes for a smaller gathering.")
    
# Handle the case where you need to buy more
else:
    print("Need to buy tomatoes before the party.")


#example 
# Check if you have exactly the right amount of basil
if basil_grams == required_basil:
    print('Perfect! You have exactly the right amount of basil.')
else:
    print('You need to adjust your basil quantity.') 