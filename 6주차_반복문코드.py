#1. for문 사용
sum = 0

for i in range(0,4):
    sum += int(input('정수를 입력하세요: '))

print('합계는 %d 입니다' %sum)


#1-2. while문 사용
count=0
sum=0
while count < 4:
    sum += int(input('정수를 입력하세요: '))
    count = count+1

print('합계는 %d 입니다' %sum)


#2. for문 사용
num = int(input('원하는 단을 입력하세요 : '))

for i in range(1,10):
    print('%d x %d = %d' %(num, i, num*i))

#2-2. while문 사용
num = int(input('원하는 단을 입력하세요 : '))
i = 1
while i < 10:
    print('%d x %d = %d' %(num, i, num*i))
    i = i+1


#3.
for i in range(1, 7, 1):
    for j in range(1, i+1, 1):
        print(j,end = ' ')
    print('')

print('\n')

for i in range (7, 1, -1):
    for j in range(1, i, 1):
        print(j,end = ' ')
    print(' ')


for i in range(7, 0, -1):
    for j in range(1,7, 1):
        if j < i:
            print(' ', end =' ')
        else:
            print(j-i+1, end = ' ')
    print(' ')

print('\n')
        


for i in range(1, 7, 1):
    for j in range (1, 7, 1):
        if j< i:
            print(' ', end=' ')
        else:
            print(j-i+1, end = ' ')
    print(' ')


#이중포문 약식

    
for i in range(1,5):
    for j in range(1,i+1):
        print(j, end = ' ')
    print(' ')

print('\n')

for i in range(1,5):
    for j in range(1,5):
        if j< i:
            print(' ', end=' ')
        else:
            print(j, end = ' ')
    print(' ')

