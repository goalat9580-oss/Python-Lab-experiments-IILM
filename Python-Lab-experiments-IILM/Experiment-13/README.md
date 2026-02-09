# Experiment 13 – Merge Two Sorted Arrays Without Extra Space

## Problem Statement

You are given two sorted arrays `a[]` and `b[]` of sizes `n` and `m` respectively.

The task is to merge both arrays in **sorted order without using any extra space**.  
After merging:
- Array `a[]` should contain the **first `n` smallest elements**
- Array `b[]` should contain the **last `m` largest elements**

---

**Input:**

a = [2, 4, 7, 10]  
b = [2, 3]

**Output:**

a = [2, 2, 3, 4]  
b = [7, 10]

---

## Algorithm

1. Initialize two pointers:
   - `i` at the last index of array `a`
   - `j` at the first index of array `b`
2. While `i >= 0` and `j < m`:
   - If `a[i] > b[j]`, swap `a[i]` and `b[j]`
   - Decrement `i` and increment `j`
   - Otherwise, break the loop
3. Sort array `a`.
4. Sort array `b`.
5. Arrays are now merged in sorted order without using extra space.

---

## Output Screenshot

![Output Screenshot]

