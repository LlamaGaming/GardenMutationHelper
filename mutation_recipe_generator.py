def normalize(name):
    return name.strip().lower()

recipes = {
    "Timestalk": {"Stoplight Petal":4, "Chorus Fruit":2, "Shellfruit":2},
    "Phantomleaf": {"Chorus Fruit":4, "Shellfruit":4},
    "All-in Aloe": {"Magic Jellybean":6, "PlantBoy Advance":2},
    "Devourer": {"Puffercloud":4, "Zombud":4},
    "Glasscorn": {"Startlevine":4, "Chloronite":4},

    "Stoplight Petal": {"Snoozling":4, "Noctilume":4},
    "Chorus Fruit": {"Chloronite":5, "Magic Jellybean":3},
    "Shellfruit": {"Turtillini":6, "Blastberry":2},
    "PlantBoy Advance": {"Snoozling":6, "Thunderling":6},
    "Puffercloud": {"Snoozling":2, "Do-not-eat-shroom":6},
    "Zombud": {"Dead Plants":4, "Cindershade":2, "Fleshtrap":2},
    "Startlevine": {"Blastberry":4, "Cheesebite":4},
    "Turtillini": {"Soggybud":4, "Choconut":4},
    "Thunderling": {"Soggybud":5, "Noctilume":3},

    "Magic Jellybean": {"Sugarcane":5, "Duskbloom":3},
    "Chloronite": {"Coalroot":6, "Thornshade":2},
    "Snoozling": {"Creambloom": 4, "Dustgrain":3, "Witherbloom":3, "Duskbloom":3, "Thornshade":3},
    "Noctilume": {"Duskbloom":6, "Lonelily":6},
    "Blastberry": {"Chocoberry":5, "Ashwreath":3},
    "Do-not-eat-shroom": {"Veilshroom":4, "Scourroot":4},
    "Fleshtrap": {"Cindershade":4, "Lonelily":4},
    "Cheesebite": {"Creambloom":4, "Fermento":4},
    "Soggybud": {"Melon Seeds":2, "Gloomgourd":2},

    "Cindershade": {"Ashwreath":4, "Witherbloom":4},
    "Duskbloom": {"Moonflower":2, "Shadevine":2, "Sunflower":2, "Dustgrain":2},
    "Thornshade": {"Scourroot":3, "Ashwreath":5},
    "Creambloom": {"Choconut":8},
    "Chocoberry": {"Choconut":6, "Gloomgourd":2},
    "Coalroot": {"Ashwreath":5, "Scourroot":3},

    "Choconut": {"Cocoa Beans":2},
    "Dustgrain": {"Wheat Seeds":2},
    "Witherbloom": {"Dead Plants":4},
    "Ashwreath": {"Fire":2, "Nether Wart":2},
    "Veilshroom": {"Red Mushroom":1, "Brown Mushroom":1},
    "Scourroot": {"Potato":1, "Carrot":1},
    "Gloomgourd": {"Pumpkin Seeds":1, "Melon Seeds":1},
    "Shadevine": {"Cactus":1, "Sugarcane":1},
}

def normalize(name):
    return name.strip().lower()

recipes = {normalize(k): {normalize(i): v for i, v in val.items()}
           for k, val in recipes.items()}

def get_cost(item, amount, recipes, result):
    if item not in recipes:
        result[item] = result.get(item, 0) + amount
        return

    for ingredient, qty in recipes[item].items():
        get_cost(ingredient, amount * qty, recipes, result)

def print_tree(item, amount, recipes, prefix="", is_last=True):
    connector = "└── " if is_last else "├── "
    print(prefix + connector + f"{item.title()} x{amount}")

    if item not in recipes:
        return

    ingredients = list(recipes[item].items())

    for i, (ingredient, qty) in enumerate(ingredients):
        last = i == len(ingredients) - 1

        # Extend prefix:
        # If current node is last → no vertical line
        # Otherwise → keep vertical line
        new_prefix = prefix + ("    " if is_last else "│   ")

        print_tree(ingredient, amount * qty, recipes, new_prefix, last)

user_input = input("Enter item(s) separated by commas: ")
items = [normalize(x) for x in user_input.split(",") if x.strip()]

result = {}

for item in items:
    print(f"\n=== Recipe Tree for {item.title()} ===\n")
    get_cost(item, 1, recipes, result)
    print_tree(item, 1, recipes)

print("\nRaw materials (combined):")
for k, v in result.items():
    print(f"{k}: {v}")
