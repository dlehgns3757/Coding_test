from collections import Counter

def solution(participant, completion):
    participant = Counter(participant) # {"leo": 1, "kiki": 1, "eden": 1}
    completion = Counter(completion)
    
    answer = list(participant - completion) # Counter 모듈 - 연산
    
    return answer[0]

if __name__ == '__main__':
    participant = ["leo", "kiki", "eden"]
    completion = ["eden", "kiki"]
    
    solution(participant, completion)