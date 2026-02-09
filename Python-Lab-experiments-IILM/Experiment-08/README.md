
# Experiment 08 – Search Insert Position in Sorted Array

## Problem Statement
Given a sorted array of distinct integers and a target value, return the index if the target is found.  
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

**Input:**  
nums = [1, 3, 5, 6], target = 5

**Output:**  
2

---

## Algorithm
1. Initialize two pointers: `low = 0`, `high = len(nums) - 1`.  
2. While `low` is less than or equal to `high`:  
   - Find mid = `(low + high) // 2`.  
   - If `nums[mid] == target`, return `mid`.  
   - Else if `nums[mid] < target`, set `low = mid + 1`.  
   - Else set `high = mid - 1`.  
3. If target is not found, return `low` (the insertion position).

---

## Output Screenshot

![Output Screenshot](https://github.com/goalat9580-oss/Python-Lab-experiments-IILM/blob/main/Python-Lab-experiments-IILM/Experiment-08/test8_passed.png)
