class Recipes():
    """description of class"""
    name = ""
    ing = []
    bakeTime = ""
    bakeTemp = ""
    directions = ""
    favorite = 0
    rerun = True

    def add(self):
        print("Welcome to adding a recipe")
        while(rerun):
            name = input("What is the name of the recipe")

            amount = ""
            while(isinstance(amount, int)):
                amount = input('How many ingredients are there.')
            for x in amount:
                ing.append(input("What is the ingredient and it's amount"))
        
            decTemp = '';
            while(decTemp.lower() != 'no' and decTemp.lower() != 'yes'):
                decTemp = input('Does it need to bake (yes or no)')
                if(decTemp.lower() == 'yes'):
                    bakeTime = input('What is the baking time')
                    bakeTemp = input('What is the baking temprature (only the number)')
                elif decTemp.lower() == 'no':
                    break;
        
            directions = input("What are the directions for making the recipe.")

            favPick = ''
            while favPick != 'yes' and favPick != 'no':
                favPick = input('Is this a family favorite (Yes or No)')
                if favPick == yes:
                    favorite = 1
                elif favPick == no:
                    favorite = 0
                else:
                    pass
        check()

    def check(self):
        pass
        