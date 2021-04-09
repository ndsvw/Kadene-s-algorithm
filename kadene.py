# O(n) time, O(n) auxiliary space
def maxSubArraySum(a):
    if len(a) == 0:
        raise Exception("length of input array must be > 0")
    arr = [0] * len(a)
    arr[0] = a[0]
    for i in range(1, len(a)):
        arr[i] = max(a[i], arr[i-1] + a[i])
    return max(arr)
    
# O(n) time, O(1) auxiliary space
def maxSubArraySumSpaceImproved(a):
    if len(a) == 0:
        raise Exception("length of input array must be > 0")
    highest = a[0]
    cur = a[0]
    for i in range(1, len(a)):
        cur = max(a[i], cur + a[i])
        highest = max(cur, highest)
    return highest