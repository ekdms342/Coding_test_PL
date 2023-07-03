def solution(phone_book):
    answer = True
    for cn in range(0,len(phone_book),1):
        check_number = phone_book[cn]
        for i in range(cn + 1,len(phone_book),1):
            if phone_book[i][0:len(check_number)] == check_number or check_number[0:len(phone_book[i])] == phone_book[i]:
                answer = False
                break
                
        if answer == False :
            break
            
    return answer
