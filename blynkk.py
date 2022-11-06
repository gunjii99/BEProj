import blynklib
import random
import time

BLYNK_AUTH = 'BL6PB5eysjs-Bfzc4ptPk6_4cesG1dV2'
TARGET_EMAIL = 'beprojectbgv@gmail.com'

blynk = blynklib.Blynk(BLYNK_AUTH)
EMAIL_PRINT_MSG = "[EMAIL WAS SENT to '{}']".format(TARGET_EMAIL)


@blynk.handle_event("connect")
def connect_handler():
    print('Sleeping 2 sec before sending email...')
    time.sleep(2)
    blynk.email(TARGET_EMAIL, 'smart irrigation system', 'WATER YOUR FIELD!')
    print(EMAIL_PRINT_MSG)


###########################################################
# infinite loop that waits for event
###########################################################
while True:
    blynk.run()