import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(5, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)

GPIO.output(5, 0)
GPIO.output(12, 0)
GPIO.output(16, 0)
GPIO.output(26, 0)

time.sleep(2)

run = True;

while run:
        leftButton = GPIO.input(19)
        rightButton = GPIO.input(13)
        if leftButton == False and rightButton == False:
            print("BOTH")
            GPIO.output(5, 0)
            GPIO.output(12, 0)
            GPIO.output(16, 0)
            GPIO.output(26, 1)
            time.sleep(0.2)

        if leftButton == False and rightButton == True:
            print("ONLY LEFT")
            GPIO.output(5, 0)
            GPIO.output(12, 0)
            GPIO.output(16, 1)
            GPIO.output(26, 0)

            time.sleep(0.2)

        if leftButton == True and rightButton == False:
            print("ONLY RIGHT")
            GPIO.output(5, 0)
            GPIO.output(12, 1)
            GPIO.output(16, 0)
            GPIO.output(26, 0)
            time.sleep(0.2)

        if leftButton == True and rightButton == True:
            print("NOTHING")
            GPIO.output(5, 1)
            GPIO.output(12, 0)
            GPIO.output(16, 0)
            GPIO.output(26, 0)
            time.sleep(0.2)
