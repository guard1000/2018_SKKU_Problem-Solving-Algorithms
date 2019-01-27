#4-1
#import turtle as t

#t.bgcolor('black')
#t.speed( 0) # 거북이 속도 최대

#for x in range(200):
#    if x%3 ==0:
#        cl = 'red'
#    if x%3 ==1:
#        cl = 'yellow'
#    if x%3 ==2:
#       cl = 'blue'

#    t.color(cl)
#    t.forward(x *2)

 #   t.left(119)


#4-2
import turtle as t

t.shape('turtle')

n = 70
t.bgcolor('black')
t.color('green')
t.speed(0)
for x in range(n):
    t.circle(80)
    t.left(360/n)


