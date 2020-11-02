# printer
Package to switch on and off the printer and the LEDs (RGB).

It subscribes to two topics:

## /switch_printer (std_msgs/Bool)
If value received is True, the printer is switched on
If value received is False, the printer is switched off

## /switch_rgb (std_msgs/Int16MultiArray)
The value received indicates wether red (R), green (G) or blue (B) leds are switched on or off.
If the value received is [0, 0, 0], all leds are switched off, and if the value is [1,1,1] all leds are switche on.
Note that the first value referes to red (R), the second to green (G) and the third to blue (B): [R, G, B]
