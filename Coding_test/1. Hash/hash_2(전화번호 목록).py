def solution(phone_book):
    phone_book = sorted(phone_book)
    
    for pb, pre in zip(phone_book, phone_book[1:]):
        if pre.startswith(pb): # pre안에 pb로 시작하는 문자열이 있는가
            return False
    return True

if __name__ == '__main__':
    phone_book = ["119", "97674223", "1195524421"]

    print(solution(phone_book))