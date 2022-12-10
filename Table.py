class Table:
    def __init__(self,a):

        for i in range(2,a+1):
            print("This is tble of:",i)
            for j in range(1,11):
                print(i,"x","%2d"%(j),"=","%2d"%(i*j))
            print(" ")    
a=int(input("Enter the no.: "))
member=Table(a)


