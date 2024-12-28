# Problem:
"""
this one is based on:
'Alice has some cards with numbers written on them. She arranges the cards in decreasing order, 
and lays them out face down in a sequence on a table. She challenges Bob to pick out the card containing a given number by 
turning over as few cards as possible. Write a function to help Bob locate the card.'

testcases:
test1 = {
	'inputs': {
		'cards': [10, 8, 6, 4, 2],
		'query': 6
	},
	'output': 2
}

cards = [10, 8, 6, 4, 2]
query = 10
output = 0

cards = [10, 8, 6, 4, 2]
query = 2
output = 4

cards = [5]
query = 5
output = 0

cards = [5]
query = 3
output = -1

cards = [10, 8, 6, 4, 2]
query = 7
output = -1

cards = [10, 8, 8, 6, 4, 2]
query = 8
output = 1

cards = []
query = 10
output = -1
"""

test1 = {
	'inputs': {
		'cards': [],
		'query': 10
	},
	'output': -1
}

# # Solution For this scenario
# def test_result(cards, query, mid):
#     if cards[mid] == query:
#         if (mid-1) >= 0 and cards[mid-1] == query:
#             return 'left'
#         else:
#             return 'found'
#     elif cards[mid] < query:
#         return 'left'
#     else:
#         return 'right'


# def binary_search(cards, query):
#     # print("cards:", cards, "query:",query)
#     l,h = 0,len(cards)-1

#     while l <= h:
#         mid = (l + h) //2
#         # print("mid:", mid)

#         result = test_result(cards, query, mid)

#         if result == 'found':
#             return mid
#         elif result == 'left':
#             h = mid - 1
#         else:
#             l = mid + 1
#     return -1

# if binary_search(**test1['inputs']) == test1['output']:
#     print("Passed")
# else:
#     print("Failed")
    

# Generic Binary Search
def binary_search(l,h, condition):
    while l <= h:
        mid = (l + h) //2
        result = condition(mid)
        if result == 'found':
            return mid
        elif result == 'left':
            h = mid - 1
        else:
            l = mid + 1
    return -1

def test_result(cards, query):
    def condition(mid):
        if cards[mid] == query:
            if (mid-1) >= 0 and cards[mid-1] == query:
                return 'left'
            else:
                return 'found'
        elif cards[mid] < query:
            return 'left'
        else:
            return 'right'
    return binary_search(0, len(cards)-1, condition)
    

# if test_result(**test1['inputs']) == test1['output']:
#     print("Passed")
# else:
#     print("Failed")


"""
Another Question: 'GIVEN AN ARRAY OF INTEGERS NUMS SORTED IN ASCENDING ORDER, FIND THE STARTING AND ENDING POSITION OF A GIVEN NUMBER.'


test cases:
test2 = {
	'inputs': {
		'nums': [2, 4, 4, 4, 6, 8, 10],
		'target': 4
	},
	'output': (1,3)
}

nums = [2, 2, 4, 6, 8, 10]
target = 2
output = (0,1)

nums = [2, 4, 6, 8, 10, 10]
target = 10
output = (4,5)

nums = [1, 2, 3, 4, 5, 6]
target = 3
output = (2,2)

nums = [1, 3, 5, 7, 9]
target = 4
output = (-1,-1)

nums = [4, 4, 4, 4, 4]
target = 4
output = (0,4)

nums = []
target = 4
output = (-1,-1)
"""

test2 = {
	'inputs': {
		'nums': [],
		'target': 4
	},
	'output': (-1,-1)
}

# solving medium question using 4 function
def binary_search(l,h,condition):
    while l<=h:
        mid = (l+h)//2
        result = condition(mid)
        if result == 'found':
            return mid
        elif result == 'left':
            h = mid - 1
        else:
            l = mid + 1
    return -1

def first_position(nums, target):
    def condition(mid):
        if nums[mid] == target:
            if (mid-1) >=0 and nums[mid-1] == target:
                return 'left'
            else:
                return 'found'
        elif nums[mid] < target:
            return 'right'
        else:
            return 'left'
    return binary_search(0, len(nums)-1, condition)

def last_position(nums, target):
    def condition(mid):
        if nums[mid] == target:
            if (mid+1)<=len(nums)-1 and nums[mid+1] == target:
                return 'right'
            else:
                return 'found'
        elif nums[mid] > target:
            return 'left'
        else:
            return 'right'
    return binary_search(0, len(nums)-1, condition)

def start_and_end(nums, target):
    return (first_position(nums, target),last_position(nums,target))


print(start_and_end(**test2['inputs']))
if start_and_end(**test2['inputs']) == test2['output']:
    print('Passed')
else:
    print('Failed')















