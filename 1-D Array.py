# Create an array containing car names:

cars = ["Ford", "Volvo", "BMW"]
print(cars)

#Get the value of the first array item:

x = cars[0]
print(x)

#Modify the value of the first array item:

cars[0] = "Toyota"
print(cars)

#Return the number of elements in the cars array:

x = len(cars)
print(x)

#Print each item in the cars array:

for x in cars:
  print(x)

#Add one more element to the cars array:

cars.append("Honda")
print(cars)

#Adds an element at the specified position

cars.insert(2,"Mazda")
print(cars)

#Delete the second element of the cars array:

cars.pop(1)
print(cars)

#Delete the element that has the value "Volvo":

cars = ["Ford", "Volvo", "BMW"]
cars.remove("Volvo")
print(cars)

#Returns a copy of the list

cars_2=cars.copy()
print(cars_2)


#Removes all the elements from the list

cars.clear()
print(cars)

#Sorts the list
cars_2.sort()
print(cars_2)

#Reverses the order of the list

cars_2.reverse()
print(cars_2)

#Returns the number of elements with the specified value

print(cars_2.count("Ford"))

