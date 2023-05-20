def solution(x, n):
    answer = []
    num = x
    answer = list(map(lambda x: x*num, range(n+1)))[1:]
    return answer