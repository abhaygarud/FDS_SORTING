def swap(a,b,arr):
    if a!=b:
      l1[a],l1[b]=l1[b],l1[a]

def quick_sort(l1,i,j):
    if i < j:
        p1 = partition(l1,i,j)
        quick_sort(l1,i,p1-1)
        quick_sort(l1,p1+1,j)


def partition(l1,i,j):
    pivot_index = i
    pivot = l1[pivot_index]
  
    while i < j:
        while i < len(l1) and l1[i] <= pivot:
            i += 1
        while l1[j] > pivot:
            j -= 1
        if i < j:
            swap(i,j,l1)
    swap(pivot_index,j,l1)
    return j


if __name__ == "__main__":
    l1 = []
    for i in range(int(input("enter the lenght of arr :"))):
        l1.append(int(input("entr the random number")))
    print(l1)
    quick_sort(l1,0,len(l1)-1)
    print(l1)

