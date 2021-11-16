def sort(nums):
    for j in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j]>nums[j+1]:
             nums[j],nums[j+1]=nums[j+1],nums[j]          
    print("list after sorting:",nums)


if __name__=="__main__":
    nums=[]
    for i in range(int(input("enter the length of the list :"))):
        nums.append(int(input("enter the numbers in the list :")))
    print("list before sorting :",nums)
    sort(nums)