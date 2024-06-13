def binary_search_insertion_simple(nums:list[int],target):
    """二分查找插入点且没有重复元素"""
    i,j=0,len(nums)-1 #初始化双闭区间
    while i <=j:
        m=(i+j)//2
        if nums[m]<target:
            i=m+1
        elif nums[m]>target:
            j=m-1
        else:
            return m
    return -1#没有找到插入点

def binary_search_insertion(nums:list[int],target):
    i,j=0,len(nums)-1
    while i<=j:
        m=(i+j)//2
        if nums[m]<target:
            i=m+1
        elif nums[m]>target:
            j=m-1
        else:
            j=m-1
    return i
""""
代码说明:
因为i,j不断靠近target
然后因为如果碰到相等的需要看的是i的右边全部都是比target都大的数才行
否则j会一直向i的方向移动,直至j移动到了右边,就是找左边界
"""
def binary_search_insertion_right(nums:list[int],target):
    i,j=0,len(nums)-1
    while i<=j:
        m=(i+j)//2
        if nums[m]<target:
            i=m+1
        elif nums[m]>target:
            j=m-1
        else:
            i=m+1
    return i

nums=[2,4,5,7,9,10,10,10,10,11,17]
print(binary_search_insertion_right(nums,10))
