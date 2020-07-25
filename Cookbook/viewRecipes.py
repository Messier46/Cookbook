# from dbConnection import Lookup
class ViewRecipes():
    """description of class"""



    def viewAll(self):
        mycursor = Lookup.mydb.cursor()

        mycursor.execute("SELECT Name, Type, Ingredients, Bake_Time, Bake_Temp, Directions, Favorite FROM recipes ORDER BY Type")

        myresult = mycursor.fetchall()
        #print(myresult)

        self.printLoop(myresult)
        

    def viewSelect(self):
        mycursor = Lookup.mydb.cursor()

        selection = input('What type of recipe are you looking for?\n')
        selection = selection.lower()

        sql = "SELECT Name, Type, Ingredients, Bake_Time, Bake_Temp, Directions, Favorite FROM recipes WHERE Type = %s"
        adr = (selection,)
        mycursor.execute(sql, adr)

        myresult = mycursor.fetchall()
        self.printLoop(myresult)
    




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

