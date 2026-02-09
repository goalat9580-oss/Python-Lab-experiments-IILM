# Experiment 11 – Minimize the Heights

## Problem Statement

You are given an array `arr[]` denoting the heights of `n` towers and a positive integer `k`.

For each tower, you must perform exactly one of the following operations:
- Increase the height of the tower by `k`
- Decrease the height of the tower by `k`

After modifying each tower, find the minimum possible difference between the height of the shortest and tallest towers.

It is compulsory to either increase or decrease the height of each tower by `k`.

Return the minimum possible difference.

**Note:**  
After the operation, the resultant array should not contain any negative integers.

---

**Input:**

k = 2  
arr = [1, 5, 8, 10]

**Output:**

5

---

## Algorithm

1. Sort the array in ascending order.
2. Set:
   - `smallest = arr[0] + k`
   - `largest = arr[n - 1] - k`
3. If `smallest > largest`, swap them.
4. Traverse the array from index `1` to `n - 2`:
   - Calculate `subtract = arr[i] - k`
   - Calculate `add = arr[i] + k`
5. Ignore the element if `subtract` is negative.
6. Update `smallest` and `largest` to minimize the difference.
7. Return `min(largest - smallest, original_max - original_min)`.

---

## Output Screenshot

![Output Screenshot]
https://github.com/goalat9580-oss/Python-Lab-experiments-IILM/blob/main/Python-Lab-experiments-IILM/Experiment-11/test11_passed.png
