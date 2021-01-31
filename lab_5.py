def lab_5():
    from gpiozero import Button # import module LED
    from gpiozero import LED # import module LED
    from time import sleep
    button = Button(2)
    led =LED(17)
    while True:
     if button.is_pressed:
     print("Pressed")
     led.on() # set the GPIO 17 to high
     else:
     print("Released")
     led.off() # set the GPIO 17 to low
     sleep(1)
    


from gpiozero import PWMLED
from time import sleep
led = PWMLED(21)
while True:
 led.value = 0 # off
 sleep(1)
 led.value = 0.5 # half brightness
 sleep(1)
 led.value = 1 # full brightness
 sleep(1)
    
if_name_=='_main_':
    lab_5()