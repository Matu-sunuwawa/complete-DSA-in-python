## BINARY SEARCH

## #1 without considering repetition of query(target number)

def locate_card(cards, query):
    lo, hi = 0, len(cards) - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        mid_number = cards[mid]
	
	print("lo:", lo, ", hi:", hi, ", mid:", mid, ", mid_number:", mid_number)
	
	if mid_number == query:
	    return mid
	elif mid_number < query:
	    hi = mid-1
	elif mid_number > query:
	    lo = mid + 1

    return -1

## #2 considering the repetition of query(target number)

def test_location(cards, query, mid):
    mid_number = cards[mid]
    print("mid:", mid, ", mid_number:", mid_number)
    if mid_number == query:
        if mid-1 >= 0 and cards[mid-1] == query:
			return 'left'
		else:
			return 'found'
    elif mid_number < query:
		return 'left'
    else:
		return 'right'

def locate_card(cards, query):
    lo, hi = 0, len(cards) - 1

    while lo <= hi:
	print("lo:", lo, ", hi:", hi)
	mid = (lo +hi) // 2
	result = test_location(cards, query, mid)

	if result == 'found':
	    return mid
	elif result == 'left':
	    hi = mid - 1
	elif result == 'right':
	    lo = mid + 1
    return -1



## #3 GENERIC BINARY SEARCH

def binary_search(lo, hi, condition):
	"""TODO - add docs"""
	while lo <= hi:
		mid = (lo + hi) // 2
		result = condition(mid)
		if result == 'found':
		    return mid
		elif result == 'left':
			hi = mid - 1
		else:
			lo = mid + 1
	return -1


## #4 IN CARDS CASE:

def locate_card(cards, query):
	
	def condition(mid):
		if cards[mid] == query:
			if mid > 0 and cards[mid-1] == query:
				return 'left'
			else:
				return 'found'
		elif cards[mid] < query:
			return 'left'
		else:
			return 'right'
			
		return binary_search(0, len(cards) -1, condition)


## QUICK QUESTION SOLVE USING 'GENERIC BINARY SEARCH'.....
Q# GIVEN AN ARRAY OF INTEGERS NUMS SORTED IN ASCENDING ORDER, FIND THE STARTING AND ENDING POSITION OF A GIVEN NUMBER.

def first_position(nums, target):
	def condition(mid):
		if nums[mid] == target:
			if mid > 0 and nums[mid-1] == target:
				return 'left'
			return 'found'
		elif nums[mid] < target:
			return 'right'
		else:
			return 'left'
	return binary_search(0, len(nums)-1, condition)

def last_position(nums, target):
	def condition(mid):
		if nums[mid] == target:
			if mid < len(nums)-1 and nums[mid+1] == target:
				return 'right'
			return 'found'
		elif nums[mid] < target:
			return 'right'
		else:
			return 'left'
	return binary_search(0, len(nums)-1, condition)
	
def first_and_last_position(nums, target):
	return first_position(nums, target), last_position(nums, target)
	
	
# IMPLEMENTING THE SOLUTION "SAMPLE"
def count_rotations_binary(nums):
	lo = ???
	hi = ???
	
	while ???:
		mid = ???
		mid_number = nums[mid]
		
		if mid > 0 and ???:
			return mid
		elif ???:
			hi = mid - 1
		else:
			lo = mid + 1
	return ???

