def hashing(arr,queries ):
    hash_table= [0]*13

    #precompute
    for number in arr:
        hash_table[number] += 1

    #fetch
    print("here is the ansewer")
    for number in queries:
        print(hash_table[number])
    



n = int(input(()))
arr = list(map(int,input().split()))

q = int(input())
queries = []

for _ in range(q):
    queries.append(int(input()))

hashing(arr,queries)


    