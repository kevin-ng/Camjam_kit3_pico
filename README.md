# Camjam_kit3_pico
Discuss issues with porting existing lessons of Camjam motor kit to pico

### Camjam motor controller kit pinouts for RPi

motor A - 19, 21

 motor B - 8, 7



![](./image/20230819_camjam_kit3.jpg)

### Rpi pico pinouts

![](./image/20230819_pico_pinout.jpg)

    pins = """        ---usb---

GP0  1  |o     o| -1  VBUS
GP1  2  |o     o| -2  VSYS
GND  3  |o     o| -3  GND
GP2  4  |o     o| -4  3V3_EN
GP3  5  |o     o| -5  3V3(OUT)
GP4  6  |o     o| -6           ADC_VREF
GP5  7  |o     o| -7  GP28     ADC2
GND  8  |o     o| -8  GND      AGND
GP6  9  |o     o| -9  GP27     ADC1
GP7  10 |o     o| -10 GP26     ADC0
GP8  11 |o     o| -11 RUN
GP9  12 |o     o| -12 GP22
GND  13 |o     o| -13 GND
GP10 14 |o     o| -14 GP21
GP11 15 |o     o| -15 GP20
GP12 16 |o     o| -16 GP19
GP13 17 |o     o| -17 GP18
GND  18 |o     o| -18 GND
GP14 19 |o     o| -19 GP17
GP15 20 |o     o| -20 GP16
        ---------"""

### motor test code with GPIO zero

```python
# Turn all motors off
GPIO.output(7, 0)
GPIO.output(8, 0)
GPIO.output(9, 0)
GPIO.output(10, 0)

# Turn the right motor forwards
GPIO.output(9, 0)
GPIO.output(10, 1)

# Turn the left motor forwards
GPIO.output(7, 0)
GPIO.output(8, 1)
```



### Electrical interface compatibility issue

From the motor test code with GPIO zero lib, the pins to drive motors are (7,8,9,10).

The controller was designed to plug into the expansion port of the RPi.

The Rpi pico has a 40 pin connector with totally different layout compared to that of Rpi. The ground pins do not align with each other. Therefore electrically the pico and Rpi pinouts are incompatible.

The controller with its 26pin connector was designed to work with Rpi and therefore cannot be plugged into the pico.

There are 3 ways to circumvent this issue:

* Design an adapter to translate the pinout of the existing motor kit to match with that of the pico, or
* Patch dupont wires from the motor kit to that of pico, or
* Design a new motor kit specifically for the pico



For hackers, patch is acceptable.

For education to 9 year old, patch is probably not acceptable.

 

### Patch wire recommendation

5 wires had to be connected from the controller to the pico. This arrangement ensures the same GPIO numbers are maintained and therefore the same python code from GPIOzero can be run with Picozero.

| Motor controller | Pico              | Function          |
| ---------------- | ----------------- | ----------------- |
| GPIO 7 (pin 26 ) | GPIO 7  (pin 10)  | motorB_0          |
| GPIO 8 (pin 24 ) | GPIO 8   (pin 11) | motorB_1          |
| GPIO 9 (pin 21 ) | GPIO 9  (pin 12)  | motorA_0          |
| GPIO 10 (pin 19) | GPIO 10 (pin 14)  | motorA_1          |
| GND              | GND  (pin 13)     | electrical ground |
|                  |                   |                   |
|                  |                   |                   |



### Reference

* Picozero - https://github.com/RaspberryPiFoundation/picozero
* Camjam motor kit 3 - https://camjam.me/?page_id=1035
* Camjam motor kit 3 on github - https://github.com/CamJam-EduKit/EduKit3/blob/master/CamJam%20Edukit%203%20-%20RPi.GPIO/Code/3-motors.py



end of this doc

