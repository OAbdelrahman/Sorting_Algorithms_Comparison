import random
from time import time

def mergeSort(A):
    if len(A) < 2:
        return A[:]
    
    else:
        mid = len(A)//2
        left = mergeSort(A[:mid])
        right = mergeSort(A[mid:])

        return merge(left, right)

def merge(A, B):
    out = []
    i, j = 0, 0

    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            out.append(A[i])
            i+=1
        
        else:
            out.append(B[j])
            j+=1

    while i < len(A):
        out.append(A[i])
        i+=1
    
    while j < len(B):
        out.append(B[j])
        j+=1
        
    return out


def insertSort(A):
    n = len(A)
    for i in range(1, n):
        key= A[i]
        j = i-1

        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            j = j-1
        
        A[j+1] = key
    
    return A

def bubbleSort(A):
    n = len(A)

    for i in range(n):
        for j in range(0, n-i-1):
            if A[j]>A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]

    return A

def main ():
    n= [i for i in range(100, 5001, 1000)]

    print("N\tMerge\tInsert\tBubble")
    for i in n:
        A = [j for j in range(i)]

        random.shuffle(A)
        t1 = time()
        B = mergeSort(A)
        t2 = time()
        mtime = (t2-t1)*1000
        
        random.shuffle(A)
        t1 = time()
        C = insertSort(A)
        t2 = time()
        itime = (t2-t1)*1000
        
        random.shuffle(A)
        t1 = time()
        D = bubbleSort(A)
        t2 = time()
        btime = (t2-t1)*1000
        
        print(f"{i}\t{mtime:.2f}\t{itime:.2f}\t{btime:.2f}")




if __name__ == "__main__":
    main()
