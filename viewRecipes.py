from dbConnection import Lookup
import os
import json
class ViewRecipes():
    """description of class"""



    def viewAll(self):
        recipeHolder = {}
        for file in os.listdir("../Cookbook"):
            if(file.endswith(".json")):
                with open(file, "r") as jsonRecipe:
                    f = json.load(jsonRecipe)
                    if(len(recipeHolder) == 0):
                        recipeHolder = f.copy()

                    else:
                        recipeHolder.update(f)
                    jsonRecipe.close()
        for reName, reInfo in recipeHolder.items():
            print("\nRecipe Name:", reName)
            
            for key in reInfo:
                print(key + ':', reInfo[key])
        

    def viewSelect(self):

        typeInput = 0
        recipeType = ''
        recipeHolder = {}
        while(typeInput <= 0 or typeInput > 7):
            try:
                typeInput = int(input('What type of recipe are you looking for?\n(1) for Breakfast \n(2) for Main Dish \n(3) for Side Dish \n(4) for Soup \n(5) for Bread \n(6) for Dessert \n(7) for Drink \n'))
            except: 
                typeInput = 0
            if typeInput == 1:
                recipeType = 'Breakfast.json'
            elif typeInput == 2:
                recipeType = 'Main_Dish.json'
            elif typeInput == 3:
                recipeType = 'Side_Dish.json'
            elif typeInput == 4:
                recipeType = 'Soup.json'
            elif typeInput == 5:
                recipeType = 'Bread.json'
            elif typeInput == 6:
                recipeType = 'Dessert.json'
            elif typeInput == 7:
                recipeType = 'Drink.json'
            else:
                print('Incorrect input')

        for file in os.listdir("../Cookbook"):
            if(file == recipeType):
                with open(file, "r") as jsonRecipe:
                    f = json.load(jsonRecipe)
                    recipeHolder = f.copy()
                    jsonRecipe.close()
        
        if(len(recipeHolder) == 0):
            print("There are currently no recipes for this type.")
        for reName, reInfo in recipeHolder.items():
            print("\nRecipe Name:", reName)
            
            for key in reInfo:
                print(key + ':', reInfo[key])
    




    def printLoop(self, tupHold):
        for tup in tupHold:
            for st, var in enumerate(tup):
                if st == 0:
                    print('Name: %s' % (var))
                elif st == 1:
                    if(var == None or var == ''):
                        pass
                    else:
                        print('Type: %s' % (var))
                elif st == 2:
                    print('Ingredients: %s' % (var))
                elif st == 3:
                    if(var == None or var == ''):
                        pass
                    else:
                        print('Bake Time: %s' % (var))
                elif st == 4:
                    if(var == None or var == ''):
                        pass
                    else:
                        print('Bake Temp: %i' % (var))
                elif st == 5:
                    print('Directions: %s' % (var))

                elif st == len(tup) - 1:
                    if(var == 0):
                        print('Favorite: No')
                    else:
                        print('Favorite: Yes')
                    print()
                else:
                    print('ERROR')

