import turtle as t  # turtle은 기니까 t라고 부르기로 합시다.

t.shape('turtle')   # turtle 모양으로 그림을 그려요.
for i in range(3):  # 3번 반복하겠습니다. 삼각형이니까요!
    t.forward(100)  # 앞으로 100만큼 이동
    t.right(360/3)  # 오른쪽으로 360/3도 회전합니다
                    # 정n각형의 외각은 360/n도이기 때문이죠.


t.shape('turtle')
t.left(45)
for i in range(4):
    t.forward(100)
    t.right(360/4)
    
    
t.shape('turtle')
for i in range(5):
    t.forward(100)
    t.right(360/5)
    
t.shape('turtle')
for i in range(6):
    t.forward(100)
    t.right(360/6)


t.shape('turtle')
t.circle(100)


#2
import turtle as t
t.shape('turtle')
t.color('red')     # 펜의 색깔
t.begin_fill()     # 색칠할 영역의 시작
for i in range(3):
    t.forward(100)
    t.right(360/3)
t.end_fill()       # 색칠할 영역 끝


#3
import turtle as t
length = int(input('Enter the length of a star: '))
t.shape('turtle')
for i in range(5):
    t.forward(length)
    t.right(180-36)


