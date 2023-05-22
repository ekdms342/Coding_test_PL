def solution(s):
    answer = "".join(s for s in sorted(s,reverse = True))
    return answer