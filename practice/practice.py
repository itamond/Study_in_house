from random import *

date = randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월 " +str(date)+ "일로 선정되었습니다")

sentence = "나는 소년입니다"
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """
나는 소년이고 미남이다"""
print(sentence3)

jumin =  "990120-1234567"

print("성별 : " + jumin[7])
print("연 : " +jumin[0:2]) # 0 부터 2 직전까지
print("월 : " +jumin[2:4])
print("일 : " +jumin[4:6])
print("생년월일 : " +jumin[:6]) # 처음부터 6 직전까지
print("뒤 7자리 : " +jumin[7:]) # 7 부터 끝까지
print("뒤 7자리 (뒤에부터) : " +jumin[-7:])
# 맨 뒤에서 7번째부터 끝까지

#문자열 처리 함수

python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python", "Java"))

index = python.index("n")
print(index)
index = python.index("n", index + 1)
print(index)

print(python.find("Java"))
#print(python.index("Java"))
print("hi")

print(python.count("n"))

#문자열 포멧
print("a"+"b")
print("a","b")

# 방법 1
print("나는 %d살입니다." % 20)
print("나는 %s을 좋아해요." % "파이썬")
print("Apple 은 %c로 시작해요." %"A")
# %s
print("나는 %s살입니다." % 20)
print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))
print("나는 {}살입니다.".format(20))
print("나는 {0}색과 {1}색을 좋아해요." .format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요." .format("파란", "빨간"))

# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요." .format(age=20, color="빨간"))

# 방법 4
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")

# \n :  줄바꿈
#print("백문이 불여일견\n백견이 불여일타")


#print('저는 "나도코딩"입니다.')
#print("저는 \"나도코딩\"입니다.")

# \\ : 문장 내에서 \
print("C:\\Users\\배환희\\Desktop\\PythonWorkspace>")

# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine")

# \b : 백스페이스(한 글자 삭제)
print("Redd\bApple")
# \t : 탭
print("Red\tApple")


url = "http://daum.net"
my_str = url.replace("http://", "")
my_str = my_str[:my_str.index(".")]
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0} 의 비밀번호는 {1} 입니다.".format(url, password))