from gpiozero import LED, Button
from signal import pause

# GPIO 26
myLED = LED(26)
mySwitch = Button(2)

# myLED.blink()
mySwitch.when_pressed = myLED.on
mySwitch.when_released = myLED.off

pause()
