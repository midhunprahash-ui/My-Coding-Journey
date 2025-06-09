def push_zeros_to_end(arr):
    count=0
    for i in range(len(arr)):
        if(arr[i]!=0):
            arr[count]=arr[i]
            count+=1
    while(count<len(arr)):
        arr[count]=0
        count+=1
if __name__=="__main__":
    arr=[456,67,0,67,0,45,0,0,78,68,0,567,0,467,567,0,875,0]
    print(push_zeros_to_end(arr))

