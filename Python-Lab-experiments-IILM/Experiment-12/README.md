# Experiment 12 – Find the Duplicate Number

## Problem Statement

You are given an array of integers `nums` containing `n + 1` integers, where each integer is in the range `[1, n]`.

There is only **one repeated number** in the array.  
Your task is to find and return this repeated number.

The solution must be implemented **without modifying the array** and using **only constant extra space**.

---

**Input:**

nums = [1, 3, 4, 2, 2]

**Output:**

2

---

## Algorithm

1. Use Floyd’s Tortoise and Hare (Cycle Detection) algorithm.
2. Initialize two pointers `slow` and `fast` at the first element.
3. Move:
   - `slow` by one step (`slow = nums[slow]`)
   - `fast` by two steps (`fast = nums[nums[fast]]`)
4. Continue until both pointers meet.
5. Reset one pointer to the first element.
6. Move both pointers one step at a time.
7. The point where they meet again is the duplicate number.
8. Return the duplicate number.

---

## Output Screenshot

![Output Screenshot]
