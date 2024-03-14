def check(arr) :
    l=len(arr)
    c1 = 0
    c2 = max(arr)
    for i in range(l-1) :
        c1 = abs(arr[i]-arr[i+1])
        if(c1>c2):
            print(c1,c2)
            return False
        c2 = c1 
    return True 



num = str(input("Enter the numbers :"))
arr = [int(i) for i in num.split(" ")]
print(check(arr))
