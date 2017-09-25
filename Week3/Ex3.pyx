
        
cdef int tot, i, j
j = 0
while j<1000:
    tot=0   
    i=1
    while i<=10000:
        tot+=1/(i**2)
        i+=1
    j+=1
print('finish')