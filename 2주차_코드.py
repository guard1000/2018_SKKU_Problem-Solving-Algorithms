#1번
print('12345678','홍길동')
print('12345678'+'홍길동')
print('홍길동'*3)

#2번
print (6+4,6-4,6*4,6/4,6//4,6%4)
print((10.3*5.0-4.2*3)/(19.5+2.7))

#3번
print('둘레:',3.2*2+5.7*2)
print('넓이:',3.2*5.7)

#input
a = int(input('a: '))
b = int(input('b: '))
print(a+b)


#4번
w=float(input('가로를 입력하세요 : '))
l=float(input('세로를 입력하세요 : '))
print('가로', w, '세로', l, '인 직사각형 둘레는',(w+l)*2, '넓이는', w*l)

#과제
kor = int(input('국어점수: '))
eng = int(input('영어점수: '))
mat = int(input('수학점수: '))
print('평균은', (kor+eng+mat)/3)
