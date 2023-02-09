# 회문 여부 구별
def palindrome(pstr):
    if len(pstr) <= 1:
        return True

    if pstr[0] != pstr[-1]:
        return False

    return palindrome(pstr[1:len(pstr)-1])  # 양 끝을 판단 후 리스트 크기를
                                            # 계속 줄여줌


str_array = ['안녕', '메롱메', '살금 살금', '야 너 이번주 주번이 너야']
for test in str_array:
    test = test.lower().replace(' ','')
    print(palindrome(test))