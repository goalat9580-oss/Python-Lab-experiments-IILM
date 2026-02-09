# Experiment 16 – Factorial of a Large Number

## Problem Statement

You are given an integer `n`.  
The task is to find the **factorial of `n`** and return a list of integers representing the **digits** of the factorial.

---

**Input:**

n = 5

**Output:**

[1, 2, 0]

---

## Algorithm

1. Initialize a list `result` with value `[1]` to store digits of the factorial.
2. For each number from `2` to `n`:
   - Multiply the current number with all digits in `result`.
   - Handle carry by updating digits and appending remaining carry.
3. After completing multiplication, `result` will store the factorial digits in reverse order.
4. Reverse `result` to obtain the correct digit order.
5. Return the result list.

---

## Output Screenshot

![Output Screenshot]

