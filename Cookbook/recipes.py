from serverCheck import checker
class Recipes():
    """description of class"""
    
    name = ''
    amount = 0
    ing = []
    ingString = ''
    bakeTime = ''
    bakeTemp = ''
    directions = ''
    favorite = 0
    rerun = True

    def add(self):
        print("Welcome to adding a recipe\n\n")
        while(self.rerun):
            self.name = input("What is the name of the recipe\n")
            self.amount = int(input('How many ingredients are there.\n'))
            for x in range(self.amount):
                self.ing.append(input("What is the ingredient and it's amount? (Press enter after each ingredient and qty added)\n") + ' ')
        
            self.decTemp = input('Does it need to bake (yes or no)\n')
            while(self.decTemp.lower() != 'no' and self.decTemp.lower() != 'yes'):
                self.decTemp = input('Incorrect input. \nDoes it need to bake (yes or no)\n')
            if(self.decTemp.lower() == 'yes'):
                self.bakeTime = input('What is the baking time\n')
                self.bakeTemp = int(input('What is the baking temprature (only the number)\n'))
            elif self.decTemp.lower() == 'no':
                pass;
        
            self.directions = input("What are the directions for making the recipe. \nRemember proper spelling and spaceing.\n")

            self.favPick = input('Is this a family favorite (Yes or No)\n')
            while self.favPick.lower != 'yes' and self.favPick.lower != 'no':
                self.favPick = input('Incorrect input. Is this a family favorite (Yes or No)\n')
            if self.favPick == 'yes':
                self.favorite = 1
            elif self.favPick == 'no':
                self.favorite = 0
            else:
                pass
            #checker(self.name)
            for x in self.ing:
                self.ingString += x
            print('Name %s \nIngredients %s \nBake Time %s \nBake Temp %i \n\nDirections %s \nFavorite %s  Fav digit %i' % (self.name, self.ingString, self.bakeTime, self.bakeTemp, self.directions, self.favPick, self.favorite))
            self.rerun = False

    