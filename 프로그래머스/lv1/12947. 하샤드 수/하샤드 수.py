def solution(x):
    answer = True
    num = str(x)
    sum_all = 0
    for i in num:
        sum_all += int(i)
        
    if x % sum_all == 0 :
        answer = True
    else : 
        answer = False
    
    return answer