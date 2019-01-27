 #1
def ormchasun(x,y,z):
    if x>y:
        x,y = y,x
    if y>z:
        y,z = z,y
    if x>y:
        x,y = y,x
    print(x,y,z)
    
a = int(input('첫번째 정수 : '))
b = int(input('두번째 정수 : '))
c = int(input('세번째 정수 : '))

print('입력:',a,b,c)
print('오름차순:', end=' ')
ormchasun(a,b,c)


#2 버블정렬
def bubble_sort(data):
    for i in range(len(data)-1): #각 실행 한번 될 때 마다 가장 큰 녀석을 찾음.
        for j in range(len(data)-1): 
            if data[j]>data[j+1]:
                data[j],data[j+1] = data[j+1], data[j]
        print(data)
    return data

data = [53,27,90,16,76,31,40,55,19,15]
bubble_sort(data)


#3

def BinarySearch(data, target, low, high):  # data 리스트, 타겟, 처음과 끝을 받아 옵시다.
    if low> high:                            # 당연히 low가 high보다 크면 뭔가 잘못된거죠?
        return False
    else:                                   
        mid = (low + high) // 2             # 중간 값이 들어있는곳의 위치를 정해줍니다.
        if target == data[mid]:             # 중간 값과 타겟을 비교해서 같다면,
            print('hit')                    # hit 을 출력
            return True 
        elif target < data[mid]:            # 타겟 < 중간 값 이라면,
            print('miss')
            return BinarySearch(data, target, low, mid-1)
        else:                               # 타겟 > 중간 값 이라면,
            print('miss')
            return BinarySearch(data, target, mid+1, high)


data = [6,13,14,25,33,43,51,53,64,72,84,93,95,96,97]
BinarySearch(data, 33, 0, len(data)-1)


#과제
def Input_and_Sort():                       #10개의 숫자를 받아 정렬한 리스트를 리턴하는 함수
    a_list=[]
    for i in range(10):
        a=int(input('숫자를 입력하세요'))
        a_list.append(a)

    a_list.sort()
    return a_list


def BinarySearch(data, target, low, high):  #이진 탐색 함수
    if low>high:                            
        return False
    else:                                   
        mid = (low + high) // 2             
        if target == data[mid]:             
            print('hit')                   
            return True 
        elif target < data[mid]:            
            print('miss')
            return BinarySearch(data, target, low, mid-1)
        else:                               
            print('miss')
            return BinarySearch(data, target, mid+1, high)


data= Input_and_Sort()                      #data에 정렬된 숫자들의 리스트를 대입
print(data)                                 #정렬이 잘 되었는지 확인차 출력
target = data[3]                            #타겟은 3번 인덱스의 값
BinarySearch(data, target, 0, len(data)-1 ) 

    
    

