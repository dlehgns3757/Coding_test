def solution(n, lost, reserve):
    # 여벌 체육복을 도난당했을때
    lost_ = set(lost) - set(reserve)
    reserve_ = set(reserve) - set(lost)
    
    for r in reserve_:
        if r-1 in lost_: # 앞사람 빌려줄때
            lost_.remove(r-1)
        elif r+1 in lost_: # 뒷사람 빌려줄때
            lost_.remove(r+1)
                
    return n - len(lost_)
    
if __name__ == '__main__':
    n = 5 # 총 학생수
    lost = [2, 4] # 잃어버린 친구들
    reserve = [1, 3, 5] # 여벌이 있는 친구들
    
    solution(n, lost, reserve)