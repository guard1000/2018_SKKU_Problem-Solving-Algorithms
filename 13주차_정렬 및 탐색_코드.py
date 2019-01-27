
'''
#삽입 정렬
def InsertionSort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i
        while j > 0 and data[j-1] > data[j]:
            data[j-1], data[j] = data[j], data[j-1]
            j = j-1
        print(data)


data = [1, -4.5, 10.6, 4.5, 92, 84, 18, 32]
InsertionSort(data)
'''

#선택 정렬
def SelectionSort(data):
    for i in range(0, len(data)-1):
        j=i+1
        while(j < len(data) and data[i] > data[j]):
            data[i],data[j] = data[j],data[i]
            j = j+1
    print(data)

data = [1, -4, 10, 4, 92, 84, 18, 32, -58, 100]
SelectionSort(data)


"""
#3
flag = 0
length = 0
count = 0

while(True):
    num = int(input('숫자를 입력하세요(0을 입력시 종료): '))
    if num ==0:
        break
    elif num == 7 and flag == 0:
        flag =1
    elif num == 7 and flag == 1:
        if length < count:
            length = count
            count = 0
    elif num != 7 and flag == 1:
        count = count+1

print('최대길이는',length+1)
"""

"""
#과제
def draw(num):
    for i in range(1,num+1):
        print ("  "*(num-i), end=" ")
        for j in range(i,0,-1):
            print(j, end=" ")
        for j in range(1, i, 1):
            print(j+1, end=" ")
        print(" ")

n = int(input("1~15사이의 줄 수를 입력하세요.: "))
draw(n)
"""         
