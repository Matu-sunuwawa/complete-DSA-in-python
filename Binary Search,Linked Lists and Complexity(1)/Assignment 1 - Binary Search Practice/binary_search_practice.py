
PROBLEM - ROTATED LISTS

You are given list of numbers, obtained by rotating a sorted list an unknown number of times. Write a function to determine the minimum number of times the original sorted list was rotated to obtain the given list. Your function should have the worst-case complexity of O(log N), where N is the length of the list. You can assume that all the numbers in the list are unique.
Example: The list [5, 6, 9, 0, 2, 3, 4] was obtained by rotating the sorted list [0, 2, 3, 4, 5, 6, 9] 3 times.
We define "rotating a list" as removing the last element of the list and adding it before the first element. E.g. rotating the list [3, 2, 4, 1] produces [1, 3, 2, 4].
"Sorted list" refers to a list where the elements are arranged in the increasing order e.g. [1, 3, 5, 7].


Optional Bonus 2: Handling repeating numbers

So far we've assumed that the numbers in the list are unique. What if the numbers can repeat? E.g. [5, 6, 6, 9, 9, 9, 0, 0, 2, 3, 3, 3, 3, 4, 4]. Can you modify your solution to handle this special case?


Optional Bonus 3: Searching in a Rotated List

Here's a slightly advanced extension to this problem:
You are given list of numbers, obtained by rotating a sorted list an unknown number of times. You are also given a target number. Write a function to find the position of the target number within the rotated list. You can assume that all the numbers in the list are unique.
Example: In the rotated sorted list [5, 6, 9, 0, 2, 3, 4], the target number 2 occurs at position 5.


