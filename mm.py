length = 5
grid = [[0 for i in range(0,length)] for j in range(0,length)]

def show(gd):
    s = "\"\"\""
    for i in range(0,length):
        for j in range(0, length):
            if grid[i][j] == 1:
                s+="#"
            else:
                s+="."
        s+="\n"
    s+="\"\"\""
    basic.show_leds(s)

def on_forever():
    if input.button_is_pressed(Button.A):
        basic.show_leds("""
            . . . . .
                        . # # # .
                        . . . . .
                        . . . . .
                        . . . . .
        """)
basic.forever(on_forever)
