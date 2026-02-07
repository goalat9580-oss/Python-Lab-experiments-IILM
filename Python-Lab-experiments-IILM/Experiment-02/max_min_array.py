class Solution:
    def getMinMax(self, arr):
         mn = arr[0]
         mx = arr[0]

         for i in range(1, len(arr)):
            if arr[i] < mn:
                mn = arr[i]
            if arr[i] > mx:
                mx = arr[i]

         return mn, mx
