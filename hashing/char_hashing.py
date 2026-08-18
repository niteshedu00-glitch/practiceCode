def char_hashing(s):
    hash_table = [0] * 128

    for char in s:
        hash_table[ord(char)] += 1

    return hash_table


s= input("Enter stringd")

hashtable = char_hashing(s)

q = int(input())
for _ in range(q):
    ch = input()
    print(hashtable[ord(ch)])

