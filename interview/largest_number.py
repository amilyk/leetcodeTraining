from functools import cmp_to_key

class solution:
    def largestNumber(self, nums):
        def cmp(a, b):
            return int(a+b)-int(b+a)
        nums_s = list(map(str, nums))
        nums_s.sort(key=cmp_to_key(cmp),reverse=True)
        # print(nums_s)
        s = ''.join((nums_s))
        s = s.lstrip("0")
        if len(s) == 0:
            return "0"
        return s
    
if __name__ == "__main__":
    nums = [3,0,7,5,9]
    solu = solution()
    print(solu.largestNumber(nums))
