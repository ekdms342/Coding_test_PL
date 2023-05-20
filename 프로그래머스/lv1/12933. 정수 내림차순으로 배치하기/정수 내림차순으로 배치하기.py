def solution(n):
    answer = ''
    n = sorted(list(int(i) for i in str(n)) , reverse = True)
    for i in n :
        answer += str(i)
    answer = int(answer)
    return answer