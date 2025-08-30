class Solution(object):
    def replaceElements(self, arr):
        n = len(arr)
        maximum_right = -1
        for i in range(n-1, -1, -1):
            arr[i], maximum_right = maximum_right, max(maximum_right, arr[i])
        return arr
