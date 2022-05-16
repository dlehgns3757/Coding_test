def solution(clothes):
    wear = {}
    answer = 1

    for c in clothes:
        wear[c[1]] = []
        
    for c in clothes:
        wear[c[1]].append(c[0])
    
    for k in wear.keys():
        answer = answer * (len(wear[k]) + 1)
    
    return answer - 1