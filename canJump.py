
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #print(nums, len(nums))
        if len(nums) <= 1:
            return True
        
        max_reach = nums[0]
        i = 0 
        if max_reach >= len(nums)-1:
            return True

        while i <= max_reach:
            # print("cur_jump: ", x+1, len(nums))
            
            if i + nums[i] > max_reach:
                max_reach = i + nums[i]
            if max_reach >= len(nums)-1:
                return True

            i+=1

        # print("exiting", num_jumps)
        return False


x = Solution()
print (x.canJump([2,3,1,1,4]))
print (x.canJump([3,2,1,0,4]))
print (x.canJump([2,0,0]))

