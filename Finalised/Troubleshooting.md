# Troubleshooting/Internal Checks

## Purpose
This file documents the internal checks that occur within the code of the Population Model project in order to ensure that it functions correctly. This document should also be used for troubleshooting purposes.

<br />

## User Inputs
Within this model the user is asked to input values for six variables:

            * num_of_sheep 
            * num_of_wolves 
            * neighbourhood 
            * num_of_iterations 
            * wolf_threshold 
            * sheep_threshold 
            
These variables MUST be positive integers for the program to function correctly. This data is validated internally via a try/except error capturing structure. In the event one of these variables is found not be a positive integer a message box is displayed asking the user to reenter these values as shown below.         

<img src="https://github.com/mjggibson4/Practical1/blob/master/ParameterError.png" width="550">

<br />


## Web Scraping

The initial locations of the sheep agents are defined via webscraping. In the event that an internet connection is not available this program would fail. To prevent this, a try/except error capturing structure has been put in place. In this structure, the program attempts to access values defined within the html of a defined website and set these to defined variables. If this process fails, the intial starting locations of the agents are placed randomly within the environment's domain. In this scenario, the user is alerted by the following message box.

<img src="https://github.com/mjggibson4/Practical1/blob/master/NetworkError.png" width="550">


<br />

## Environment

The environment within this model is defined via a .txt file. If this file is not present within the directory from which the script is being run then the program would fail. In this scenario, a try/except error capturing structure has been defined to alert the user and terminate the program.

<img src="https://github.com/mjggibson4/Practical1/blob/master/NetworkError.png" width="550">

