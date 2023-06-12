import requests
from bs4 import BeautifulSoup
# this url is invalid and code woulld return "food list not found"
def scrape_calorie_counter():
    url = "https://www.webmd.com/diet/healthtool-food-calorie-counter"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    food_list = soup.find_all("div", class_="tool-food-list")
    if len(food_list) == 0:
        print("Food list not found")
        return []

    food_items = food_list[0].find_all("li")
    if len(food_items) == 0:
        print("No food items found")
        return []

    calorie_data = []
    for food_item in food_items:
        food_name = food_item.find("a").text.strip()
        calories = food_item.find("span").text.strip()
        calorie_data.append({"food": food_name, "calories": calories})

    return calorie_data

# Example usage:
calorie_counter_data = scrape_calorie_counter()
if calorie_counter_data:
    for item in calorie_counter_data:
        print(f"Food: {item['food']}")
        print(f"Calories: {item['calories']}")
        print("---")
