class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:

        '''
      Input: nums = [3,1,4,2], p = 6
      Output: 1
      total = 10
      target = 10 % 6 = 4

      dic = {
          0: -1,


      }

        '''
        total = sum(nums)
        if total  % p == 0:
            return 0


        target = total % p
        dic, n = {0:-1}, len(nums)

        curS, res = 0, n
        for i, num in enumerate(nums):
            curS = (curS + num) % p
            if dic.get((curS - target ) % p ) is not None:
                res = min(res , i - dic.get((curS-target) % p))
            dic[curS] = i
        return res if res < n else -1





