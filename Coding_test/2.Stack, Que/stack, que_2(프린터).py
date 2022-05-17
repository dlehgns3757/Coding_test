from collections import deque

def solution(priorities, location):
    priorities = [(v, i) for i, v in enumerate(priorities)]
    priorities = deque(priorities)
    answer = 0
    
    while True:
        J = priorities.popleft()
        
        if priorities and max(priorities)[0] > J[0]:
            priorities.append(J)
        else:
            answer += 1
            if J[1] == location:
                return answer