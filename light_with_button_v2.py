from gpiozero import LED, Button
from signal import pause

# GPIO 26
myLED = LED(26)
mySwitch = Button(2)

myLED.blink()


pause()
