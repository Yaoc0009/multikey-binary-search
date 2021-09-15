import random

# algorithm for searching positions of values closest and greater than 3 targets
def binarySearch(arr, l, r, x):
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            r = mid - 1
        else:
            l = mid + 1
    # check that value at r is greater not smaller
    if arr[r] < x: r += 1
    return r
    
def binarySearch2key(arr, l, r, keys):
    keys = sorted(keys)
    k1, k2 = keys[0], keys[1]
    pos1, pos2 = 0, 0
    # Check base case
    if l <= r:
        mid = l + (r - l) // 2
        if arr[mid] < k1:
            pos1, pos2 = binarySearch2key(arr, mid + 1, r, [k1, k2])
        elif arr[mid] == k1:
            pos1 = mid
            pos2 = binarySearch(arr, mid + 1, r, k2)
        elif arr[mid] > k1 and arr[mid] < k2:
            pos1 = binarySearch(arr, l, mid - 1, k1)
            pos2 = binarySearch(arr, mid + 1, r, k2)
        elif arr[mid] == k2:
            pos1 = binarySearch(arr, l, mid - 1, k1)
            pos2 = mid
        elif arr[mid] > k2:
            pos1, pos2 = binarySearch2key(arr, l, mid - 1, [k1, k2])
    # check that value at pos is greater not smaller
    if arr[pos1] < k1: pos1 += 1 
    if arr[min(len(arr) - 1, pos2)] < k2: pos2 += 1
    return pos1, pos2

def binarySearch3Key(arr, l, r, keys):
    keys = sorted(keys)
    k1, k2, k3 = keys[0], keys[1], keys[2]
    pos1, pos2, pos3 = 0, 0, 0
    # Check base case
    if l <= r:
        mid = l + (r - l) // 2
        if arr[mid] < k1:
            pos1, pos2, pos3 = binarySearch3Key(arr, mid + 1, r, [k1, k2, k3])
        elif arr[mid] == k1:
            pos1 = mid
            pos2, pos3 = binarySearch2key(arr, mid + 1, r, [k2, k3])
        elif arr[mid] > k1 and arr[mid] < k2:
            pos1 = binarySearch(arr, l, mid - 1, k1)
            pos2, pos3 = binarySearch2key(arr, mid + 1, r, [k2, k3])
        elif arr[mid] == k2:
            pos1 = binarySearch(arr, l, mid - 1, k1)
            pos2 = mid
            pos3 = binarySearch(arr, mid + 1, r, k3)
        elif arr[mid] > k2 and arr[mid] < k3:
            pos1, pos2 = binarySearch2key(arr, l, mid - 1, [k1, k2])
            pos3 = binarySearch(arr, mid + 1, r, k3)
        elif arr[mid] == k3:
            pos1, pos2 = binarySearch2key(arr, l, mid - 1, [k1, k2])
            pos3 = mid
        elif arr[mid] > k3:
            pos1, pos2, pos3 = binarySearch3Key(arr, l, mid - 1, [k1, k2, k3])
    # check that value at pos is greater not smaller
    if arr[pos1] < k1: pos1 += 1 
    if arr[pos2] < k2: pos2 += 1
    if arr[min(len(arr) - 1, pos3)] < k3: pos3 += 1  # prevent value larger than length
    return pos1, pos2, pos3
  
  if __name__ == "__main__":
    ls = list(range(1000))
    target = list(random.sample(ls, 3))
    # pos1 = -1 if target less than lowest val
    # pos3 = len(ls) if target more than highest val
    pos1, pos2, pos3 = binarySearch3Key(ls, 0, len(ls) - 1, target)
    print(pos1, pos2, pos3)
