# sleepstudy
Open Source Sleep study project

## Table of Contents
 - [Project in short](https://github.com/holmie/sleepstudy#project-overview)
 - [Wanted metrics / measurements](https://github.com/holmie/sleepstudy#wanted-metrics)
   - [Body position](https://github.com/holmie/sleepstudy#body-position)
   - [Heart rate](https://github.com/holmie/sleepstudy#heart-rate)
   - [Oxygen / SpO2](https://github.com/holmie/sleepstudy#spo2)
   - [Snore train](https://github.com/holmie/sleepstudy#snore-train)
   - [Breathing rate](https://github.com/holmie/sleepstudy#breathing-rate)
   - [Sweat](https://github.com/holmie/sleepstudy#sweat)
 - [Hardware](https://github.com/holmie/sleepstudy#hardware)
 - [Other projects](https://github.com/holmie/sleepstudy#other-projects)

## Project overview
I recently participated in a one night sleep study with the aim to measure the quality of my sleep.
Based on several metrics collected, it is possible to guesstimate the efficiency of your sleeping hours.
The metrics were collected with a device fitted to the chest by the aid of a rip band.

The aim of this project is to be able to create relatively cheap and modular hardware to collect metrics to determine the efficiency of a nights sleep.  
With this, it will be possible to self-study the sleep effects of increased or decreased amount of exercise, alcohol intake, tobacco and dietary habits. It will make it easier to take the right choices to decrease the risk of coronary heart disease and other diseases which are highly influenced by the amount of good sleep.

## Wanted Metrics

### Body Position
Body position may for many play a big role in the amount of consumed oxygen. This will aid in knowing which side is most beneficiary to sleep on.

### Heart Rate
How hard is your heart working to transport oxygen around to your organs?
A vital metric to measure stress, sleep phase and the amount of work to transport oxygen.

### SpO2
The actual amount of oxygenated haemoglobin. Assumed to be the most vital metric.

### Snore train
Not a vital metric, but there can be correlations between all the others. 
Snoring can be looked upon as a blockage of the air passage to the lungs.

### Breathing rate
A vital metric is how fast you are breathing, an increase while dropping in SpO2 suggests shallow breaths.
The depth of breaths should also be able to be measured by rip bands.

### Sweat
If possible, I want to measure how moist the skin is. It is a sign of a stressor.
This may involve pads, which may feel more intrusive and not so cost effective (they will wear out quick.)

## Hardware
I want for this to be WiFi (and MQTT) connected, with maybe a possibility for local data logging to sdcard.

First Header  | Second Header
------------- | -------------
The brain  | ESP32 (Bluetooth and WiFi enabled, with possibility of Micro SDCard)
Body position | GY-521 3 Axis Accelerometer Gyroscope Module 6 DOF MPU-6050 Module for the ESP32.
SpO2  | Have experimented with Contec CMS50D-BT, but may need help to investigate if it can give data points with wanted resolution. I have spent some time reverse engineering it, I will share my efforts in a directory in this repository.
Heart rate | Hopefully this will easily be picked from the SpO2 solution.
Snore train | Microphone hooked up to the ESP32.
Breathing rate | Cheap rip band?
Sweat | Assuming conductive pads

