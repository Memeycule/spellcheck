# SpellCheck
A small spellcheck code for python! you can use it as much as you can...

# How To Use
It's easy to use too! make an instance of `SpellCheck()` and use the `.setlist` method to set the list from where the program will choose the words which will be used to recommend to the user

# Examples
### Code
checker = SpellCheck()\
countries = ["India", "America", "Japan", "China", "Nepal"]\
checker.set_list(countries)\
result = checker.correct("Amriaeca")\
print(result)
### Result
America
