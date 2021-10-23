import re
# ca?e
# case, cafe


def print_match(m):
    if m:
        print(m.group())  # group() : 매칭되는 내용을 알려준다.
        print(m.string)  # string() : 매칭되는 내용을 알려준다.
        print(m.start())  # start() : 매칭되는 내용을 알려준다.
        print(m.end())  # end() : 매칭되는 내용을 알려준다.
        print(m.span())  # span() : 매칭되는 내용을 알려준다.
    else:
        print("매칭되지 않음")


p = re.compile("ca.e")
m = p.search("good care")  # search : 문자열 중 일치하는게 있나 확인
print_match(m)
# lst = p.findall("careless")  # findall : 일치하는 모든것 리스트로 반혼
