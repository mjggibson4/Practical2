# Bacterial Bomb Model

## Description

This python-based project has been designed to model of the fallout of a bacterial bomb. In this scenario, a bacterial based bomb has been placed at the top of a building and this program has been designed to model the movement of these particles within the wind and record their find resting locations. This wind is determined by probabilities which are to be defined by the user. The final output of this model is a heatmap of the resting locations of the bacteria and an associated csv file. 
An in depth insight into how this program was developed is available [here](https://github.com/mjggibson4/Practical1/blob/master/Scope.md ""):

## Table of Contents

1. Prerequisites
2. Installation
3. Initialising Program
4. Running Program
5. Standards Used
6. Known Issues
7. Troubleshooting
8. Licensing
9. Acknowledgements

## 1. Prerequisites

Before this project can be executed, a suitable python environment must first be in place. This project was used using the data science platform Anaconda. This package is free and includes the integrated development environment Spyder 3.3.6 on which this project was developed. An installation guide to Anaconda alongside installation instructions can be found here: 
[install guide](https://docs.anaconda.com/anaconda/install/windows/ ""). 

This model scrapes the initial location of the bomb from the web. Due to this a suitable web connection is advised. In the absence of an internet connection, a .txt file containing this bombing location has also been provided. 
This model was developed in a PC environment but has been successfully tested on Mac OS.

## 2. Installation

This project consists of 3 python scripts and one text file which should be downloaded from the github repository found here: [Practical 2 Repo](https://github.com/mjggibson4/Practical2 ""). These files should be saved to the user’s desktop. This program attempts to write a .csv file in the location from which the project is run. It is for this reason important the user has write access to this location to prevent complications.

## 3. Project Structure

The three script files contained within this project have their own unique function.

GUI:  Sets up the graphical user interfaces from which the program is run. This interface allows for the initial parameters of the model to be edited as necessary. These parameters are verified within this GUI script before the model is allowed to run. 

Maincode: Defines the logic behind the model itself.

Framework: Contains the classes from which the bacterial agents are defined. This framework dictates the behaviours of the bacteria such as how they move in the XY and Z planes.

In.txt (Optional but recommended): Backup environment containing the bombing location in the event of no internet connection.

## 3. Initialising the Program

This model can be initialised in one of two manners:

#### Option A: From command line
1. Right click on the Desktop.
2. Select “Open New Command Window Here”
3. Type python GUI.py
4. Press enter

#### Option B: From IDE
1. Open the file GUI in Spyder
2. Press Run

Either of these methods should result in the GUI for the Bacterial Bomb model being presented as displayed below:

<img src="https://github.com/mjggibson4/Practical1/blob/master/GUIGrab.png" width="300">


## 4. Running Model

### Setting Parameters 

Click the Model menu and then "Set Parameters". This produces a window in which the user is asked to input 3 sets of parameters which will influence the behaviour of the model. These parameters are listed below alongside a brief explanation of what they represent in regards to the model.

#### Initial Conditions
       Number of Bacteria: Number of bacteria to be released by the bomb
       Elevation: Height at which bomb is detonated
        #### XY Probabilities 
        North: Probability of particle moving in the positive y direction
        South: Probability of particle moving in the negative y direction
        West: Probability of particle moving in the negative x direction
        East: Probability of particle moving in the positive x direction

#### Z Probabilites
        Up: Probability of particle moving in the positive z direction
        Level: Probability of particle keeping a constant z value
        Down: Probability of particle moving in the negative z direction

A screenshot of this menu is provided below:

![alt text](https://github.com/mjggibson4/Practical1/blob/master/ParameterMenu.png "Logo Title Text 1")
 
Once these parameters have been defined, click apply. These parameters must fulfil the following conditions in order to be accepted by the GUI:

*  All parameters must not be strings
* Parameters defining XY movement must all be decimals between 0 and 1
* Parameters defining XY movement must sum to 1
* Parameters defining Z movement must all be decimals between 0 and 1
* Parameters defining Z movement must sum to 1
* The parameters defining the number of bacteria and elevation must be positive integers

An internal check occurs to verify these parameters are valid case. If integers are not input, the following warning screen is displayed and user is forced to re-enter appropriate values:


<img src="https://github.com/mjggibson4/Practical1/blob/master/ParameterError.png" width="550">


### Run the Model

Select the "Model" menu and "Click" Run. Within the canvas of the GUI, the final resting locations of the bacteria will be displayed as seen below.

![alt text](https://github.com/mjggibson4/Practical2/blob/master/Images/RunExample.PNG "Example Run")

Alongside this, a set of statistics are displayed detailing the behaviour of the bacteria, 

## 5. Standards Used

This model has been produced in Python 3.7. The code has been produced to adhere to Google Python standards. The full details of this style can be found [here](http://google.github.io/styleguide/pyguide.html ""). This code has been produced in a manner consistent with the loose coupling pattern.

## 6. Known Issues

A known issue within this project is that an unnecessary figure  is display on running the program. The source of this bug is unknown at the time of writing but has zero impact of the functionality of the program itself and the results provided. 

## 7. Troubleshooting
In the case of errors within this program please check the troubleshooting file which can be located [here](https://github.com/mjggibson4/Practical2/blob/master/InternalChecks.md "")

## 8. Licensing

This program is open source and licensed via an MIT license. The full details of this license are available [here](https://github.com/mjggibson4/Practical1/blob/master/License.md "")

## 9. Acknowledgements

This project has been produced as part of coursework for the module: Programming for Geographical Information Analysts: Core Skills (WUN).  Exercises and tutorials given within this course have been modified as appropriate and used within the python code for this project. In addition, I'd like to give thanks to my course tutor Andy Turner who helped with issues encountered during development.

References for the produced code as available in the following here [here](https://github.com/mjggibson4/Practical1/blob/master/References.md "")

