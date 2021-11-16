def insertion_sort(list):
    for i in range (1,len(list)):
        key=list[i]
        j=i-1
        while j>=0 and list[j]>key:
            list[j+1]=list[j]
            j-=1
        list[j+1]=key
    


if __name__ == "__main__":
    list=[]
    no=int(input("enter the len list :"))
    for i in range(int(input("enter the len list :"))):
        num=int(input("enter the number to be sorted :"))
        list.append(int(input("enter the number to be sorted :")))
    insertion_sort(list)
    print ("Sorted array is:")
    for i in range(len(list)):
     print (list[i])

