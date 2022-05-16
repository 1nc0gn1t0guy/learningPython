name = "Zed A. Shaw."
age = 35 # not a lie
height = 74 # inches
height_m = round(height * 0.0254)
weight = 180 # lbs
weight_kg = round(weight * 0.453592)
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}")
print(f"He's {height_m} metres tall.")
print(f"He's {weight_kg} kg heavy.")
print("Acutally that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")