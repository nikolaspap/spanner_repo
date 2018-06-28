from Spannerpi import Spannerpi
from Tester import Tester
from Ifttt import Ifttt
import time

BINARY_FROM = "SPANNER"
SID = "2c0019001347343438323536"

spannerpi = Spannerpi()
tester = Tester(SID)
ifttt = Ifttt()

# Cloud Functionality
def C1_validate_ifttt_buttonOn():
   # check blue led state
   value0 = tester.digitalWrite("D7", "HIGH")
   print(value0)

   value1 = tester.digitalRead("D7")
   print(value1)

   if value1['return_value'] == 1:
       return 0
   else:
       return 1

if __name__ == "__main__":
   res = run_test(C1_validate_ifttt_buttonOn())
   print(res)
