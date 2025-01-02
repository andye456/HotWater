import machine, onewire, ds18x20
import network
import time
import urequests
import ujson
"""
This is to be sent to the Pico using Thonny
"""
ssid = "EE-39NJN7"
password = "wKbRWdu4WfDTNuLU"

led = machine.Pin("LED", machine.Pin.OUT)
led.low()

# This is the reset timer, sets it to the current time in 
reset_watchdog = time.ticks_ms()
# above doesn't seem to work, try using iterations
iterations = 0
def blink(num, timep):
    for _ in range(num):
        led.high()
        time.sleep(timep)
        led.low()
        time.sleep(timep)

def get_date():
    (y, mo, d, _, h, m, s, _) = rtc.datetime()
    date = f"{y}-{'%02d' % mo}-{'%02d' % d}T{'%02d' % h}:{'%02d' % m}:{'%02d' % s}"
    return date

# def log(message):
#     url = "http://18.168.124.146:3000/log"
#     try:
#         data = ujson.dumps({"time": get_date, "message": message})
#         response = urequests.post(url, headers={'content-type': 'application/json'}, data=data)
#     except:
#         blink(2, 2)
#         # print(response.text)
#     response.close()

#log("Entry point after a reset")
def connect():
    # Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        blink(1, 0.1)
        time.sleep(1)
    #log(wlan.ifconfig())
    blink(5, 0.1)


try:
    connect()
#     blink(2,0.5)
#     time.sleep(1)

except:
    blink(20, 0.1)
    machine.reset()

# get the current time from the end-point
url = "http://18.168.124.146:3000/get_time"
now = urequests.get(url)
print("Got time", now.text)
t = now.text.split(",")
rtc = machine.RTC()
print(rtc.datetime((int(t[0]), int(t[1]), int(t[2]), int(t[3]), int(t[4]), int(t[5]), int(t[6]), int(t[7]))))

t_pin = []
t = []
# These correspond to the GPn ping of the Pico (range, 21 not included)
for i in range(16, 23):
    t_pin.append(machine.Pin(i))
for i in range(26, 29):
    t_pin.append(machine.Pin(i))
# blink(3,0.5)
# time.sleep(1)

for tp in t_pin:
    t.append(ds18x20.DS18X20(onewire.OneWire(tp)))
# blink(4,0.5)
# time.sleep(1)

roms = []
for temp in t:
    #log(temp.scan()[0])
    try:
        roms.append(temp.scan()[0])
    except:
        blink(1, 3)

#for r in roms:
#    log(r)

print(time.gmtime(1674820741))

while True:
    sent_time = time.ticks_ms()
    #log(sent_time)
    #     blink(5,0.5)
    #     time.sleep(1)
    try:
        for c in t:
            c.convert_temp()
            # pause between each temp reading
            time.sleep_ms(500)
            blink(1, 0.025)
    except:
        f.close()
        #log("cannot convert temp")
        blink(2, 1)

    #     blink(6,0.5)
    #     time.sleep(1)

    temp = [None] * 10
    # reads each of the probes and write value to a "t" value
    for x, rom in enumerate(roms):
        #log(rom)
        temp[x] = t[x].read_temp(rom)
    #     blink(7,0.5)
    #     time.sleep(1)

    # (y, mo, d, _, h, m, s, _) = rtc.datetime()
    date = get_date
    #     blink(8,0.5)
    #     time.sleep(1)

    # add the temperatures to the REST data
    post_data = ujson.dumps({'time': date, 'data':
        [{'id': 't1', 'time': date, 'temp': temp[0]},
         {'id': 't2', 'time': date, 'temp': temp[1]},
         {'id': 't3', 'time': date, 'temp': temp[2]},
         {'id': 't4', 'time': date, 'temp': temp[3]},
         {'id': 't5', 'time': date, 'temp': temp[4]},
         {'id': 't6', 'time': date, 'temp': temp[5]},
         {'id': 't7', 'time': date, 'temp': temp[6]},
         {'id': 't8', 'time': date, 'temp': temp[7]},
         {'id': 't9', 'time': date, 'temp': temp[8]},
         {'id': 't10', 'time': date, 'temp': temp[9]}]})
    print(post_data)
    url = "http://18.168.124.146:3000/add"
    try:
        response = urequests.post(url, headers={'content-type': 'application/json'}, data=post_data)
    #         blink(9,0.5)
    #         time.sleep(1)

    except:
        blink(2, 2)
        print(response.text)
    response.close()
    # get here if data posted
    #     blink(10,0.5)
    #     time.sleep(1)

    # pasuses for 300 seconds
    while time.ticks_diff(time.ticks_ms(), sent_time) < 300000:
        blink(1, 0.01)
        time.sleep(1)
    
    #log(iterations)
    if iterations > 144:
        #log("should reset now")
        machine.reset()

    iterations+=1
    # If the time elapsed since the program started exceeds 1 hour then reset.
    #if time.ticks_diff(time.ticks_ms(), reset_watchdog) > 3600000: 
    #    machine.reset()
    




