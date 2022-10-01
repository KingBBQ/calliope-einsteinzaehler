input.onButtonEvent(Button.A, input.buttonEventClick(), function () {
    basic.setLedColor(0xff0000)
    basic.showNumber(Zähler)
    basic.pause(1000)
    basic.setLedColor(0x00ff00)
    basic.pause(5000)
    basic.setLedColor(0x000000)
})
Touch.touchP1.onEvent(TouchButtonEvent.Down, function () {
    basic.setLedColor(0xff0000)
    Zähler += 1
    basic.showNumber(Zähler)
    basic.pause(1000)
    basic.setLedColor(0x00ff00)
    basic.pause(5000)
    basic.setLedColor(0x000000)
})
let Zähler = 0
Zähler = 0
Touch.touchP1.calibrate()
basic.setLedColor(0x00ff00)
basic.forever(function () {
	
})
