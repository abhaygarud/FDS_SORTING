def merge_sort(list1):
    if len(list1)>1:
        left_list1=list1[:len(list1)//2] #loop will run from 0 index till mid of left side
        right_list1=list1[len(list1)//2:]   #lop will run till mid of right to end of the list          
   
    #recursion
        merge_sort(left_list1) 
        merge_sort(right_list1)
            
        i=j=k=0
        #loop will run till the len of list in bigger than i and j
        while i<len(left_list1) and j<len(right_list1): 
            if left_list1[i]<right_list1[j]:
                list1[k]=left_list1[i]
                i+=1
            else:
                list1[k]=right_list1[j]
                j+=1
            k+=1

        while i<len(left_list1):
            list1[k]=left_list1[i]
            i+=1
            k+=1
        while j<len(right_list1):
            list1[k]=right_list1[j]
            j+=1
            k+=1
if __name__=="__main__":
    list1=[]
    for i in range(int(input("enter the lenght of arr :"))):
        list1.append(int(input("entr the random number")))
    print(list1)

    merge_sort(list1)
    print(list1)
        
"""

list1=[3,7,1,8,4,12]
first divide the araay in 2 parts left and right
divdii till we get the index  value 1
once it get divide
check left side with right side
if left is smaller apend it in lisr1
else append right list
"""







