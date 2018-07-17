# This example will test two of our Product's outputs, to make sure that one is high, and the other one is low.
#
# The goal of this example is to show you how you can read a simple digital output from your device, and how you can assert boolean values.
#
# In our particular example, we expect the pin we're connecting to our Testboard's D5 to be always LOW, and the pin we're connecting to our Testboard's D7 to be always HIGH. Of course this would never be a real world example, it's only for educational purposes
#
# If you want to replicate this setup, you can use our Particle Photon Testboard and connect the D5 pin to GND, and the D7 pin to 3V3.

import time
from Spanner import Spanner
from Testboard import Testboard

TESTBOARD_ID = "250020001047343438323536"
testboard = Testboard(TESTBOARD_ID)

if __name__ == "__main__":

    print("Spanner Unlimited Started")
    sleep(1200)
    print("Test almost Finished")
    sleep(100)
    print("Unlimited Finished")
