import itertools
import re

def isPrime(a):
    if(a<2):
        return False
    for i in range(2,a):
        if(a%i==0):
            return False
    return True

def solution(numbers):
    num = []
    all_com = []
    new = []
    cnt = 0
    
    for n in numbers:
        num.append(int(n))
        
    for i in range(len(num)):
        for j in list(itertools.permutations(num, i+1)):
            j = str(j)
            characters = ")(, "
            j = ''.join( x for x in j if x not in characters)
            all_com.append(re.sub(", ","",str(j)))
    
    for a in all_com:
        new.append(int(a))
    
    new = list(set(new))
    print(new)
    
    for a in new:
        if isPrime(a):
            cnt += 1
    
    return cnt