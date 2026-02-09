Experiment 10 – Minimum Number of Jumps
Problem Statement

You are given an array arr[] of non-negative integers.

Each element represents the maximum number of steps you can jump forward from that position.

If arr[i] = 0, you cannot jump forward from that position.

Find the minimum number of jumps needed to reach the last index.

Return -1 if the last index cannot be reached.

Input

arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]

Output

3

Explanation

Start at index 0.

Jump from index 0 to index 1.

Jump from index 1 to index 4.

Jump from index 4 to the last index.

Minimum number of jumps required is 3.

Algorithm

Step 1: If the array is empty or the first element is 0, return -1.

Step 2: Initialize maxReach = arr[0], steps = arr[0], jumps = 1.

Step 3: Traverse the array from index 1 to the end.

Step 4: Update maxReach = max(maxReach, i + arr[i]).

Step 5: Decrease steps by 1 after each move.

Step 6: If steps becomes 0, increment jumps.

Step 7: If the current index is greater than or equal to maxReach, return -1.

Step 8: When the last index is reached, return jumps.

Output Screenshot
