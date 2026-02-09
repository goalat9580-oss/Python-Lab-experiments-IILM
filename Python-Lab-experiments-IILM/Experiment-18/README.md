# Experiment 18 – Triplet Sum in Array

## Problem Statement

You are given an array `arr[]` and an integer `target`.

The task is to determine whether there exists a **triplet** in the array whose sum is equal to the given `target`.

Return `true` if such a triplet exists, otherwise return `false`.

---

**Input:**

arr = [1, 4, 45, 6, 10, 8]  
target = 13

**Output:**

true

---

## Algorithm

1. Sort the array in ascending order.
2. Traverse the array from index `0` to `n - 3`.
3. For each element, use two pointers:
   - `left = i + 1`
   - `right = n - 1`
4. While `left < right`:
   - Calculate `current_sum = arr[i] + arr[left] + arr[right]`.
   - If `current_sum == target`, return `true`.
   - If `current_sum < target`, increment `left`.
   - If `current_sum > target`, decrement `right`.
5. If no such triplet is found, return `false`.

---

## Output Screenshot

![Output Screenshot]
https://github.com/goalat9580-oss/Python-Lab-experiments-IILM/blob/main/Python-Lab-experiments-IILM/Experiment-18/test18_passed.png

