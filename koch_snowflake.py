import turtle


def koch_snowflake(t, recursion_level, line_size):
    """Створює сніжинку Коха.

    t: Turtle
    recursion_level: Глибина рекурсії
    line_size: Довжина лінії
    """
    if recursion_level == 0:
        t.forward(line_size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(t, recursion_level-1, line_size/3)
            t.left(angle)


def main():

    recursion_level = int(input("Введіть рівень рекурсії: "))
    line_size = 300

    screen = turtle.Screen()

    t = turtle.Turtle()
    t.speed(0)  # найбільша швидкість
    # центрування
    t.penup()
    t.backward(line_size/1.732)
    t.pendown()

    # Створення сніжинки
    for _ in range(3):
        koch_snowflake(t, recursion_level, line_size)
        t.right(120)

    t.end_fill()
    t._update()
    screen.mainloop()


if __name__ == "__main__":
    main()
