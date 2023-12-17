class FoodRating:
    def __init__(self, food, rating, cuisine):
        self.food = food
        self.rating = rating
        self.cuisine = cuisine
        self.deleted = False

    def __gt__(self, other):
        if self.rating == other.rating:
            return self.food > other.food
        return self.rating > other.rating

    def __eq__(self, other):
        return self.rating == other.rating and self.food == other.food

    def __lt__(self, other):
        if self.rating == other.rating:
            return self.food < other.food
        return self.rating < other.rating


class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        n = len(foods)
        self.foods = {}
        self.cuisines = {}

        for i in range(n):
            rating = -ratings[i]
            cuisine = cuisines[i]
            food = FoodRating(foods[i], rating, cuisine)

            self.foods[food.food] = food

            if cuisine not in self.cuisines:
                self.cuisines[cuisine] = []

            self.cuisines[cuisine].append(food)

        for cuisine in self.cuisines.keys():
            heapq.heapify(self.cuisines[cuisine])

    def changeRating(self, food: str, newRating: int) -> None:
        foodObject = self.foods[food]
        foodObject.deleted = True
        cuisine = foodObject.cuisine

        newFoodObject = FoodRating(food, -newRating, cuisine)
        self.foods[food] = newFoodObject
        heapq.heappush(self.cuisines[cuisine], newFoodObject)

        while self.cuisines[cuisine][0].deleted:
            heapq.heappop(self.cuisines[cuisine])

    def highestRated(self, cuisine: str) -> str:
        return self.cuisines[cuisine][0].food

# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
