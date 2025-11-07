# list abd tupules
# A list is a mutable (modifiable) collection of elements, it acn store multiple data types
my_list = [1, 2, 3, "Apple", "red", True]
list2 =["block", "glock", 14, False]
list3 = ["my", "Love", "for", "Her", "never", "Dies"]
list4 =[2, 25, 33, 59 , 47, 100, 76]
# common operations
# accessing elements
# print(my_list)

# # slicing
# print(my_list[1:3])
# print(my_list[-3:-1])

# # modifying elements
# my_list[1] = 10

# my_list[1: 2] = [10, 12]

# my_list[1: 2] = [10]

# my_list.insert(0, "orange")

# my_list.extend(["cherry", "banana"])

# adding elements

# for x in list2:  # addilind elements to a list by looping
#     my_list.append(x)
#     print(my_list)

# removing items
# my_list.remove("Apple") # specifying the exact item to remove
# my_list.pop() #removes last item
# del my_list[0]  # deletind specified index
# print(my_list)
# sortin elements
''' list containong strings are sorted aphabetically
while list containing numbers are sorted numricaly ascending order unless specified otherwise
upper case are sorted befor lower case strings
note when sorting all elements in the list must be of the same type
'''

# list3.sort() # normar ascending order nad upper case first
# list3.sort(reverse = True) # sort in descending order
# list3.sort(key = str.lower) # sorts lower case first

# list4.sort() # normar ascending order nad upper case first
# list4.sort(reverse = True) # sort in descending order
# print(list3)
# print(list4)

# using customized sorting funtion
# def myFunc(item):
#     return abs(item - 40) # sorting based on the closser they are to 40 closest first
# list4.sort(key = myFunc)
# print(list4)

# # Tuples
# A tuple is an immutable (unmodifiable) collection of elements
# it can be accessed and used the same way a list can be accessed but it cannot be modified
my_tuple = (1, 2, 3, 4, "Apple", True)


# # set
# a set stores multiple items in a single variable, it is unordered and un indexed
# set items cannot be modified ( changed) but it allows removal and addition
my_set ={ 1, 2, 3, 4}
# to run the codes on this page coppy to your terminal ==> python 23_advanced_data_types.py