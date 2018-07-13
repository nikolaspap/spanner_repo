from Testboard import Testboard
from Ifttt import Ifttt
import time

BINARY_FROM = "SPANNER"
TESTBOARD_ID = "340040000f51353532343635"
IFTTT_ACCESS_TOKEN = "54c8df8cb04da38a34e26ec6da046abf92182de4"

testboard = Testboard(TESTBOARD_ID)
ifttt = Ifttt(IFTTT_ACCESS_TOKEN)

# D7 -> Relay PIN
RELAY_PIN = "D7"

# Cloud Functionality
def validate_network_cmd_on():
    ifttt.buttonOn()

    testboard.digitalWrite(RELAY_PIN, 'HIGH')
    time.sleep(2)

    # check PIN state
    value = testboard.digitalRead(RELAY_PIN)
    if (testboard.spanner_assertTrue(value) == 1):
        return 0 # Success
    else:
        return 1 # Failure

# Cloud Functionality
def validate_network_cmd_off():
    ifttt.buttonOff()

    # check PIN state
    value = testboard.digitalRead(RELAY_PIN)
    if (testboard.spanner_assertTrue(value) == 0):
        return 0 # Success
    else:
        return 1 # Failure

if __name__ == "__main__":
    print("Spanner Started")
#     run_test(validate_network_cmd_on())
    print("WAITING FOR 4minutes")
    time.sleep(1800)
    print("WAITING FOR 2 more minutes")
    time.sleep(2)
    print("Spanner Test Finished")
