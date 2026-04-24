# Print statements
print("Hello World!")
print("This is intro in python programming")

# Variables
a = 5 + 10, 9 - 4, 6*5, 16/4, 16//4, 30%3, 9 ** 2
b = "Not quite my tempo"
print(b)
print(a)

x = 5
y = 9.6
z = 'caravan'
r = True

# If Statements
if x > 3:
    print("x is greater than 3")
else:
    print("x is less than 3")

# For/While loops
for i in range(5):
    print(i)
i = 0
while i < 5:
    print(i)
    i += 1

# Functions
def multiply(a, b):
    return a * b

# Recursive functions
def multiply_recursive(a, b):
    if b == 0:
        return 0
    return a + multiply_recursive(a, b - 1)

# Object Oriented Programming
class Whiplash:
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

    def play(self):
        return self.title + "is playing"

# Data structures
# Array (Lists in Python)
my_list = [5, 9.6, "caravan", True]

# Linked list
class LinkedList:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# Binary search tree
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# Hash table (Dictionary in python)
my_dict = { "not": 1, "my": 2, "tempo": 3 }

# Algorithms

# Big-O Notation: O(1) to O(n!)

# Sorting Algorithms, below is selection sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr