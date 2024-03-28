import turtle

def main():
    t = turtle.Turtle()
    move(t, 0, 0)
    t.screen.mainloop()


def move(t, x, y):
    if x == 200:
        return
    t.goto(x, y)
    move(t, x+10, y+10)

main()