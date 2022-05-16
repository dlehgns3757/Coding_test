def cluster(res): 
    answer = []
    cnt = 1
    head = res[0]
    
    for i in range(1, len(res)):
        if head >= res[i]:
            cnt += 1
        else:
            head = res[i]
            answer.append(cnt)
            cnt = 1
            
    answer.append(cnt)
                
    return answer
    
def solution(progresses, speeds):
    for_100 = []
    
    for p, s in zip(progresses, speeds):
        k = 0
        
        while True:
            if p >= 100:
                break
            p += s
            k += 1
            
        for_100.append(k)
        
    return cluster(for_100)