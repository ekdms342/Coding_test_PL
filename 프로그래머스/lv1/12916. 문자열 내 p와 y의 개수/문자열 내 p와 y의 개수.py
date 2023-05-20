def solution(s):
    answer = True
    
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    p_len = s.count('p') + s.count('P')
    y_len = s.count('y') + s.count('Y')

    if p_len == y_len :
        answer = True
    else :
        answer = False
        
    return answer