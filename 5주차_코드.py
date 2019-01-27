#1 윤년
year=int(input())
if year%400==0:
    print("윤년")
elif year%4==0 and year%100!=0:
    print("윤년")
else:
    print("윤년 아님")

#2 자릿수 판단
num=int(input())
if num>=100:
    print("세 자리")
elif num>=10:
    print("두 자리")
else:
    print("한 자리")

#실습 과제
num2=int(input())
if (num2//100)==(num2%10):
    print("회문")
else:
    print("회문 아님")
