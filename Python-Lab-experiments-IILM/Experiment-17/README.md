# Experiment 17 – Check if Array is a Subset of Another Array

## Problem Statement

You are given two arrays `a[]` and `b[]`.  
The task is to determine whether array `b[]` is a **subset** of array `a[]`.

If all elements of `b[]` are present in `a[]`, return `true`, otherwise return `false`.

---

**Input:**

a = [11, 7, 1, 13, 21, 3, 7, 3]  
b = [11, 3, 7, 1, 7]

**Output:**

true

---

## Algorithm

1. Create a frequency map of elements in array `a[]`.
2. Traverse array `b[]`:
   - If an element is not present in the frequency map or its count is zero, return `false`.
   - Otherwise, decrease its count.
3. If all elements of `b[]` are found, return `true`.

---

## Output Screenshot

![Output Screenshot]


