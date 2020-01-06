# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 17:19:15 2019

@author: mjggi
"""

"""A python script modelling a plume of deadly bacteria in a spatial domain

v1.2

This script models the movement of bacteria from a single release point. This
origin is located via an associated .txt file from which the coordinates are
extracted. The bacteria are individually moved both vertically and horizontally
from this point based on predefined probably which model wind behaviour. The 
landing point of each bacterium is recorded from which a heat map is produced.

Changelog:

Pull bacteria movement into sepearate class script in order to tidy and 
improve functionality
Added functionality to time taken for plume to hit the ground
Added fuctionality to measure distance covered by plume
TODO use this functionality to draw sensible axis on final figure
Added functionality to output csv on completion
Wind probabilites placed in a list for neatness and to reduce arguements into 
functions
"""


import csv
import matplotlib
import matplotlib.pyplot
import numpy
import FrameWork

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
        TODO: Scrape environment for web
        TODO: Raise error if file not found - although let program run if
        available.
        Try except set up in order to facilitate this.
        .
    """
    try:
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
        if len(environment) == len(environment[0]):
            return environment
    except:
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
        if len(environment) == len(environment[0]):
            return environment
        
     

def find_bomb_origin(environment):
    """Extracts coordinates of bomb location from enviroment and returns these
    within a list

    Args:
        environment: list containing a single non zero value 

    Returns:
        bomb_origin: List containing two element representing the x and y coords
        of the bombing location

    Raises:
        TODO [Completed]: Raise an error here if list has greater than two
        elements
    """
    
    #Extract coords of non zero element
    b_origin = numpy.nonzero(environment)
    # If one bombing location found, pass coordinates to a list
    if len(b_origin) == 2:
        bomb_origin = [int(b_origin[0]),int(b_origin[1])] 
        return bomb_origin
    # If more than one location found, terminate program. Out of scope for this
    # scenario
    elif len(b_origin) >= 2 :
        print('More than one bombing location found')
        #TODO add message box
    # If no bombing location found, define it to be null     
    else:
        bomb_origin = [None, None]
        return bomb_origin
        print('Random bombing location to be used')
        
        

def create_blank_heatmap(length):
    """Creates a blank square environment of defined size.

    This function creates a square enviroment containing exclusively zeros. To 
    be used to record the final landing positions of bacteria.
    
    Args:
        length: Length of square environment

    Returns:
        landscape: A square environmet containing purely '0'
    """
    
    heatmap = []
    for i in range(length):
        row_list = []
        for j in range(length):
            row_list.append(0)
        heatmap.append(row_list)
    return heatmap

 
def move_bacteria(bomb_origin, num_bact, elevation, wind_probabilities, heatmap):
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
        wind_probabilities - List whos element define the probabilites of a 
        bacteria moving in a defined direct. The elements within this list are
        described below
        
        prob_north: Probability of particle moving in the positive y direction
        prob_south: Probability of particle moving in the negative y direction
        prob_west: Probability of particle moving in the negative x direction
        prob_east: Probability of particle moving in the positive x direction
        prob_up: Probability of particle moving in the positive z direction
        prob_level: Probability of particle keeping a constant z value
        prob_down: Probability of particle moving in the negative z direction
        
    Returns:
        bacteria: List contain bacteria agents that have moved accordingly

    Raises:
        IOError: An error occurred accessing the bigtable.Table object.
        
    TODO make probabilities of wind direction inputs into this function
    TODO think about possibility of bacteria entering infinite loop due to 
    prob_up being larger than prob_down     
    """    
 
    # Initiate bacteria list
    bacteria = []
    for i in range(num_bact):
        # Add bacteria agent to list
        bacteria.append(FrameWork.Bacteria(elevation, bomb_origin, wind_probabilities, heatmap))
        # End the movement of bacteria when it hits ground
        while bacteria[i].elevation != 0:
            # Move bacteria in Z plane
            bacteria[i].elevate()
            # Move bacteria in XY plane
            bacteria[i].plane_move()
        # mark landing location of bacteria 
        bacteria[i].mark_heatmap() 
    return bacteria

    
def write_results(heatmap):
    """ Writes heatmap describing the final resting locations of the bacteria
    to a CSV file


    Args:
        heatmap: heatmap of landing locations of bacteria
        
    Returns:
        CSV file in 
        
    """    
    data_list = heatmap
    # Define delimiter and file name to be written
    with open('ResultHeatmap.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerows(data_list)


def calc_distances(bomb_origin, agents):
    """ Function to calculate the distance each bacteria has travelled from 
    bomb origin

    Args:
        agents: list of bacteria
        
    Returns:
        CSV file in 
        
        
    TODO: Not working quite as expected    
    """    
    distances = []
    for i in range(len(agents)):
        print(len(agents))
        # Use pythagoras to define distances
        dist = ((bomb_origin[0] - agents[i].bomb_origin_y)**2+ (bomb_origin[1]
        - agents[1].bomb_origin_x)**2)**0.5
        distances.append(dist)
        print(len(distances))
        return distances
    print(distances)
        
        
        


if __name__ == "__main__":
    #Define intial conditions of model
    num_bact = 5000
    elevation = 75
    #Define probabilites. 
    # TODO: anyway to make this a bit slicker and neater
    #? [COMPLETED: Put in a list]
    prob_north = 0.75
    prob_west = 0.1
    prob_east =  0.05
    prob_south = 0.1
    prob_up = 0.2
    prob_level = 0.1
    prob_down = 0.7
    # Place probabilities within a list. This is purely to reduce amount of
    # arguments input into future functions
    wind_probabilities = [prob_north, prob_west, prob_east, prob_south, 
                         prob_up, prob_level, prob_down]

    
    #Find origin of bomb
    enviroment = open_environment()
    bomb_origin = find_bomb_origin(enviroment)
    # Create blank heatmap to be marked. BLank heatmap set to match dimensions 
    # of environment
    heatmap = create_blank_heatmap(len(enviroment))
    
    #Input ICs and move bacteria
    bacteria = move_bacteria(bomb_origin, num_bact, elevation,
                             wind_probabilities, heatmap)
    times = []
    for i in range(len(bacteria)):
        times.append(bacteria[i].hangtime)
        
    #x = calc_distances(bomb_origin, bacteria)
    #print(x)
    #matplotlib.pyplot.boxplot(x)
    
    matplotlib.pyplot.xlim(0, 300)
    matplotlib.pyplot.ylim(0, 300)
    
    
    matplotlib.pyplot.imshow(bacteria[0].heatmap)
    matplotlib.pyplot.scatter(50, 150, s = 8, color = "yellow", marker  = "*")

    # matplotlib.pyplot.scatter(matplotlib.pyplot.scatter(bomb_origin[0], bomb_origin[1]))
    
    matplotlib.pyplot.show()
    write_results(bacteria[0].heatmap)
#        
    

    
    