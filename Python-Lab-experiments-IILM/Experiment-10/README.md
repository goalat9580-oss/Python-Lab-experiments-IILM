# Experiment 10 – Minimum Number of Jumps to Reach End

## Problem Statement

You are given an array `arr[]` of non-negative integers.  
Each element represents the maximum number of steps you can jump forward from that position.

If `arr[i] = 0`, you cannot move forward from that position.

Your task is to find the minimum number of jumps required to reach the last index starting from the first index.

Return `-1` if the last index cannot be reached.

---

**Input:**

arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]

**Output:**

3

---

## Algorithm

1. If the array is empty or the first element is `0`, return `-1`.
2. Initialize:
   - `maxReach = arr[0]`
   - `steps = arr[0]`
   - `jumps = 1`
3. Traverse the array from index `1` to `n - 1`:
   - Update `maxReach = max(maxReach, i + arr[i])`.
   - Decrease `steps` by `1`.
4. If `steps` becomes `0`:
   - Increment `jumps`.
   - If the current index is greater than or equal to `maxReach`, return `-1`.
   - Set `steps = maxReach - i`.
5. When the last index is reached, return `jumps`.

---

## Output Screenshot

![Output Screenshot]
