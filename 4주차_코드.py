#1
num = int(input("수를 입력하세요. :"))

if num%2 == 0:
    print('Even Number')
else:
    print('Odd Number')

#2
ganzi = ['쥐', '소', '호랑이', '토끼', '용', '뱀', '말','양', '원숭이','닭','개','돼지']

y = int(input('연도를 입력하세요. : '))
if (y%12==4):
    print('%d년생은 쥐띠입니다.'%y)
elif (y%12==5):
    print('%d년생은 소띠입니다.'%y)
elif (y%12==6):
    print('%d년생은 호랑이띠입니다.'%y)
elif (y%12==7):
    print('%d년생은 토끼띠입니다.'%y)
elif (y%12==8):
    print('%d년생은 용띠입니다.'%y)
elif (y%12==9):
    print('%d년생은 뱀띠입니다.'%y)
elif (y%12==10):
    print('%d년생은 말띠입니다.'%y)
elif (y%12==11):
    print('%d년생은 양띠입니다.'%y)
elif (y%12==0):
    print('%d년생은 원숭이띠입니다.'%y)
elif (y%12==1):
    print('%d년생은 닭띠입니다.'%y)
elif (y%12==2):
    print('%d년생은 개띠입니다.'%y)
else:
    print('%d년생은 돼지띠입니다.'%y)

#2-1.
ganzi = ['쥐', '소', '호랑이', '토끼', '용', '뱀', '말','양', '원숭이','닭','개','돼지']
y = int(input('연도를 입력하세요. : '))
#print(ganzi[(y-4)%12]))
print('%d년생은 %s띠입니다.' %(y,ganzi[(y-4)%12]))


#3
k = float(input('키(m)를 입력하세요. : '))
m = int(input('몸무게(kg)를 입력하세요. : '))

bmi= m/(k*k)

if (bmi < 18.5):
    print('저체중 입니다.')
elif bmi>=18.5 and bmi<23.0:
    print('정상체중 입니다.')
elif bmi>=23.0 and bmi<25:
    print('위험증가 입니다.')
else:
    print('비만 입니다.')


#과제

a = int(input('첫번째 정수 : '))
b = int(input('두번째 정수 : '))
c = int(input('세번째 정수 : '))

print('입력:',a,b,c)

if a>b:
    a,b = b,a
if b>c:
    b,c = c,b
if a>b:
    a,b = b,a

print('오름차순 : ',a,b,c)




#힌트

a = 10
b = 5
print(a,b) #변경 전 값 확인

a,b = b,a  #치환문 사용 값이 바뀜
print(a,b) #변경 후 값 확인


