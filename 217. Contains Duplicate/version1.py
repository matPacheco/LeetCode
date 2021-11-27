class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        # Aux variables
        last = None
        found_equal = False

        nums.sort()

        for n in nums:
            if n == last:
                found_equal = True
                break
            last = n

        return found_equal
