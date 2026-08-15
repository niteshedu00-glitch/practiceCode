def subs(ind, ds, arr, n):
    if ind >= n:
        print(ds)
        return

    ds.append(arr[ind])
    subs(ind+1, ds, arr,n)

    ds.pop()
    subs(ind+1, ds, arr, n)


arr = [3,1,2]
n = len(arr)

subs(0, [], arr, n )