# Problem: Time Based Key-Value Store - https://leetcode.com/problems/time-based-key-value-store/

class TimeMap:
    def __init__(self):
        self.data = {}
    def binary_search(self, arr, left, right, target):
        if right >= left:
            mid = (left + right)//2
            val = arr[mid][1]

            if val == target:
                return mid
            elif val < target:
                return self.binary_search(arr, mid + 1, right, target)
            else:
                return self.binary_search(arr, left, mid - 1, target)
        else:
            if right < 0:
                return -1
            else:
                return right

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.data:
            self.data[key] = []
        self.data[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key in self.data:
            arr = self.data[key]
            indx = self.binary_search(arr, 0, len(arr) - 1, timestamp)
            if indx == -1:
                return ""
            return arr[indx][0]
        else:
            return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)