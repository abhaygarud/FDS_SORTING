#list=[3,7,1,5,2]
#wiht the help of selection sort sort the element
#pass 1
#list index = 0 1 2 3 4
#list   =    [3|,7,1,5,2]
              #i=3<<minmum
              #i<list[index]
              #swap i with<list[index]

def selection_sort(list):
    for i in range(0,len(list)):
        mim_index=i
        for j in range(i,len(list)):
            if list[mim_index]>list[j]:
                mim_index=j
        #code for swaping the mim value
        list[i],list[mim_index]=list[mim_index],list[i]

    
    print(list)

if __name__ == "__main__":
    list=[]
    for i in range(int(input("enter the range of the list:"))):
        list.append(int(input("enter the value for sorting :")))
    print(list)
    selection_sort(list)
  