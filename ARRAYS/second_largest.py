class Solution:
    def getSecondLargest(self, arr):
        largest=-1
        second_largest=-1
        
        for i in range(len(arr)):
            if arr[i]>largest:
                largest=arr[i]
        for i in range(len(arr)):
            if arr[i]>second_largest and arr[i]!= largest:
                second_largest=arr[i]
        return second_largest