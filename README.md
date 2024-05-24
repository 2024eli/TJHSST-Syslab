# TJHSST-Syslab

This is Waste Wizard, a TJHSST senior research lab project created by Evelyn Li (Syslab), Abi Little (Engineering Lab), and Derek Liu). 

## Table of Contents

- [Arduino](#arduino)
- [Raspberry Pi](#raspberry-pi)
- [Model](#model)

## Arduino
Arduino code is all in *wastewiz.ino*. It controls the stepper motor, lcd, buttons, and signal to the pi. This code was written in collaboration between Abi Little and Evelyn Li. 

## Raspberry Pi
Code is: 
- *bt.py* (useless testing file)
- *start.py* (file where the waste classification model is processed and images are taken)
- *system.py* (file where the pi interacts with the arduino and works with it to make Waste Wizard work)

## Model
*wasteclassify_mobilenet.ipynb* is a python notebook run in TJ's Jupyter Hub that builds the model and test/trains it. 
