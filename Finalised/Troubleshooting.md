# Troubleshooting

## Purpose
This file documents the error messages associated within the bacterial bomb model. This document should be used in order to troubleshoot encountered issues.

<br />

## Parameter Validation
Within this model the user is asked to input values for nine variables which dictate the initial conditions and wind speed of the scenario at hand.

##### Initial Conditions
   * Number of Bacteria: Number of bacteria to be released by the bomb
   * Elevation: Height at which bomb is detonated
   
##### XY Probabilities 
   * North: Probability of particle moving in the positive y direction
   * South: Probability of particle moving in the negative y direction
   * West: Probability of particle moving in the negative x direction
   * East: Probability of particle moving in the positive x direction
##### Z Probabilites
   * Up: Probability of particle moving in the positive z direction
   * Level: Probability of particle keeping a constant z value
   * Down: Probability of particle moving in the negative z direction
    
These parameters are validated against a set of defined conditions before the program is allowed to proceed. These condition can be viewed in full within the readme documentation XXXXX. These check have been thoughly tested and this can be seen here XXXX. Incorrect values will result in one of the following three error messages being displayed.

### Errror Message 1:

<img src="https://github.com/mjggibson4/Practical2/blob/master/Images/ErrorSum.png">

Cause: Parameters defining probabilities do not sum to 1 and hence need reviewed

### Error Message 2:

<img src="https://github.com/mjggibson4/Practical2/blob/master/Images/ErrorNonNumeric.png" width="550">

Cause: String values have been entered within the parameters and need removed.

### Error Message 3: 

<img src="https://github.com/mjggibson4/Practical2/blob/master/Images/ErrorNegative.png" width="550">

Cause: Negative values have been inserted within the parameters


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

