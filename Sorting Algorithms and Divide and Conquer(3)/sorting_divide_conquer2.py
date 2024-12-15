
## Sorting Algorithm divide and conquer

# problem.
Q# you're working on a new feature on Jovian called "Top Notebooks of the week". Write a function to start a list of notebooks in `decreasing order of likes.`
   keep in mind that up to millions of notebooks can be created every week, so your function needs to be as efficient as possible.
   
 Note That: we use `bubble sort`, as it causes smaller elements to bubble to the top and larger to sink to the bottom.
 
 ```
 def bubble_sort(nums):
	 nums = list(nums)
	 
    for _ in range(len(nums) - 1):
	    for i in range(len(nums) -1):
		    if nums[i] > nums[i+1]:
			    nums[i], nums[i+1] = nums[i+1], nums[i]
    return nums
 ```
 
 nums0, output = test0['input']['nums'], test0['output']
 print('Input:', nums0)
 print('Expected output:', output0)
 
 result0 = bubble_sort(nums0)
 print('Actual output:', result0)
 print('Match:', result0 == output0)
 
 
## Complexity
# Time complexity...O(n**2)
# Space Complexity...O(n)
 
 
# Apply Divide and Conquer:
# for steps look at `divide_conquer.png` and `divide_conquer_2.png`
- if te input list is empty or contains just one element, it is already sorted. return it.
- if not, divide the list of numbers into two roughly. equal parts.
- sort each part recursively using the merge sort algorithm. You'll get back two sorted lists.
- merge the two sorted lists to get a single sorted list.

```
def merge_sort(nums):
	if len(nums) <= 1:
		return nums
	mid = len(nums)//2
	
	left = muns[:mid]
	right = nums[mid:]
	
	left_sorted, right_sorted = merge_sort(left), merge_sort(right)
	
	sorted_nums = merge(left_sorted, right_sorted)
	
	return sorted_nums
```
# for detail look at `divide_conquer_demo.png`

```
def merge(nums1, nums2):
	merged = []
	i, j = 0, 0
	while i < len(nums1) and j < len(nums2):
		if nums1[i] <= nums2[j]:
			merged.append(nums1[i])
		else:
			merged.append(nums2[j])
	
	nums1_tail = nums1[i:]
	nums2_tail = nums2[j:]
	
	return merged + nums1_tail + nums2_tail
```
merge([1,4,7,9,11], [-1, 0, 2, 3, 8, 12])
nums0, output0 = test0['input']['nums'], test0['output']

print('input:', nums0)
print('Expectated output:', output0)
result0 = merge_sort(nums0)
print('Actual output:', result0)
print('Match:', result0 == output0)

```
def merge(nums1, nums2, depth=0):
	print(' '*depth, 'merge:', nums1, nums2)
	i, j, merged = 0,0,[]
	while i<len(nums1) and j<len(nums2):
		if nums1[i] <+ nums2[j]:
			merged.append(nums1[i])
			i +=1
		else:
			merged.append(nums2[j])
			j +=1
	return merged + nums1[i:] + nums2[j:]
def merge_sort(nums, depth=0):
	print(' '*depth, 'merge_sort:', nums)
	if len(nums) < 2:
		return nums
	mid = len(nums)//2
	return merge(merge_sort(nums[:mid], depth+1),merge_sort(nums[mid:],depth+1), depth+1)
```
merge_sort([5, -12, 2, 6, 1, 23, 7, 7, -12])
# for detail look at `divide_conquer_demo2.png`

# Complexity(merge sort algorithm):
- Time complexity...O(nlogn)
- space complexity...O(n)

# Apply Quick Sort...to overcome `space complexity O(n)`...that is not good:
- it is another divide-and-conquer based sorting algorithm called `quicksort`.
# for detail look at `quick_sort.png`

# Assume we already have a helper function called partitions
```
def quicksort(nums, start=0, end=None):
	if end is None:
		nums = list(nums)
		end = len(nums)-1
	if start < end:
		pivot = partition(nums, start,end)
		quicksort(nums, start, pivot-1)
		quicksort(nums, pivot+1, end)
	return nums
```
quicksort([3,3,5,23,4,2,3,23])

```
def partition(nums, start=0, end=None):
	if end is None:
		end = len(nums)-1
	l, r = start, end-1
	while r>1:
		if nums[1]<=nums[end]:
			l+=1
		elif nums[r] > nums[end]:
			r-=1
		else:
			nums[1], nums[r] = nums[r], nums[l]
	if nums[l] > nums[end]:
		nums[1], nums[end] = nums[end], nums[l]
	else:
		return end
```

l1 = [1,5,6,2,0,11,3]
pivot = partition(l1)
print(11, pivot)

nums0, output0 = test0['input']['nums'], test0['output']

print('Input:', nums0)
print('Expected output:', output0)
result0 = quicksort(nums0)
print('Actual output:', result0)
print('Match:', result0 == output0)

# Complexity(Quick sort)
# Best case partitioning(more probability)
- Time complexity...O(nlogn)...this is called average-case-complexity
- Space complexity...O(1)
# Worst case partitioning(less probability)
- Time complexity...O(n**2)
- Space complexity...O(1)
 
## Custom COmparison Function...(original problem)...notesbooks in decreasing orders.

# creates basic info class
```
class Notebook:
	def __init__(self, title, username, likes):
		self.title, self.username, self.likes = title, username, likes
	def __repr__(self):
		return 'Notebook <"{}/{}", {} likes>'.format(self.username, self.title, self.likes)
```
# i created sample notebooks look at...`sample_notebooks.png`

```
def compare_likes(nb1, nb2):
	if nb1.likes > nb2.likes:
		return 'lesser'
	elif nb1.likes == nb2.likes:
		return 'equal'
	elif nb1.likes < nb2.likes:
		return 'greater'
```

```
def default_compare(x, y):
	if x < y:
		return 'lesser'
	elif x == y:
		return 'equal'
	else:
		return 'greater'
def merge_sort(objs, compare=default_compare):
	if len(objs) < 2:
		return objs
	mid = len(objs)//2
	return merge(merge_sort(objs[:mid], compare),merge_sort(objs[mid:], compare), compare)
def merge(left, right, compare):
	i, j, merge = 0, 0,[]
	while i < len(left) and j < len(right):
		result = compare(left[i], right[j])
		if result == 'lesser' or result == 'equal':
			merged.append(left[i])
			i+=1
		else:
			merged.append(right[j])
	return merged + left[i:] + right[j:]
```
sorted_notebooks = merge_sort(notebooks, compare_likes)
RUN: sorted_notebooks

## Summary and Exercises:
# Covered:
- Bubble Sort
- Insertion Sort
- Merge Sort
- Quick Sort






