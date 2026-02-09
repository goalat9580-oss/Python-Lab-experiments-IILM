# Experiment 09 – Two Sum Problem

## Problem Statement
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.  
You may assume that each input would have exactly one solution, and you may not use the same element twice.  
You can return the answer in any order.

**Input:**  
nums = [2, 7, 11, 15], target = 9

**Output:**  
[0, 1]

**Explanation:**  
Because `nums[0] + nums[1] == 9`, we return `[0, 1]`.

---

## Algorithm
1. Initialize an empty hash map/dictionary.  
2. Traverse the array `nums` with index `i`:  
   - Calculate `need = target - nums[i]`.  
   - If `need` is in the hash map, return `[hash_map[need], i]`.  
   - Otherwise, add `nums[i]` with index `i` to the hash map.  
3. The answer will be found during traversal as there is exactly one solution.

---

## Output Screenshot

![Output Screenshot](https://github.com/goalat9580-oss/Python-Lab-experiments-IILM/blob/main/Python-Lab-experiments-IILM/Experiment-09/test9_passed.png)

