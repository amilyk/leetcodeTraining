import random

class Solution(object):
    def randomPartition(self, nums, low, high):
        #随机选择一个数，然后放到首位作为pivot
        i = random.randint(low, high)
        nums[low],nums[i] = nums[i], nums[low]
        return self.Partition(nums, low, high)

    def Partition(self,nums, low, high):
        #左侧比pivot小，右侧大于pivot，找到这个位置点
        i = low
        j = high
        pivot = nums[low]
        while i < j:
            #后面元素应该都是比pivot大
            while i < j and nums[j] >= pivot:
                j -= 1
            #前面元素应该都是比pivot小
            while i < j and nums[i] <= pivot:
                i += 1
            nums[i], nums[j] = nums[j], nums[i]

        #交换之后，i这个位置之前都是比pivot小，j这个位置之后都比pivot大
        nums[low], nums[i] = nums[i], nums[low]
        return i

    def QuickSort(self, nums, low, high, k, size):
        if low < high:
            pivot_i = self.randomPartition(nums, low, high)
            if pivot_i == size - k:#这里只能拿到QuickSort(3,5)
                return nums[size - k]
            elif pivot_i < size - k:
                self.QuickSort(nums, pivot_i+1, high, k, size)
            else:
                self.QuickSort(nums, low, pivot_i-1, k, size)
        #不加就没返回值QuickSort(0,n-1)
        return nums[size - k]
            
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return self.QuickSort(nums, 0, len(nums)-1, k, len(nums))

        
if __name__ == "__main__":
    solu = Solution()
    nums = [3,2,1,5,6,4]
    k = 2
    new_nums = solu.findKthLargest(nums, k)
    print(new_nums)