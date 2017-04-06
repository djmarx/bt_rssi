from bt_proximity import BluetoothRSSI
import time
import sys
from datetime import datetime

BT_ADDR = 'C8:A8:23:EE:14:61'  # Enter your bluetooth address here!

# -------------------- Do not Edit Anything Below this line!!! -------------------- #

NUM_LOOP = 2
records = []


def write(records, count):
    f = open("records.txt", "a+") #open records for append. If not present create
    for i in range(count): #write out each record
        f.write(str(records[i][0]) + "," + str(records[i][1]) + '\n')
    f.close()

def main():

    time.sleep(10)
    addr = BT_ADDR
    num = NUM_LOOP
    count = 0

    while(count < num):      
        btrssi = BluetoothRSSI(addr=addr)
        current_time = str(datetime.now().strftime('%H:%M:%S.%f')) #create current time
        record = (btrssi.get_rssi(), current_time)
        records.append(record)
        count += 1
        time.sleep(.5)
    write(records, count)


if __name__ == '__main__':
    main()
