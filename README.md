# Laser-Tracker

Main idea: we point a laser to an object moving within the range of our cameras, with focus on minimizing latency and maximizing precision.

We will be using Python for core computational tasks, such as computer vision, coordinate calculation and communication with Arduino.
Arduino will be used for physical control of the laser gimbal (the code will be written in C++).

---

#### Architecture

Hardware:

- two smartphone cameras (configured as high-FPS USB/IP webcams with Iriun)
- Arduino Uno
- actuators: two MG90S metal-gear micro servos mounted on a Pan-Tilt bracket
- low-power 5V laser diode

Software:

- Python: OpenCV (video feeds, real-time object detenction), NumPy (mathematical operations), PySerial (communication with microcontroller)
- C++: receives pre-calculated target angles from Python, directs the hardware with minimal latency
