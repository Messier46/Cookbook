import json
#from serverCheck import checker
#from dbConnection import Lookup
class Recipes():
    """This class currently holds the adding a recipe method"""
    
    name = ''
    recipeType = ''
    amount = 0
    ing = []
    ingString = ''
    bakeTime = ''
    bakeTemp = 0
    directions = ''
    favorite = 0
    rerun = True
    process = 'add'
    idHold = 0
    tempFConvert = ''

    def add(self):
        if(self.process == 'update'):
            print('Welcome to updating a recipe\n')
        else:
            print("Welcome to adding a recipe\n")

        while(self.rerun):
            self.name = input("What is the name of the recipe\n")

            typeInput = 0
            while(typeInput <= 0 or typeInput > 7):
                try:
                    typeInput = int(input('What type of recipe is it? \n(1) for Breakfast \n(2) for Main Dish \n(3) for Side Dish \n(4) for Soup \n(5) for Bread \n(6) for Dessert \n(7) for Drink \n'))
                except: 
                    typeInput = 0
                if typeInput == 1:
                    self.recipeType = 'Breakfast.json'
                elif typeInput == 2:
                    self.recipeType = 'Main_Dish.json'
                elif typeInput == 3:
                    self.recipeType = 'Side_Dish.json'
                elif typeInput == 4:
                    self.recipeType = 'Soup.json'
                elif typeInput == 5:
                    self.recipeType = 'Bread.json'
                elif typeInput == 6:
                    self.recipeType = 'Dessert.json'
                elif typeInput == 7:
                    self.recipeType = 'Drink.json'
                else:
                    print('Incorrect input')





            while(self.amount <= 0):
                #Need to add exception handling expecially here
                try:
                    self.amount = int(input('How many ingredients are there.\n'))
                except:
                    print('No input/incorrect input')
                    self.amount = 0
            for x in range(self.amount):
                singleIng = ''
                singleIng = input("What is the ingredient and it's amount? (Press enter after each ingredient and qty added)\n")
                while(singleIng == ''):
                    singleIng = input("Blank input. What is the ingredient and it's amount? (Press enter after each ingredient and qty added)\n")
                self.ing.append(singleIng  + ', ')

            #Asks whether the recipe needs to bake or not.
            self.decTemp = input('Does it need to bake (yes or no)\n')
            while(self.decTemp.lower() != 'no' and self.decTemp.lower() != 'yes'):
                self.decTemp = input('Incorrect input. \nDoes it need to bake (yes or no)\n')
            if(self.decTemp.lower() == 'yes'):
                self.bakeTime = input('What is the baking time\n')
                while(self.bakeTime == ''):
                    self.bakeTime = input('Blank input. What is the baking time\n')
                while(self.bakeTemp == 0):
                    try:
                        self.bakeTemp = int(input('What is the baking temprature (only the number)\n'))
                    except:
                        self.bakeTemp = 0
            elif self.decTemp.lower() == 'no':
                pass;
        
            #Ask for the directions clearly all at one in one big string
            self.directions = input("What are the directions for making the recipe. \nRemember proper spelling and spaceing.\n")

            #Ask whether this is a family favorite 
            self.favPick = input('Is this a family favorite (Yes or No)\n')
            while self.favPick.lower() != 'yes' and self.favPick.lower() != 'no':
                self.favPick = input('Incorrect input. Is this a family favorite (Yes or No)\n')
            


            #The one or zero will be sent to the database for a boolean
            if self.favPick == 'yes':
                self.favorite = 1
            elif self.favPick == 'no':
                self.favorite = 0
            else:
                pass



            #checker(self, self.name, self.ingString, self.bakeTime, self.directions)


            #Converts ingredent list into a string
            for x in self.ing:
                self.ingString += x
            #Relists everything the person has typed to be reviewed
            print('\n\nName %s \nType %s \nIngredients %s \nBake Time %s \nBake Temp %i \n\nDirections %s \nFavorite %s' % (self.name, self.recipeType, self.ingString, self.bakeTime, self.bakeTemp, self.directions, self.favPick,))

            clearUp = input('Does this look correct? If yes type in yes to continue, else type no to retype the recipe\n')
            while(clearUp != 'no' and clearUp != 'yes'):
                clearUp = input('Incorrect input. Does this look correct? If yes type in yes to continue, else type no to retype the recipe\n')

            #If yes leaves rerun while loop
            if(clearUp == 'yes'):
                self.rerun = False
            #If no clears the variables to be readded
            elif(clearUp == 'no'):
                self.rerun = True
                self.name = ''
                self.recipeType = ''
                self.amount = 0
                self.ing = []
                self.ingString = ''
                self.bakeTime = ''
                self.bakeTemp = 0
                self.directions = ''
                self.favorite = 0





        if(self.process == 'add'):
            jsonFile = open(self.recipeType, "r")
            convertFile = json.load(jsonFile)
            jsonFile.close()
            
            
            convertFile[self.name] = {}

            convertFile[self.name]["Ingredients"] = self.ingString
            convertFile[self.name]["Bake Time"] = self.bakeTime
            convertFile[self.name]["Bake Temperature"] = self.bakeTemp
            convertFile[self.name]["Directions"] = self.directions
            convertFile[self.name]["Favorite"] = self.favorite

            revertFile = json.dumps(convertFile, indent=4)
            jsonFile = open(self.recipeType, "w")
            jsonFile.write(revertFile)
            jsonFile.close()
            
        else:
            pass
                






    
    def delete(self):
        inList = False
        print('Welcome to the delete menu')

        mycursor = Lookup.mydb.cursor()
        mycursor.execute("SELECT Id, Name, Type FROM recipes ORDER BY Id")
        myresult = mycursor.fetchall()

        for x in myresult:
            print('Id: %i   Name: %s   Type: %s \n' % (x))
        tbDelete = input('Please type the Id you would like to delete.\nOtherwise, type cancel to go back. \n')
        #Need exception handling
        if(tbDelete == "cancel"):
            tbDelete = 0
            return
            
        tbDelete = int(tbDelete)

        for x in myresult:
            if(tbDelete == x[0]):
                inList = True
            else:
                pass
        if(inList == False):
            print('No recipe found with that Id\n')
        else:
            mycursor2 = Lookup.mydb.cursor()
            sql = "DELETE FROM recipes WHERE Id = %s"
            adr = (tbDelete,)
            
            mycursor2.execute(sql, adr)

            Lookup.mydb.commit()


    def update(self):
        
        inList = False
        print('Welcome to the update menu')

        mycursor = Lookup.mydb.cursor()
        mycursor.execute("SELECT Id, Name, Type FROM recipes ORDER BY Id")
        myresult = mycursor.fetchall()

        for x in myresult:
            print('Id: %i   Name: %s   Type: %s \n' % (x))
        tbUpdate = input('Please type the Id you would like to update.\nOtherwise, type cancel to go back. \n')
        #Need exception handling
        if(tbUpdate == "cancel"):
            tbUpdate = 0
            return
            
        tbUpdate = int(tbUpdate)

        for x in myresult:
            if(tbUpdate == x[0]):
                inList = True
            else:
                pass
        if(inList == False):
            print('No recipe found with that Id\n')
        else:
            self.process = 'update'
            self.idHold = tbUpdate
            self.add()
        





        