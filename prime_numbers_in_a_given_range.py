N,Q = input("enter a number: ").split()
N=int(N)
Q=int(Q)
           
  
for i in range(N,Q+1):
    if i>1:
        for j in range(2,i):
            if (i%j)== 0:
                break
        else:
            print(i)

    
