import turtle
t = turtle.Turtle()
wn = turtle.Screen()


t.left(90)
def draw_tree(s):
    if s <= 5:
        return
    else:
        t.forward(s)
        t.left(30)
        draw_tree(s - 5)
        t.right(60)
        draw_tree(s - 5)
        t.left(30)
        t.back(s)
draw_tree(30)
wn.mainloop()
