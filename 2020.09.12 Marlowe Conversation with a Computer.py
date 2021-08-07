##########
# LV Marlowe
# 09/12/2020
# Conversation with a Computer
# This program asks the user's name and discusses the user's pets.
##########

# Ask user's name and greet user.

firstName = input('What is your first name?\n')  # string
lastName = input('What is your last name?\n')  # string
print('Hello, ' + firstName, lastName + '.')  #Greet user.

# Ask about user's pets.

numDogs = input('How many dogs do you have?\n')  # string
numCats = input('And how many cats do you have?\n')  # string

# Evaluate user's knowledge of cats' superiority and educate if necessary.

answer = input('Did you know that cats are better than dogs? (yes or no)\n')  # string
if answer in ['YES', 'YES.', 'YES!', 'Yes', 'Yes.', 'Yes!', 'yes', 'yes.', 'yes!', 'y', 'y.', 'y!', 'Y', 'Y.', 'Y!']:  # Check if answer is in list of likely variations of affirmative.
    print('Good!')  #Praise user.
else:
    print('Well, now you do.')  # Otherwise, educate user.

# Inform user of ideal pet composition.

print('Everyone should have more cats than dogs.')

# Compare cats to dogs.

moreCats = int(numCats) - int(numDogs)  # integer calculating how many more cats than dogs
moreDogs = int(numDogs) - int(numCats)  # integer calculating how many more dogs than cats

# Evaluate composition of user's pets and suggest improvements if necessary.

if int(numDogs) == 0 and int(numCats) == 0:  # Check if user has no dogs and no cats.
    print('You have no dogs or cats. You should get at least', moreDogs + 1, 'cat.')  # User has no dogs and no cats. Suggest getting a cat.
elif int(numDogs) == 0 and int(numCats) == 1:  # If not, check if user has no dogs and 1 cat.
    print('You have no dogs and', int(numCats), 'cat. So, you already have', moreCats, 'more cat than you have dogs. That is great! Still, you should get your cat a cat friend.')  # User has no dogs and 1 cat. Praise user but suggest getting another cat.
elif int(numDogs) == 1 and int(numCats) == 0:  # If not, check if user has 1 dog and no cats.
    print('You have', int(numDogs), 'dog but no cats. So, you should get at least', moreDogs + 1, 'cats.')  # User has 1 dog and no cats. Suggest getting cats.
elif int(numDogs) > 1 and int(numCats) == 0:  # If not, check if user has more than 1 dog and no cats.
    print('You have', int(numDogs), 'dogs and no cats. That is unacceptable. You should get at least', moreDogs + 1, 'cats.')  # User has more than 1 dog and no cats. Suggest getting cats.
elif int(numDogs) == 0 and int(numCats) > 1:  # If not, check if user has no dogs and more than 1 cat.
    print('You have', int(numCats), 'cats but no dogs! So, you already have', moreCats, 'more cats than dogs. You are awesome!')  # User has no dogs and more than 1 cat. Praise user.
elif int(numDogs) == int(numCats):  # If not, check if user has same number of cats and dogs.
    print('You have the same number of cats as dogs. So, you should get at least', moreDogs + 1, 'more cat.')  # User has same number of cats and dogs and at least 1 dog and 1 cat. Suggest getting more cats.
elif moreCats == 1:  # If not, check if user has 1 more cat than dogs.
    print('You have', moreCats, 'more cat than you have dogs. That is cutting it close, so you should get even more cats.')   # User has at least 1 dog and 1 more cat than dogs. Suggest getting more cats.
elif moreDogs == 1:  # If not, check if user has 1 more dog than cats.
    print('You have', moreDogs, 'more dog than you have cats. So, you should get at least', moreDogs + 1, 'more cats.')  # User has 1 more dog than cats and at least 1 cat. Suggest getting more cats.
elif int(numDogs) < int(numCats):  # If not, check if user has more cats than dogs.
    print('You have', moreCats, 'more cats than dogs! Keep up the good work!')  # User has at least 1 dog and at least 2 more cats than dogs. Praise user.
else:
    print('You have', moreDogs, 'more dogs than cats. So, you should get at least', moreDogs + 1, 'more cats.')   # Otherwise, user has at least 2 more dogs than cats and at least 1 cat. Suggest getting more cats.
