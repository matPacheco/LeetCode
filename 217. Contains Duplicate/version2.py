# Tried to make a different version, but it times out on LeetCode
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        found_equal = False

        nums_dict = {}

        for n in nums:
            if n in nums_dict.keys():
                found_equal = True
                break
            else:
                nums_dict[n] = True

        return found_equal
