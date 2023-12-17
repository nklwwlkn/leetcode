from sortedcontainers import SortedSet

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.foodToRating = dict()
        self.foodToCuisine = dict()
        self.cuisineToRating = defaultdict(SortedSet)

        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.foodToRating[food] = rating
            self.foodToCuisine[food] = cuisine
            self.cuisineToRating[cuisine].add((-rating, food))

    def changeRating(self, food: str, newRating: int) -> None:
        rating = self.foodToRating[food]
        cuisine = self.foodToCuisine[food]

        self.cuisineToRating[cuisine].remove((-rating, food))

        self.cuisineToRating[cuisine].add((-newRating, food))
        self.foodToRating[food] = newRating
        

    def highestRated(self, cuisine: str) -> str:
        return self.cuisineToRating[cuisine][0][1]
        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)