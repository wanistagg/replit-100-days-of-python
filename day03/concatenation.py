print("=== The Ultimate Wacky Recipe Maker ===")
print()

print("""Welcome to The Ultimate Wacky Recipe Maker! 
Today, we will be creating a wacky recipe for today's menu. 
You will be asked to enter a few ingredients, and, based on what you choose, we will create a menu tailored especially for you.""")
print()

food = input("Choose a food: ")
plant = input("Choose a plant: ")
cooking = input("Choose a cooking method: ")
burned = input("Choose a word to decribe burned food: ")
item = input("Choose a DIY item: ")
print()

print("--- TODAY'S MENU ---")
print()
print(cooking, food, "with", burned, plant, "on a bed of", item)
