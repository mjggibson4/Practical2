# Document Scope

This document seeks out to outline the problem which is to be solved within Practical 2 of the module GIS and Python. The deliverables will be developed within this paper and the development plan by which this will be achieved will be outlined. This document is to be updated during this process detailing testing within each stage of development.

# Introduction

In our scenario the customer is wishing to model the impact a bacterial bomb would have within a spatial domain. The bomb is to be denoted at a height of 75m and released 5000 particles. The scope of this project is to track the final resting places of these 5000 particles and display these locations to the user. This heatmap will also be exported to a csv file. 

# Deliverables

The deliverables required for this project have been split into two categories for prioritisation purposes.

### Must Haves:

The produced program should include the basic functionality in order to be considered acceptable by the customer:

*	Display the landing locations of the bacteria within a graph to the user
*	Record the landing locations of the bacteria within a .csv file
*	Application should be presented within a user-friendly GUI.
*	Application should be well commented to the standards defined within the Google style guide. http://google.github.io/styleguide/pyguide.html

### Nice to Haves:

*	A dynamic GUI in which users can input their own parameters
*	A method of validating these parameters before running the program.
*	Production of a series of statistics regarding the bacteria movement
*	Web scrape the bomb location from an online resource

# Development Plan

This project will be undertaken using an iterative to software development. In this approach, the software in constructed in stages each building on the functionality that was introduced within the last iteration (Fronczak, 2019).


<img src="https://github.com/mjggibson4/Practical2/blob/master/Images/IncrementalIterations.png" width="450">

At the time of writing, it is intended to break this workflow into 4 stages:

* Version 1:    Outline basic moving mechanics of bacteria
* Version 1.1:  Create wind probability variables and create bacteria class in distinct script
* Version 1.2:  Create GUI script for project. Create error trapping methods.
* Version 1.3   Finalise project

# Version 1

### Scope 

The scope of this version of the model was to produce a rudimental version of the bacterial plume. This script was focused on modelling the movement of the bacteria within the plume using the provided probabilities and intentionally kept within one script in aid of simplicity. This script was to be used as a basis on which the whole project would be expanded and fleshed out. 

The scope of this model included:
*	The ability to read a file containing the bombing location
*	Find the coordinates of this location within this file
*	Produce a blank square list to be used to mark the landing locations of the bacteria
*	Move the bacteria in a random fashion in both vertical and horizontal locations
*	Record the landing locations of these bacteria and display these within a heat map

### Testing

The program was ran using the initial conditions as defined by the customers which are defined below:

<img style="float: right;" src="https://github.com/mjggibson4/Practical2/blob/master/Images/IncrementalIterations.png" width="150">

| Initial Conditions  |      |
|---------------------|------|
| Number of Bacteria  | 5000 |
| Elevation           | 75   |
|                     |      |

|    XY Probabilities    |      |
|------------------------|------|
| West                   | 0.05 |
| East                   | 0.75 |
| North                  | 0.1  |
| South                  | 0.1  |

|    Z Probabilities     |      |
|------------------------|------|
| Down                   | 0.7  |
| Up                     | 0.2  |
| North                  | 0.1  |



# References

Fronczak S. (2019). Software Development Life Cycle (SDLC): Making Sense of the Different Methodologies. Available: https://www.plutora.com/blog/software-development-life-cycle-making-sense-of-the-different-methodologies. Last accessed 1st Jan 2020.
