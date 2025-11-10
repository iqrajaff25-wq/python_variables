# Lists In Python
# Lists can be categorized or typed based on what they contain or how they are used.

# 01. Homogeneous Lists
#======================
# A homogeneous list contains elements of the same data type.
numbers = [1,2,3,4,5,6,7]
fruits = ['apple','date','orange','fig','mango']
# print(numbers)
print(fruits)



# 02. Heterogeneous Lists
#========================
#A heterogeneous list contains different types of data.
multi_data = ['Ali', 123, True, 3.54, [23,45]]
# print(multi_data)


# 03. Nested Lists (Lists within Lists)
#======================================
# A nested list means one or more lists inside another list.Commonly used for representing 2D data (like matrices, tables, grids).

nested_list = [ [12,13,14,15], ['ali','Hero','Hamza','Sundas'], [3.4, 4.6, 1.2]]
# print(nested_list)



# 04. Dynamic Lists
#==================
# All Python lists are dynamic, meaning they can grow or shrink in size during program execution.

# ADDITION OF ELEMENTS IN LIST
# ----------------------------

# Appending a list
fruits.append('appricot')
print(fruits, "List Appended")

# Extending a List
fruits.extend(['peach','pear','dragon fruit','raspberry','cherry','banana','berry','melon'])
print(fruits, 'List Extended')

#Insert an element
fruits.insert(2, 'pineapple')
print(fruits, 'Inserted an element at the second index')




# REMOVAL OF ELEMENTS
#-------------------

#Removing an element
fruits.remove('date')
print(fruits, 'Date is been removed')

# Removal of last value
fruits.pop()
print(fruits, 'Last value is been removed by using pop()')

# Removal by index
del fruits[2]
print(fruits, '3rd value is been removed from list by using del')

# Replace/Update an element according to index
fruits[1]='muskmelon'
print(fruits, 'An element replaced according to index')





# SLICING OF ELEMENTS FROM LIST
#------------------------------


print(fruits [1:4], 'Presenting 3 elements from 2nd to 4th positions')

    # Slicing from start
print(fruits[:5], 'Slicing the elemets from start')

    #Slicing from End
print(fruits[2:], 'Slicing elements till last value')

    # Slicing from and to a specific index
print(fruits[2:9:2], 'Slicing with skipping a single value respectively')
print(fruits[2::2], 'Slicing elements till end by skipping a single value')







