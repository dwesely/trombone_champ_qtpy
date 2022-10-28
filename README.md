# trombone_champ
Controller for trombone champ game

Control Trombone Champ by emulating a mouse with a QT-PY 2040 and VL53L0X distance sensor.

Parts and connections:
![Fritzing representation of parts and connections](qtpy_controller_bb.png)

## Target operation

3-way switch allows orientation to be inverted, or to disable the mouse emulation (so it doesn't interfere with operation outside the game).

The momentary switch clicks mouse button 1, activating toot.

A rotary encoder acts as mouse wheel and mouse button 2.

A potentiometer sets the scale (max distance), to make operation more comfortable for people with different sizes of arms.

## Other features 

Hardware debounce to clean up toot command without adding processing complexity.

On board RGB LED indicates detected position (red for low/far, blue for high/near.

JST connectors for input devices. 
