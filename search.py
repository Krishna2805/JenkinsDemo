def Search():
    arr = (10,15,20,25,30,35,40)
    key = 25
    beg = 0
    end = len(arr)-1

    while(beg!=end):
        mid = int((beg+end)/2)

        if(arr[mid] == key):
            print("Key found")
            return
        elif(arr[mid] > key):
            beg = mid + 1;
        else:
            end = mid-1;

    print("Key not found")  

Search()
