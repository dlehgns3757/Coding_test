import itertools
import re

# 소수 구하는 함수
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
        for j in list(itertools.permutations(num, i+1)): # permutations로 모든 순열 생성
            j = str(j)
            characters = ")(, "
            j = ''.join( x for x in j if x not in characters) # permutations는 튜플을 반환하기 때문에 문자열로 변환 후 불필요한 문자 제거 
            all_com.append(re.sub(", ","",str(j)))
    
    for a in all_com:
        new.append(int(a))
    
    new = list(set(new))
    print(new)
    
    for a in new:
        if isPrime(a):
            cnt += 1
    
    return cnt

if __name__ == '__main__':
    numbers = "17"
    
    solution(numbers)
