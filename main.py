def on_button_pressed_a():
    basic.show_leds("""
        # # # # #
                . # . . #
                . . # . #
                . . . # #
                . . . . #
    """)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.show_icon(IconNames.LEFT_TRIANGLE)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    pass
basic.forever(on_forever)
