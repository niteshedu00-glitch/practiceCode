def combination(i, ds, arr,target):
    if target ==0:
        return [ds.copy()]
    if i == len(arr) or target < 0 :
        return []
    result = []
    ds.append(arr[i])
    result += combination(i,ds,arr, target-arr[i])
    ds.pop()
    result += combination(i+1,ds,arr,target)
    return result




arr = [2,3,6,7]
target = 7
print( combination(0, [],arr,target))

