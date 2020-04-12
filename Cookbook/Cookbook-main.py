from recipes import Recipes
from viewRecipes import ViewRecipes
contRun = True


while(contRun):
	#x = Recipes()
	#x.add()
	y = ViewRecipes()
	y.viewAll()
	#y.viewSelect()

	hold = input('\nWould you like to look up another? (yes or no)\n')
	if hold.lower() == 'no':
		contRun = False

