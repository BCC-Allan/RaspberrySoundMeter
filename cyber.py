import RPi.GPIO as GPIO
# import leitor_audio
import calcula
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)#Button to GPIO23
GPIO.setup(24, GPIO.OUT)   #LED to GPIO24


def loop_principal():
    nomearq = "result.wav"
    last_state = False
    inicial = time.time()
    C = 0
    try:
        while True:
            button_state = GPIO.input(23) == GPIO.HIGH
            if button_state == False:
                if last_state == True:
                    tempo = time.time() - inicial
                    GPIO.output(24, True)
                    time.sleep(tempo)
                    GPIO.output(24, False)
                    # leitor_audio.gravar(nomearq, record_time=tempo)
                    calcula.calcular_db(nomearq)

                print('{C} Button Pressed...'.format({C:C}))
                time.sleep(0.2)
            else:
                if last_state == False:
                   inicial = time.time()
                # GPIO.output(24, False)
            last_state = button_state

    except Exception as e:
        print(e)
        GPIO.cleanup()


loop_principal()