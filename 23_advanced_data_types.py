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
my_tuple2 = ("big", "bold", "And" "Beautiful")
my_tuple3 = (10, 8 , 9, 26, 5, 4, 3, 1, 2, 6, 7, 100, 50)

# my_tuple3.sort()
# print(sorted(my_tuple3))


# # set
# a set stores multiple items in a single variable, it is unordered and un indexed
# set items cannot be modified ( changed) but it allows removal and addition
my_set ={ 1, 2, 3, 4}


# # Dictionaries
# dict are a very importany python data type
# it sttores items in key valu pairs
my_dict = {"name" : "Black", "race" : "dog", "age" : 5}
# some dictionary method
# my_dict.get("name")     # gets the value of the name key
# my_dict.pop("name")     # removes and the returns the "name" key and valu "Black"
# my_dict.popitem()       # removes and returns the last key value oair added to the dict
# my_dict.keys()          # returns all the keys in the dictionary
# my_dict.values()        # retuns all the values in the dictionary
# my_dict.items()         # returns all the items (keys and values) in the dictionary
# del["age"]              # deleting a key value pair

my_dict["no_legs"] = 4    # adding a key value pair to the dictionary

print(my_dict)











# # to run the codes on this page coppy to your terminal ==> python 23_advanced_data_types.py 