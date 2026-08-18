class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s_list = sorted(nums)
        result = []
        for i in range(len(s_list)):
            if i > 0 and s_list[i] == s_list[i-1]:      
                continue
            left, right = i+1, len(s_list)-1
            while left < right:
                total = s_list[i] + s_list[left] + s_list[right]
                if total == 0:
                    result.append([s_list[i], s_list[left], s_list[right]])
                    left += 1
                    right -= 1
                    while left < right and s_list[left] == s_list[left-1]:   
                        left += 1
                    while left < right and s_list[right] == s_list[right+1]: 
                        right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        return result


        