def binary_search(nums:list[int],target:[int])->int:
    """二分查找,双闭区间"""
    i,j=0,len(nums)-1#初始化指针
    while i<=j:
        m=(i+j)//2
        if nums[m]<target:
            i=m+1
        elif nums[m]>target:
            j=m-1
        else:
            return m
    return -1

def binary_search_lrco(nums:list[int],target:[int])->int:
    """二分查找,左闭右开"""
    i,j=0,len(nums)#初始化指针
    while i<=j:
        m=(i+j)//2
        if nums[m]<target:
            i=m+1
        elif nums[m]>target:
            j=m#此处微调即可
        else:
            return m
    return -1