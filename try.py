arrM = [0,1,2,3,4,6,7,8,9,10,11,12,13,14,16,17,18,19,20,23,26,28,37,46,58,788]

def binStart(arr, what):
    binSearch(arr, 0, len(arr) - 1, what)

def binSearch(arr, l, r, what):
    if(r >= l):
        mid = ((r - l) / 2) + 1
        if(what == arr[mid]):
            print str(what) + " " + str(arr[mid])
            return 0
        elif(what > arr[mid]):
            binSearch(arr, mid + 1, r, what)
        elif(what < arr[mid]):
            binSearch(arr, l, mid - 1, what)
    else:
        print("It's not in here")

print("Binary Search?")
binStart(arrM, 4)
#binStart(arrM, 7)
binStart(arrM, 5)
#binStart(arrM, 788)
#binStart(arrM, 25)
