""" This game represents a bartender asking questions that determine your tastes
and then identify ingredients to suit those tastes. The code will then output
the bartender creating your drink for you, each ingredient at a time. """ 


# Create a list of questions and ingredients the bartender will ask for and use.
questions = {
     "strong": "Do you like your drinks strong?" + " \nEnter yes or no: ",
     "salty":  "Do you like your drinks salty? " + " \nEnter yes or no: ",
     "bitter": "Do you like your drinks bitter? " + " \nEnter yes or no: ",
     "sweet":  "Do you like your drinks sweet? " + " \nEnter yes or no: ",
     "fruity": "Do you like your drinks fruity? " + " \nEnter yes or no: ",
}

ingredients = {
     "strong": ["glug of rum", "slug of whisky", "splash of gin"],
     "salty":  ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
     "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
     "sweet":  ["sugar cube", "spoonful of honey", "splash of cola"],
     "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}


import random 

def drink_preference():
     """Puts drink preference into a new dictionary"""
     ingredients_dictionary = {}
     for question, category in questions.items():
          user_input = input(category + " ")
          ingredients_dictionary[question] = (user_input == "yes")
     return ingredients_dictionary
     
def mixing_drink(category):
     """Uses the preferences in ingredients_dictionary to make the drink"""
     drink = []
     for question, category in category.items():
          if category is True:
               drink.append(random.choice(ingredients[question]))
     return drink

def main():
     results = drink_preference()
     print("\nHere's a cocktail with:")
     for drink in mixing_drink(results):
          print(" " + drink)
          
if __name__ == "__main__":
     main()