## Smart Cooking Assistance — Real-Time Sensor Fusion (Work In Progress)

This project aims to detect cooking states (OFF → PREHEAT → FULL → SIMMER → OFF) in real time using temperature + video + timing.
The goal is to create an infotainment-grade kitchen assistance system that can profile how chefs cook and then guide users with structured feedback.

## Hardware Used (Phase 1)

STM32F446RE

MAX6675 Thermocouple Module (K-type)

Direct burner + pan experiments

USB camera (for video capture)

## Software (Phase 1)

Python 3.10

OpenCV (video capture + encode)

Pandas (signal processing)

Matplotlib (diagnostics)

ffmpeg (video conversion)

Slope-based cooking mode inference

Cooking Mode Detection (Prototype)

OFF

PREHEAT

FULL

SIMMER

OFF

## Stages inferred using:

smoothed temperature

slope (°C/sec)

variance

thresholds

Example Output

stages.json

{
  "segments": [
    {"mode":"FULL","start":0.0,"end":180.4},
    {"mode":"SIMMER","start":180.4,"end":360.2},
    {"mode":"FULL","start":360.2,"end":600.1},
    {"mode":"OFF","start":600.1,"end":720.8}
  ]
}
