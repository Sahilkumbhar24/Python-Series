def binary_search(arr,target):
    low,high = 0,len(arr)-1
    while(low<=high):
        mid=(low+high)//2
        if(arr[mid]>target):
            high=mid-1
        elif(arr[mid]<target):
            low=mid+1
        else:
            return mid
    return -1
print(binary_search((2,5,7,9,15,20,46) ,  15 ))  
 #   index -         0 1 2 3 4  5  6  Target                