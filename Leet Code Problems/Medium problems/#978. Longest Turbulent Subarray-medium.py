class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        left, right = 0, 0
        max_length = 1  # At least one element is always a valid subarray

        while right < n - 1:
            if left == right:
                if arr[left] == arr[left + 1]:
                    left += 1
                right += 1
            else:
                if arr[right - 1] < arr[right] > arr[right + 1] or arr[right - 1] > arr[right] < arr[right + 1]:
                    right += 1
                else:
                    left = right

            max_length = max(max_length, right - left + 1)

        return max_length
        