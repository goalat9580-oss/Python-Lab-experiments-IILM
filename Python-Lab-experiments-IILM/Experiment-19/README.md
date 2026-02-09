# Experiment 19 – Trapping Rain Water

## Problem Statement

You are given an array `arr[]` of non-negative integers where each element represents the height of a block.  
The width of each block is `1`.

The task is to compute how much **rain water can be trapped** between the blocks after raining.

---

**Input:**

arr = [3, 0, 1, 0, 4, 0, 2]

**Output:**

10

---

## Algorithm

1. Initialize two pointers:
   - `left = 0`
   - `right = n - 1`
2. Initialize variables:
   - `left_max = 0`
   - `right_max = 0`
   - `water = 0`
3. While `left <= right`:
   - If `arr[left] <= arr[right]`:
     - Update `left_max = max(left_max, arr[left])`
     - Add `left_max - arr[left]` to `water`
     - Increment `left`
   - Else:
     - Update `right_max = max(right_max, arr[right])`
     - Add `right_max - arr[right]` to `water`
     - Decrement `right`
4. Return the total trapped water.

---

## Output Screenshot

![Output Screenshot]
https://github.com/goalat9580-oss/Python-Lab-experiments-IILM/blob/main/Python-Lab-experiments-IILM/Experiment-19/test19_passed.png

