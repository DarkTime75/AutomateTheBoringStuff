# Q: What is []?
# A: [] is an empty list which doesn't contain any elements

# Q: How would you assign the value 'hello' as the third value in a list stored in a variable named spam? (Assume spam contains [2, 4, 6, 8, 10].)
spam =  [2, 4, 6, 8, 10]
spam[2] = "hello"
print(spam) # Prints [2, 4, 'hello', 8, 10]

# For the following three questions, let’s say spam contains the list ['a', 'b', 'c', 'd']
# Q: What does spam[int(int('3' * 2) // 11)] evaluate to?
spam = ['a', 'b', 'c', 'd']
res = spam[int(int('3' * 2) // 11)] 
# Tracing of above code:
# spam[int(int('33') // 11)]
# spam[int(33 // 11)]
# spam[int(3)]
# spam[3]
# 'd'
print(res) # Prints 'd'

# What does spam[-1] evaluate to?
print(spam[-1]) # Prints 'd'

# What does spam[:2] evaluate to?
print(spam[:2]) # Prints ['a', 'b'], i.e slices the list from the starting index to index 1

# For the following three questions, let’s say bacon contains the list [3.14, 'cat', 11, 'cat', True].
# Q:  What does bacon.index('cat') evaluate to?
bacon = [3.14, 'cat', 11, 'cat', True]
res = bacon.index('cat')
print(res) # Prints 1, i.e returns the index of the first occurance of the element

# Q: What does bacon.append(99) make the list value in bacon look like?
bacon.append(99)
print(bacon) # Prints [3.14, 'cat', 11, 'cat', True, 99], i.e adds 99 to the end of the list.

# Q: What does bacon.remove('cat') make the list value in bacon look like?
bacon.remove('cat')
print(bacon) # Prints [3.14, 11, 'cat', True, 99], i.e removes the first occurance of the element in the list.

# Q: What are the operators for list concatenation and list replication?
# A: '+' operator is used for list concatenation and '*' is used for list replication

# Q: What is the difference between the append() and insert() list methods?
# A: <list>.append() method is used to add an element to the end of the list whereas <list>.insert() method is used to add an element at a certain index in the list.

# Q: What are two ways to remove values from a list?
# A: First way is to use <list>.remove() method which only removes the first occurance of the value in the list. The Second method is by using the 'del' keyword

# Q: Name a few ways that list values are similar to string values.
# A: 
# 1) Elements of a list as well as strings can be accessed through indexes
# 2) List and string both are iterables, i.e can be used in 'for' loops
# 3) Both strings and lists can be sliced.
# 4) Strings as well as lists can be concatenated and replicated

# Q: What is the difference between lists and tuples?
# A: lists are mutable as in the elements of a list can be mutated i.e modified, removed. Whereas, tuple is immutable as in elements of a tuple cannot be modified.

# Q: How do you type the tuple value that has just the integer value 42 in it?
# A: We indicate it as:
tup = (42,)

# Q: How can you get the tuple form of a list value? How can you get the list form of a tuple value?
# A: Assume a list
List = [1, 2, 3, 4, 5]
# It can be converted to tuple by using tuple() function
result = tuple(List)
print(result)
# Now, assume a tuple
Tuple = (1, 2, 3, 4, 5)
# It can be converted to list using list() function
Result = list(Tuple)
print(Result)

# Q: Variables that “contain” list values don’t actually contain lists directly. What do they contain instead?
# A: They contain references to list values