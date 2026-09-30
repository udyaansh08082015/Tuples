def palind(r):
    s= 0
    e= len(r) -1
    while (e>s):
        if(r[s] != r[e]):
            return False
        s+= 1
        e-= 1
    return True

tupleX = (1,2,3,4,5,6,6,5,4,3,2,1,)

if (palind(tupleX)):
    print("It is a Flip-Flop!")
else:
    print("It is not a Flip-Flop")    

        
