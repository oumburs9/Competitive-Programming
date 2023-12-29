class Solution:
    def smallestNumber(self, num: int) -> int:
        rev = False
        zeros = 0
        nums = []

        # tracking if the number is +ve or -ve and making +ve if -ve
        if num < 0:
            rev = True
            num = -num

        # spliting to the list of str and tracking the number of zeros
        for i in str(num):
            nums.append(i)
            if i =='0':
                zeros += 1
        # sorting depending on the rev
        nums.sort(reverse=rev)

        # joining the answer accordingly
        if rev == True:
            ans =  ''.join(nums)
            return -int(ans)
        else:
            while zeros > 0:
                nums.pop(0)
                nums.insert(zeros,'0')
                zeros -= 1
            return int(''.join(nums))
        
        