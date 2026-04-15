class food_item:
    """Represent a food item and its nutritional values."""

    def __init__(self, name: str, calories: float, protein: float,
                 carbohydrates: float, fat: float):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.carbohydrates = carbohydrates
        self.fat = fat



def track_nutrition(consumed_items: list[food_item]) -> dict:
    
    total_calories = 0.0
    total_protein = 0.0
    total_carbohydrates = 0.0
    total_fat = 0.0

    for item in consumed_items:
        total_calories += item.calories
        total_protein += item.protein
        total_carbohydrates += item.carbohydrates
        total_fat += item.fat

    print("24-hour nutrition summary")
    print(f"Total calories: {total_calories:.1f}")
    print(f"Total protein: {total_protein:.1f} g")
    print(f"Total carbohydrates: {total_carbohydrates:.1f} g")
    print(f"Total fat: {total_fat:.1f} g")

    if total_calories > 2500:
        print("Warning: calorie intake is above 2500 calories.")
    if total_fat > 90:
        print("Warning: fat intake is above 90 g.")

    return {
        "calories": total_calories,
        "protein": total_protein,
        "carbohydrates": total_carbohydrates,
        "fat": total_fat,
    }


# Example class usage and function call
if __name__ == "__main__":
    breakfast = food_item("Apple", 60, 0.3, 15, 0.5)
    lunch = food_item("Chicken sandwich", 450, 30, 40, 12)
    dinner = food_item("Pasta", 700, 20, 110, 18)
    snack = food_item("Chocolate bar", 250, 3, 30, 14)

    foods_eaten = [breakfast, lunch, dinner, snack]
    track_nutrition(foods_eaten)
