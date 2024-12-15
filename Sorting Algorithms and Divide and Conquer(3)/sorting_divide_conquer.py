

## SORTING ALGORITHMS AND DIVIDE AND CONQUER

# HASH TABLES IN PYTHON
# PYTHON DICTIONARIES AND HASH TABLES

i.e, phone_numbers = {
	'Aakash':'9489484949',
	'Hemanth':'9595949494',
	'Siddhant':'9231325312'
}
RUN: phone_numbers

# access a person's phone number:
RUN: phone_numbers['Aakash']

# store new and update phone numbers:
phone_numbers['Vishal'] = '8787878787' # Add new value
phone_numbers['Aakash'] = '7878787878' # Update the value
RUN: phone_numbers

# look
```
for name in phone_numbers:
	print('Name:', name, ', phone Number:', phone_numbers[name])
```
	
NOTE THAT: Dictionaries in python are implemented using a data structure called hash table.
		   - a hash table uses a list/array to store the key-value pairs,
		     and uses a hashing function to determine the index for storing or retrieving the data associated with a given key.
		     `hash_represent.png`

Q# Implement a HashTable class which supports the following operations:
	- insert
	- find
	- update
	- list

```
class HashTable:
	def insert(self, key, value):
		"""Insert"""
		pass
	def find(self, key):
		"""Find"""
		pass
	def update(self, key, value):
		"""change the value associated with a key"""
		pass
	def list_all(self):
		"""List all"""
		pass
```

# Data List
 - create a python list that will hold key-value pairs.
 - MAX_HASH_TABLE_SIZE = 4096 ... fixed size...just for sample
 
data_list = [None] * 4096
RUN: len(data_list) == 4096
data_list[99] == None

## Hashing Function
 - is used to convert strings and other non-numeric data types into `numbers`.

# Steps for implement `Hashing Function`:
1.iterate over string.
2.convert each character to number using `ord` function.
3.add numbers.
4.take `remainder` of the result with the size of the data list.

```
def get_index(data_list, a_string):
	result = 0
	
	for a_character in a_string:
		a_number = ord(a_character)
		result += a_number
		
	list_index = result%len(data_list)
	return list_index
```

RUN: get_index(data_list, '') == 0
RUN: get_index(data_list, 'Aakash') == 585
RUN: get_index(data_list, 'Don O Leary') == 941

# what is going on...here is the simple one...
data_list2 = [None]*48
get_index(data_list2, 'Aakash') == 9
RUN: ord('A') + ord('a') + ord('k') + ord('a') + ord('s') + ord('h')
RUN: 585 % 48

# insert
 - to insert a key-value pair into hash table, we can simply get the hash of the kay, and store pair at that index in te data list.
 
key, value = 'Aakash', '7878787878'
idx = get_index(data_list, key)
RUN: idx
data_list[idx] = (key, value)

# all with single line:
data_list[get_index(data_list, 'Hemanth')] = ('Hemanth', '9595949494')

# find
 - retrieve the value associated with pair, we can get hash of key and look up that index in the data list.

idx = get_index(data_list, 'Aakash')
RUN: idx

key, value = data_list[idx]
RUN: value


# list
 - to get list of keys, use `list comprehension`.

pairs = [kv[0] for kv in data_list if kv is not None]
RUN: pairs

# i think you do not understand `list comprehension`...
i.e, 
list1 = [1.3, 2.4, 3.2, 6, 7]
list2 = [x for x in list1]
RUN: list2
list2 = [x for x in list1 if x>3]
RUN: list2 # it will print x greater that 3...==>3.2,6,7
import math
list2 = [math.ceil(x) for x in list1 if x > 3]
RUN: list2

# all combined:
```
class BasicHashTable:
	def __init__(self, max_size=MAX_HASH_TABLE_SIZE):
		self.data_list = [None] * max_size
	def insert(self, key, value):
		idx = get_index(self.data_list, key)
		self.data_list[idx]=key,value
	def find(self, key):
		idx=get_index(self.data_list, key)
		kv=self.data_list[idx]
		if kv is None:
			return None
		else:
			key, value = kv
			return value
	def update(self, kay, value):
		idx=get_index(self.data_list, key)
		self.data_list[idx]=key,value
	def list_all(self):
		return [kv[0] for kv in self.data_list if kv is not None]
```

basic_table = BasicHashTable(max_size=1024)
RUN: len(basic_table.data_list)==1024

basic_table.insert('Aakash', '9999999999')
basic_table.insert('Hemanth', '8888888888')

RUN: basic_table.find('Hemanth') == '8888888888'
RUN: basic_table.find('Aakash', '9999999999')

RUN: basic_table.update('Aakash', '7777777777')
RUN: basic_table.find('Aakash', '7777777777')
RUN: basic_table.list_all() == ['Aakash', 'Hemanth']

## HANDLING COLLISIONS WITH LINEAR PROBING
 - Exceptional cases...i.e,"listen", "silent"

i.e,
basic_table.insert('listen', 99)
basic_table.insert('silent', 200)
RUN: basic_table.find('listen')

```
def get_valid_index(data_list, key):
	idx=???
	while True:
		kv=???
	if ???:
		return idx
	
	k, v = kv
	if ???:
		return idx
	idx+=1
	if idx==len(data_list):
		idx=0
```

## Complete hash table with `linear probing`
```
class ProbingHashTable:
	def __init__(self, max_size=MAX_HASH_TABLE_SIZE):
		self.data_list=???
	def insert(self, key, value):
		idx=get_valid_index(self.data_list, ???)
		self.data_list[idx]=???
	def find(self, key):
		idx=???
		kv=???
		return None if kv is None else kv[1]
	def update(self, key, value):
		idx=???
		self.data_list[idx]=???
	def list_all(self):
		return [??? for kv in self.data_list if kv is not None]
```
# creating a new hash table
probing_table = ProbingHashTable()
# insert a value
probing_table.insert('listen', 99)
# check the value
probing_table.find('listen') == 99

# insert a colliding key
probing_table.insert('silent', 200)
# check a new and old key
probing_table.find('listen') == 99 and probing_table.find('silent') == 200

# update a key
probing_table.insert('listen', 101)
# check teh value
probing_table.find('listen') == 101
probing_table.list_all() == ['listen', 'silent']

## complexity analysis...
 - insert/update...Average-case time complexity(O(1))...Worst-case time complexity(O(n))
 - find...Average-case time complexity(O(1))...Worst-case time complexity(O(n))
 - delete...Average-case time complexity(O(1))...Worst-case time complexity(O(n))
 - list...Average-case time complexity(O(n))...Worst-case time complexity(O(n))














