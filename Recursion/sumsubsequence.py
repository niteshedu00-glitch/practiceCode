# def subs(i, arr,ds,n,s, target):
#     if i == n:
#         if s == target:
#             print(ds)
#         return

#     ds.append(arr[i])
#     subs(i+1, arr,ds, n,s+arr[i],target)

#     ds.pop()
#     subs(i+1,arr,ds, n,s,target)



# arr = [1,2,1]
# n = len(arr)
# target = 2
# subs(0, arr, [], n , 0,target)


# modife only print one output

# def subs(i, arr,ds,n,s, target):
#     if i == n:
#         if s == target:
#             print(ds)
#             return True
#         return False

#     ds.append(arr[i])
#     if subs(i+1, arr,ds, n,s+arr[i],target) == True:
#         return True

#     ds.pop()
#     if subs(i+1,arr,ds, n,s,target) == True:
#         return True
#     return False



# arr = [1,2,1]
# n = len(arr)
# target = 2
# subs(0, arr, [], n , 0,target)



# now we have to print only how many count are find the value 

def subs(i, arr,n,s, k):
    if i == n:
        if s == k:
            return True
        return False
        

    pick = subs(i+1, arr,n,s + arr[i],k)

    not_pick = subs(i+1, arr,n,s,k)

    return pick + not_pick


arr = [1,2,1]
n = len(arr)
k = 2
print(subs(0, arr,n , 0,k))