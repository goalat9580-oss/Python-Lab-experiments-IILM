# Experiment 07 – Maximum Sum Subarray

## Problem Statement
You are given an integer array `arr[]`. You need to find the **maximum sum of a subarray** (containing at least one element) in the array.

**Input:**  
[2, 3, -8, 7, -1, 2, 3]

**Output:**  
11

---

## Algorithm
1. Take the input array.  
2. Initialize two variables:  
   - `max_current` with the first element of the array.  
   - `max_global` with the first element of the array.  
3. Traverse the array starting from the second element:  
   - Update `max_current = max(arr[i], max_current + arr[i])`  
   - Update `max_global = max(max_global, max_current)`  
4. After traversal, `max_global` holds the maximum subarray sum.  
5. Print `max_global`.

---

## Output Screenshot

![Output Screenshot]'
(https://github.com/goalat9580-oss/Python-Lab-experiments-IILM/blob/main/Python-Lab-experiments-IILM/Experiment-07/test7_passed.png)

