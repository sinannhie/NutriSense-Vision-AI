import pandas as pd

nutrition_db = pd.read_csv("data/nutrition.csv")


def calculate_nutrition(detected_items):

    total = {
        "calories": 0,
        "protein": 0,
        "carbs": 0,
        "fat": 0
    }

    for item in detected_items:

        food = item["name"].lower()

        result = nutrition_db[
            nutrition_db["food_name"] == food
        ]

        if result.empty:
            continue

        row = result.iloc[0]

        total["calories"] += row["calories"]
        total["protein"] += row["protein"]
        total["carbs"] += row["carbs"]
        total["fat"] += row["fat"]

    return total