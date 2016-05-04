import random
import turtle
t = turtle.Turtle()
wn = turtle.Screen()
wn.tracer(0)


t.left(90)

def draw_tree(s, w):
    if s <= 5:
        return
    else:
        new_w = w if w <= 1 else w - 1
        t.pensize(w)
        a1 = random.randint(20, 50)
        t.forward(s)
        t.left(a1)
        draw_tree(s - random.randint(2, s // 2), new_w)
        a2 = random.randint(20, 50)
        t.right(a1 + a2)
        draw_tree(s - random.randint(2, s // 2), new_w)
        t.left(a2)
        t.back(s)
for x in range(-300, 301, 200):
    print(x)
    t.up()
    t.goto(x, -100)
    t.down()
    t.color("#{}".format(str(random.randint(0, 6)) * 3))
    draw_tree(random.randint(30, 100), random.randint(4, 10))

wn.mainloop()
"""
for i in range(4):
    draw_tree(random.randint(30, 50), random.randint(3, 7))
    t.up()
    t.goto(i * 200 - 400, random.randint(-100, 100))
    t.down()
"""
