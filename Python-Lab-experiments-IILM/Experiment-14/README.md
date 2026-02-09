# Experiment 14 – Merge Overlapping Intervals

## Problem Statement

You are given an array of intervals where `intervals[i] = [start, end]`.

The task is to merge all **overlapping intervals** and return an array of **non-overlapping intervals** that cover all the intervals in the input.

---

**Input:**

intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]

**Output:**

[[1, 6], [8, 10], [15, 18]]

---

## Algorithm

1. Sort the intervals based on the starting time.
2. Initialize an empty list `merged`.
3. Traverse each interval:
   - If `merged` is empty or the current interval does not overlap with the last interval in `merged`,
     add the current interval to `merged`.
   - Otherwise, merge the intervals by updating the end time of the last interval.
4. Return the list of merged intervals.

---

## Output Screenshot

![Output Screenshot]


