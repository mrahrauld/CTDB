import json
import string

def Ex1(N):
    for i in range(0, pow(2,N)) :
        print(binary(i,N))   
def binary(i,N):
    bin = [0]*N #initialize a list of N zeros
    for j in range(0,N): # loop to fill every position, begin with the biggest
        # if the number is bigger than 2^a, then the corresponding bit equals 1 and we subtract 2^a
        if i//pow(2,N-(j+1)) == 1:
            bin[j] = 1
            i -=pow(2,N-(j+1))
    return bin
    

Ex1(3)
