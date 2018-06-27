
# Cloud Functionality
def validate_network_cmd_off():
    ifttt.buttonOff()

    time.sleep(2)

    # check PIN state
    value = testboard.digitalRead(RELAY_PIN)
    if (testboard.assert_spanner(value) == 0):
        return 0 # Success
    else:
        return 1 # Failure

if __name__ == "__main__":

    run_test(validate_network_cmd_on())

    time.sleep(2)

    print("nikolas")
    run_test(validate_network_cmd_off())
