import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(18,GPIO.IN,pull_up_down=GPIO.PUD_UP)

while True:
    try:
        button_state =GPIO.input(18)
        if button_state==False:
            print('Button ON')
            time.sleep(0.2)

    except KeyboardInterrupt:
        pass
        print('Exit with ^C. Goodbye!')
        GPIO.cleanup()
        exit()
