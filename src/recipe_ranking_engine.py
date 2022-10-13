import json
from .constants import *


if __name__ == "__main__":
    f = open('recipe_book_1.json')
    recipes = json.load(f)

    print("Enter comma separated list of ingredients")
    myIngredients = map(lambda s: s.lower, input().split(", "))

    print(myIngredients)
    

    result = []
    for recipe in recipes:
        recipeScore = 0
        totalCost = 0

        listOfLists = [ingredient['options'] for ingredient in recipe['ingredients']]
        recipeIngredients = [item for sublist in listOfLists for item in sublist]

        for myIngredient in myIngredients:
            if myIngredient in recipeIngredients:
                # 1 point for every ingredient in the recipe
                recipeScore += 1
            for recipeIngredient in recipe['ingredients']:
                if myIngredient not in recipeIngredient['options']:
                    totalCost += recipeIngredient['cost']
        # result.append(RankedRecipe(recipe['name'], recipeScore, totalCost))

    sortedResult = sorted(result, key=lambda d: str(d[TOTAL_COST]))

    # print(type(result['PBJ']['totalCost']))
    for recipe in sortedResult:
        jsonthing = json.dumps(recipe, indent=4)
        print(jsonthing)
        # for key in recipe:
        #     print('  ')
        #     print(result)

    f.close()
