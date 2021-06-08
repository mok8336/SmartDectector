
import RPi.GPIO as GPIO

import time

import smtplib
from email.mime.text import MIMEText

GPIO.setmode(GPIO.BCM)

#PIR센서 
pirPin = 7

GPIO.setup(pirPin, GPIO.IN, GPIO.PUD_UP)
#raspi에서 메세지를 보낼수 있게 하는 변수
smtp = smtplib.SMTP('smtp.gmail.com', 587)
smtp.starttls()
smtp.login('eucl2d@gmail.com','rrpwxiknvrkoubnx')


while True:
#PIR센서에 감지될경우
    if GPIO.input(pirPin) == GPIO.HIGH:
        #email로 메세지 전송
        print ("차량내 사람이 감지되어 메일을 보냅니다 gmail을 확인해주세요")
        msg = MIMEText('동작이 감지되었습니다 해당주소:192.168.50.39:8080/stream 링크로 접속하시거 어플로 차량내부를 확인하세요')
        msg['Subject'] = '라즈베리파이에서 보낸 메일'
        msg['To'] = 'mok8336@gmail.com'
        smtp.sendmail('eucl2d@gmail.com', 'mok8336@gmail.com', msg.as_string())
    else:
        print ("감지되지 않았습니다.")

    time.sleep(1)

