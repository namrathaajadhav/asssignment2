#1.Write a program which can filter even numbers in a list by using filter function. The list is: 
#[1,2,3,4,5,6,7,8,9,10].

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers)




#2. Write a program which can map() to make a list whose elements are square of elements in 
#[1,2,3,4,5,6,7,8,9,10].

number = [1,2,3,4,5,6,7,8,9,10]
squared_number = list(map(lambda x: x**2, number ))
print(squared_number)




#3. Write a program which can map() and filter() to make a list whose elements are square of even 
#number in [1,2,3,4,5,6,7,8,9,10].


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(even_numbers)

squared_even_numbers = list(map(lambda x: x**2, even_numbers ))
print(squared_even_numbers)

#4. Write a program which can filter() to make a list whose elements are even number between 1 and 
#20 (both included).


numbers = range(1, 21)
even_numbers =list(filter(lambda x: x % 2 == 0, numbers ))
print(even_numbers)







#5. Write a program which can map() to make a list whose elements are square of numbers between 
#1 and 20 (both included).


number = range(1, 21)
squared_number =list(map(lambda x: x**2, number ))
print(squared_number)





#6. Define a class named American and its subclass NewYorker.


class American:
 def __init__(self, name, state):
  self.name = name
  self.state = state

def print_info(self):
  print(f"name: {self.name}, State: {self.state}")

class NewYorker(American):
 def __init__(self, name, borough):
  super().__init__(name, "New York")
  self.borough = borough

def print_info(self):
  super().print_info()
print(f"Borough: {self.borough}")

american = American("robbert", "California")
new_yorker = NewYorker("leo", "florida")

american.print_info()
new_yorker.print_info()





#7. Define a class named Rectangle which can be constructed by a length and width. The Rectangle 
#class has a method which can compute the area.


class Rectangle:
 def __init__(self, length, width):
  self.length = length
  self.width = width

def area(self):
 return self.length * self.width
rect = Rectangle(4, 5)

print("Area of the rectangle:", rect.area())


#8. Write a function that returns the lesser of two given numbers if both numbers are even, but 
#returns the greater if one or both numbers are odd

def lesser_or_greater(a, b):
 if a % 2 == 0 and b % 2 == 0:
  return min(a, b)
 else:
  return max(a, b)

num1 = 4
num2 = 6
result = lesser_or_greater(num1, num2)
print(result)  

num1 = 3
num2 = 5
result = lesser_or_greater(num1, num2)
print(result)  






#9. Write a function takes a two-word string and returns True if both words begin with same letter



def same_letter(string):
 words = string.split()
 return words[0].startswith(words[1][0])


string1 = "lappto lock"
string2 = "green garden"
string3 = "mango grapes"

print(same_letter(string1)) 
print(same_letter(string2))  
print(same_letter(string3)) 



#10. Write a function that capitalizes the first and fourth letters of a name

def capitalize_first_and_fourth(name):
  name_list = list(name)
  name_list[0] = name_list[0].upper()
  name_list[3] = name_list[3].upper()
  return ''.join(name_list)

name = "namratha jadhav"
result = capitalize_first_and_fourth(name)
print(result)  