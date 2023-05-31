#exercise1
places = [" ","Argentina", " ", "San Diego","","  ","","Boston","New York"]
def empty_spaces(place):
    if place == "  ":
        return True
    elif place == " ":
        return True
    elif place == "":
        return True
    False

print(list(filter(empty_spaces,places)))

#exercise2

# i watchedd some videos to get to the solution after i gave up (i do understand what each code does :)
#.sort methood has a kye value so i set it to "=lambda" and i did my code as i usually do with lambda function.

author = ["Joel Carter", "Victor aNisimov", "Andrew P. Garfield","David hassELHOFF","Gary A.J. Bernstein"]

# i splitted my list using split method and accessed the split using [-1] and lowered case all the letters.
author.sort(key=lambda last_name: last_name.split(' ')[-1].lower())
print(author)

#exercise3
#(1.8)*c + 32
places2 = [('Nashua',32),("Boston",12),("Los Angelos",44),("Miami",29)]
f = list(map(lambda c:((1.8) * c[1]+32),places2))
print(f)

#exercise4

def fibonacci(x):
    if 0 < x <= 2:
        return 1
    elif x > 2:
        return fibonacci(x-1) + fibonacci(x-2)
    elif x % 1 != 0:
        return "input can't be float.. or negative.."
    else:
        return "input can't be float.. or negative.."
print(fibonacci(5))
        

        


# def test(n):
#     if 0 < n <= 2:
#         return 1
#     elif n > 2:
#         return fibonacci(n-1) 
# print(test(8))

# def test2(n):
#     if 0 < n <= 2:
#         return 1
#     elif n > 2:
#         return fibonacci(n-2) 
# print(test2(8))
 

