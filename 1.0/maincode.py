# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 17:19:15 2019

@author: mjggi
"""

"""A python script modelling a plume of deadly bacteria in a spatial domain

v1.0

This script models the movement of bacteria from a single release point. This
origin is located via an associated .txt file from which the coordinates are
extracted. The bacteria are individually moved both vertically and horizontally
from this point based on predefined probably which model wind behaviour. The 
landing point of each bacterium is recorded from which a heat map is produced.

Changelog

Probabilities added as parameters into move function
Acquried bomb location via web scraping
"""



import random
import matplotlib
import matplotlib.pyplot
import numpy

##f = open("BuildingPoint.txt")






def open_environment():
    """Create a list containing the origin of the bacterial bomb

    This function opens a text file containing the origin of the bacterial 
    bomb. This file is placed within the python environment and parsed
    into a list which is output
    
    Args:
        N/A

    Returns:
        environment: list containing bombing location

    Raises:
        TODO: Raise error if file not found.
    """
    f = open("in.txt")
    environment = []
    ##data = []
    for line in f:
        parsed_line = str.split(line,",")
        rowlist = []
        for word in parsed_line:
            rowlist.append(float(word))
        environment.append(rowlist)
    f.close()
    return environment



def find_bomb_origin(environment):
    """Extracts coordinates of bomb location from enviroment and returns these
    within a list

    Args:
        environment: list containing a single non zero value 

    Returns:
        origin: List containing two element representing the x and y coords
        of the bombing location

    Raises:
        TODO: Raise an error here if list has greater than two elements
    """
    
    #Extract coords of non zero element
    b_origin = numpy.nonzero(environment)
    print(b_origin)
    #pass coords into list and return
    bomb_origin = [int(b_origin[0]),int(b_origin[1])] 
    return bomb_origin




 
def set_initial_conditions(num_bact, elevation):
    """Sets the initial conditions of model

    Sets the initial conditions from which the model will be ran. This function
    is temporary and will be replaced by user input via a GUI

    Args:
        num_bact: number of bacteria within the model
        elevation: height at which bacteria will be released
            to fetch.
    Returns

    Raises:
        N/A
    """



 

def create_blank_heatmap(length):
    """Creates a blank square environment of defined size.

    This function creates a square enviroment containing exclusively zeros. To 
    be used to record the final landing positions of bacteria.
    
    Args:
        length: Length of square environment

    Returns:
        landscape: A square environmet of 0s
    """
    
    heatmap = []
    for i in range(length):
        row_list = []
        for j in range(length):
            row_list.append(0)
        heatmap.append(row_list)
    return heatmap

 






 
def move_bacteria(bomb_origin, num_bact, elevation, prob_north, prob_south, prob_west, prob_east, prob_up, prob_level, prob_down, heatmap):
    """Move bacteria in random fashion from bomb origin

    Moves bacteria both vertically and horizontally in a random fashion
    based on predefined probabilities. Particles are moved randomly in both
    directions until the elevation of the particle is 0. The position of this
    location is recorded.

    Args:
        bomb_origin: List containing bomb origin coordinates
        num_bact: number of bacteria to move
        elevation: Elevation of bomb
        heatmap: blank list on which final locations of bacteria are recorded
        prob_north: Probability of particle moving in the positive y direction
        prob_south: Probability of particle moving in the negative y direction
        prob_west: Probability of particle moving in the negative x direction
        prob_east: Probability of particle moving in the positive x direction
        prob_up: Probability of particle moving in the positive z direction
        prob_level: Probability of particle keeping a constant z value
        prob_down: Probability of particle moving in the negative z direction
    Returns:
        heatmap: marked list of landing locations of bacteria

    Raises:
        IOError: An error occurred accessing the bigtable.Table object.
        
    TODO make probabilities of wind direction inputs into this function     
    """    
    
    
    # Define blank list for location of bacteria to be recorded
    bacteria_location = []
    # Set variable to record the air time of bacteria before hitting ground 
    hang_time = 0
    for i in range(num_bact):
        #print(bomb_origin[0], bomb_origin[1], elevation, hang_time)
        # Create list defining properties of bacteria
        bacteria_location.append([bomb_origin[0], bomb_origin[1], elevation, hang_time])
        #print(bacteria_location)
        # End the movement of bacteria when it hits ground
        while bacteria_location[i][2] != 0:
            # Increase time increment by 1
            bacteria_location[i][3] += 1
            
            #Move bacteria in z direction
            # Generate random number from which elevation movement will be defined
            rand1 = random.random()
            # 20% chance of bacteria moving in +ve z direction
            if rand1 <= prob_up and bacteria_location[i][2] >= 75:
                bacteria_location[i][2] += 1
            # 10% chance of bacteria keeping a constant z value    
            elif rand1 <= (prob_up + prob_level) and bacteria_location[i][2] >= 75:
                bacteria_location[i][2] = bacteria_location[i][2]
            # 70% chance of bacteria moving in -ve z direction
            else:
                bacteria_location[i][2] -= 1
                                
                
            #Move bacteria in xy plane 
            # Generate random number from which xy movement will be decided
            randnum = random.random()
            # 5% chance of bacteria moving in -ve x direction
            if randnum  <= prob_west:
                bacteria_location[i][1] -= 1#
            # 10% chance of bacteria moving in -ve y direction    
            elif randnum <= (prob_west + prob_south):
                bacteria_location[i][0] -= 1
            # 10% chance of bacteria moving in +ve y direction     
            elif randnum <= (prob_west + prob_south + prob_north):
                bacteria_location[i][0] += 1
            # 75% chance of bacteria moving in ve x direction       
            else:
                bacteria_location[i][1] += 1
                
                
        # mark landing location of bacteria  
        final_y = int(bacteria_location[i][0])
        final_x = int(bacteria_location[i][1])
        heatmap[final_y][final_x] += 1
    return heatmap
        



if __name__ == "__main__":
    
    #Define intial conditions of model
    num_bact = 5000
    elevation = 75
    #Define probabilites. Looks a bit messy will need to pass six variables in
    # TODO: anyway to make this a bit slicker? 
    prob_west = 0.05
    prob_east =  0.75
    prob_north = 0.1
    prob_south = 0.1
    prob_up = 0.2
    prob_level = 0.1
    prob_down = 0.7
    #Find origin of bomb
    txt = open_environment()
    bomb_origin = find_bomb_origin(txt)
    # Create blank heatmap to be marked
    heatmap = create_blank_heatmap(500)
    #Input ICs and move bacteria
    move_bacteria(bomb_origin, num_bact, elevation, prob_north, prob_south, prob_west, prob_east, prob_up, prob_level, prob_down, heatmap)
    matplotlib.pyplot.xlim(0, 300)
    matplotlib.pyplot.ylim(0, 300)
    matplotlib.pyplot.imshow(heatmap)
    matplotlib.pyplot.scatter(50, 150, s = 8, color = "yellow", marker  = "*")
    matplotlib.pyplot.show()
    

    
    