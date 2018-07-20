# This example will set one of our Testboard's outputs, first to HIGH, and then to LOW.
#
# The goal of this example is to show you how you can drive a digital input on your device from the Testboard.
#
# In our particular example, we are only setting value and not asserting anything. Of course this would never be a real world example, it's only for educational purposes
import time
from Spanner import Spanner
from Testboard import Testboard

TESTBOARD_ID = "200023001347343438323536"
testboard = Testboard(TESTBOARD_ID)

# Our Product's Input will be connected the Testboard's Pin D3, making it our Output Pin
OUTPUT_PIN = "D3"

def toggle_digital_output():
    # set PIN state
    value = testboard.digitalWrite(OUTPUT_PIN, 'HIGH')
    spanner.assertTrue(value)

    time.sleep(2)

    value = testboard.digitalWrite(OUTPUT_PIN, 'LOW')
    spanner.assertFalse(value)

if __name__ == "__main__":
    toggle_digital_output()
