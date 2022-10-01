def on_button_a():
    basic.set_led_color(0xff0000)
    basic.show_number(Zähler)
    basic.pause(1000)
    basic.set_led_color(0x00ff00)
    basic.pause(5000)
    basic.set_led_color(0x000000)
input.on_button_event(Button.A, input.button_event_click(), on_button_a)

def on_touch_p1_down():
    global Zähler
    basic.set_led_color(0xff0000)
    Zähler += 1
    basic.show_number(Zähler)
    basic.pause(1000)
    basic.set_led_color(0x00ff00)
    basic.pause(5000)
    basic.set_led_color(0x000000)
Touch.touch_p1.on_event(TouchButtonEvent.DOWN, on_touch_p1_down)

Zähler = 0
Zähler = 0
Touch.touch_p1.calibrate()
basic.set_led_color(0x00ff00)

def on_forever():
    pass
basic.forever(on_forever)
