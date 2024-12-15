
## python Interview Questions

# Amazon Interview Question(`it is easy and good.`)

Q# Subarray with Given Sum

- you are given an array of numbers (non-negative). Find a continuous subarray of the list which adds up to a given sum.

[1,7,4,2,1,3,11,5] target 10
output: 2,6

# Do not look at me
```
def subarray_sum3(arr, target):
	n = len(arr)
	i, j, s = 0, 0, 0
	while i<n and j<n+1:
		if s == target:
			return i,j
		elif s<target:
			if j>n:
				s+=arr[j]
			j+=1
		elif s>target:
			s-=arr[i]
			i+=1
	return None, None
```


# Google Interview Question(`it is hard and not good.`)

Q# Minimum Edit Distance
- Given two strings A and B. find the minimum number of steps required to convert A to B.(each operation is counted as 1 step.)You have the ff 3 operations permitted on a word:
	- Insert a character
	- Delete a character
	- Replace a character
`google_interview.png`

```
def min_steps(str1, str2, i1=0, i2=0):
	if i1 == len(str1):
		return len(str2) - i2
	elif i2 == len(str2):
		return len(str1) - i1
	elif str1[i1] == str2[i2]:
		return min_steps(str1, str2, i1+1, i2+1)
	else:
		return 1 + min(min_steps(str1, str2, i1+1, i2), # deleted
					   min_steps(str1, str2, i1+1, i2+1), # swap
					   min_steps(str1, str2, i1, i2+1)) # inserted
```





