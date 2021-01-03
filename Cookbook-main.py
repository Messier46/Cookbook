# Main Class
import os
import json
from recipes import Recipes
from viewRecipes import ViewRecipes

contRun = True

if os.path.isfile("Breakfast.json"):
    pass
else:
    with open("Breakfast.json", "w") as outfile:
        newFile = {}
        json.dump(newFile, outfile)
        outfile.close()

    with open("Main_Dish.json", "w") as outfile:
        newFile = {}
        json.dump(newFile, outfile)
        outfile.close()

    with open("Side_Dish.json", "w") as outfile:
        newFile = {}
        json.dump(newFile, outfile)
        outfile.close()

    with open("Soup.json", "w") as outfile:
        newFile = {}
        json.dump(newFile, outfile)
        outfile.close()

    with open("Bread.json", "w") as outfile:
        newFile = {}
        json.dump(newFile, outfile)
        outfile.close()

    with open("Dessert.json", "w") as outfile:
        newFile = {}
        json.dump(newFile, outfile)
        outfile.close()

    with open("Drink.json", "w") as outfile:
        newFile = {}
        json.dump(newFile, outfile)
        outfile.close()


# Used to ask if they want to continue
def reRun():
    hold = input('\nWould you like to look up or add another recipe? (yes or no)\n')
    if hold.lower() == 'no':
        contCheck = False
    else:
        contCheck = True
    return contCheck


# Loop to keep asking what they would like to do
while (contRun):
    print('Welcome to the recipe adder, updater and viewer. What would you like to do today?')
    # Select between different options via a number
    selection = input('Please enter a number. \n(1)Add a recipe \n(2)View all recipes \n(3)View a select recipe'
                      ' \n(4)To update a recipe \n(5)To delete a recipe \n(6)Quit\n')

    # Runs the add method and adds the new recipe to the database
    if selection == "1":
        x = Recipes()
        x.add()
        contRun = reRun()

    # Displays all recipes in the database
    elif selection == "2":
        y = ViewRecipes()
        y.viewAll()
        contRun = reRun()

    # Displays a recipes based on the type of recipe the user picks
    elif selection == "3":
        y = ViewRecipes()
        y.viewSelect()
        contRun = reRun()

    # Update a recipe
    elif selection == "4":
        u = Recipes()
        u.update()
        contRun = reRun()

    # Delete a recipe
    elif selection == "5":
        d = Recipes()
        d.delete()
        contRun = reRun()

    # Ends the program
    elif selection == "6":
        contRun = False

    else:
        print("Incorrect input.")
