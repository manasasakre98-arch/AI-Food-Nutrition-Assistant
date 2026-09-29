NUTRITION_DATA = {
    "FriedChicken": {
        "serving": "1 piece (~130 g)",
        "calories": 320,
        "protein": 24,
        "carbs": 10,
        "fat": 20,
        "source": "Rice & Protein - Gai Tod",
    },

    "GaengKeawWan": {
        "serving": "1 cup (~235 g)",
        "calories": 330,
        "protein": 24,
        "carbs": 17,
        "fat": 20,
        "source": "MyFoodDiary - Thai Green Curry",
    },

    "KaoManGai": {
        "serving": "1 plate (~300 g)",
        "calories": 596,
        "protein": 28,
        "carbs": 70,
        "fat": 22,
        "source": "Rice & Protein - Khao Man Gai",
    },

    "KhaoNiewMaMuang": {
        "serving": "1 serving (~307 g)",
        "calories": 390,
        "protein": 7,
        "carbs": 68,
        "fat": 11,
        "source": "Arise - Mango Sticky Rice",
    },

    "KuayTeowReua": {
        "serving": "1 serving (~595 g)",
        "calories": 612,
        "protein": 34,
        "carbs": 58,
        "fat": 27,
        "source": "Arise - Thai Boat Noodles",
    },

    "PadThai": {
        "serving": "1 cup (~200 g)",
        "calories": 308,
        "protein": 16.3,
        "carbs": 29,
        "fat": 15,
        "source": "USDA FoodData Central reference",
    },

    "PhatKaphrao": {
        "serving": "1 serving",
        "calories": 531,
        "protein": 33.6,
        "carbs": 62.9,
        "fat": 16.2,
        "source": "The Kitchn - Pad Krapow",
    },

    "Somtam": {
        "serving": "1 plate (~150 g)",
        "calories": 150,
        "protein": 4,
        "carbs": 22,
        "fat": 5,
        "source": "Rice & Protein - Som Tam",
    },

    "StewedPorkLeg": {
        "serving": "1 plate (~350 g)",
        "calories": 690,
        "protein": 28,
        "carbs": 78,
        "fat": 30,
        "source": "Rice & Protein - Khao Kha Moo",
    },

    "TomYumGoong": {
        "serving": "1.5 cups",
        "calories": 152,
        "protein": 24,
        "carbs": 4,
        "fat": 4,
        "source": "University of Hawaiʻi Nutrition Center",
    },
}


def get_nutrition(food_name):
    return NUTRITION_DATA.get(food_name)


if __name__ == "__main__":
    print(get_nutrition("PadThai"))
 