import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville) # 배열을 heap 구조로 변경
    
    while scoville[0] < K:
        if len(scoville) == 1:
            return -1
        
        first_min = heapq.heappop(scoville) # 자료구조 heap의 pop
        second_min = heapq.heappop(scoville)
        mix_scoville = first_min + second_min * 2
        
        heapq.heappush(scoville, mix_scoville)
        answer += 1   
        
    return answer

if __name__ == '__main__':
    scoville = [1, 2, 3, 9, 10, 12]
    K = 7
    
    print(solution(scoville, K))