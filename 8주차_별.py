import turtle as t
length = int(input('Enter the length of a star: '))
t.shape('turtle')
for i in range(5):
    t.forward(length)
    t.right(180-36)
