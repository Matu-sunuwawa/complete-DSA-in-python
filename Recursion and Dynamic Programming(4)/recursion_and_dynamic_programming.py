## Recursion And Dynamic Programming
- Recursion and memoization
- Subsequence and knapsack problems
- Backtracking and pruning

# Longest Common Subsequence
Q# write a function to find the length of the longest common subsequence between two sequences. 
 # E.g. Given the strings "serendipitous" and "precipitation", the longest common subsequence is 'reipito' and its length is 7.
 
# Solution using Recursion without memorization
```
def lcs_recursive(seq1, seq2, idx1=0, idx2=0):
	if idx1 == len(seq1) or idx2 == len(seq2):
		return 0
	elif seq1[idx1] == seq2[idx2]:
		return 1 + lcs_recursive(seq1, seq2, idx1+1, idx2+1)
	else:
		option1 = lcs_recursive(seq1, seq2, idx1+1, idx2)
		option2 = lcs_recursive(seq1, seq2, idx1, idx2+1)
		return max(option1, option2)
```
TO={'input':{'seq1': 'serendipitous','seq2': 'precipitation'},'output':{7}}

RUN: %%time
	 lcs_recursive(**TO['input']) == TO['output']

# Complexity(Recursion without memory)
- Time COmplexity...O(2**(m+n))

# Solution(Recursion with memorization)
```
def lcs_memo(seq1, seq2):
	memo = {}
	def recurse(idx1=0, idx2=0):
		key=(idx1, idx2)
		if key in memo:
			return memo[key]
		elif idx1 == len(seq1) or idx2 == len(seq2):
			memo[key] = 0
		elif seq1[idx1] == seq2[idx2]:
			memo[key] = 1 + recurse(idx1+1, idx2+1)
		else:
			memo[key] = max(recurse(idx1+1, idx2), recurse(idx1, idx2+1))
		return memo[key]
	return recurse(0,0)
```

# Solution (using Dynamic programming)
```
def lcs_dp(seq1, seq2):
	n1, n2 = len(seq1), len(se2)
	table = [[0 for x in range(n2+1)] for x in range(n1+1)]
	for i in range(n1):
		for j in range(n2):
			if seq1[i] == seq2[j]:
				table[i+1][j+1] = 1 + table[i][j]
			else:
				table[i+1][j+1] = max(table[i][j+1], table[i+1][j])
	return table[-1][-1]
```


## Knapsack Problem

# Problem statement
Q# you're in charge of selecting a football(soccer) team from a large pool of players. Each player has a cost, and a rating. you have a limited budget.
 # what is the highest total rating of a team that fits within your budget. Assume that there is no minimum or maximum team size.

# General problem statement
Q# Given n elements, each of which has a weight and profit, determine the maximum profit that can be obtained by selecting a subset of the elements weighing
 # no more than w.
 i.e, profit [2,3,1,5,4,7]...like players rating
    , weight [4,5,1,3,2,5]...like players cost
    , capacity 15...like budget

# Time Compelexity...O(2**N)

```
def max_profit_recursive(weights, profits, capacity, idx=0):
	if idx == len(weights):
		return 0
	elif weights[idx] > capacity:
		return max_profit_recursive(weights, profits, capacity, idx+1)
	else:
		option1 = max_profit_recursive(weights, profits, capacity, idx+1)
		option2 = profits[idx] + max_profit_recursive(weights, profits, capacity-weights[idx], idx+1)
		
		return max(option1, option2)

```

# Exercise: do the solution with adding `Memorization`.

# Dynamic programming(Knapsack)

```
def max_profit_dp(weights, profits, capacity):
	n = len(weights)
	table = [[0 for _ in range(capacity+1)] for _ in range(n+1)]
	for i in range(n):
		for c in range(1, capacity+1):
			if weights[i] > c:
				table[i+1][c] = table[i][c]
			else:
				table[i+1][c] = max(table[i][c], profits[i] + table[i][c-weights[i]])
	return table[-1][-1]
```

# Time Complexity...O(N*W)





