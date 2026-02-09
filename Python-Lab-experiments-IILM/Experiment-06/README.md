*****Experiment 06***** – Rotate Array by One Position (Clockwise)

***Problem Statement***

Write a program to rotate a given array by one position in the clockwise direction.

**Input:**
Array: [1, 2, 3, 4, 5]

**Output:**
Array after rotating by one position clockwise: [5, 1, 2, 3, 4]

##Explanation:
The last element 5 moves to the front and all other elements are shifted one position to the right.

##Algorithm

1.Take the input array.

2.Store the last element in a variable last.

3.Traverse the array from the second last element to the first element and shift each element one step to the right.

4.Place the saved last element at the first index.

5.Print the updated array.


##Python Code
The code for this experiment is in clockwise_rotation_array.py

##Output

