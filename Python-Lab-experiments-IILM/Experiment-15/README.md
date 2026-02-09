# Experiment 15 – Common Elements in Three Sorted Arrays

## Problem Statement

You are given three sorted arrays `arr1`, `arr2`, and `arr3` in non-decreasing order.

The task is to find and print all **common elements** present in all three arrays in non-decreasing order.  
If no common elements exist, return an empty array. In that case, the output should be `-1`.

---

**Input:**

arr1 = [1, 5, 10, 20, 40, 80]  
arr2 = [6, 7, 20, 80, 100]  
arr3 = [3, 4, 15, 20, 30, 70, 80, 120]

**Output:**

[20, 80]

---

## Algorithm

1. Initialize three pointers `i`, `j`, and `k` to `0`.
2. Traverse all three arrays simultaneously:
   - If `arr1[i] == arr2[j] == arr3[k]`, add the element to the result.
   - Increment all three pointers.
3. If `arr1[i] < arr2[j]`, increment `i`.
4. Else if `arr2[j] < arr3[k]`, increment `j`.
5. Else, increment `k`.
6. Skip duplicate elements to avoid repeating values.
7. Continue until any one of the arrays is fully traversed.
8. Return the result array or `-1` if the result is empty.

---

## Output Screenshot

![Output Screenshot]

