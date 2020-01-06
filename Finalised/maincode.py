# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 17:19:15 2019

@author: mjggi
"""

"""A python script modelling a plume of deadly bacteria in a spatial domain

v1.4

This script models the movement of bacteria from a single release point. This
origin is located via an associated .txt file from which the coordinates are
extracted. The bacteria are individually moved both vertically and horizontally
from this point based on predefined probably which model wind behaviour. The 
landing point of each bacterium is recorded from which a heat map is produced.

Changelog:

Production of statistics regarding plume (distance, time etc)
Final Verision
Comments revised and improved
"""


import csv
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot
import numpy
import framework
from tkinter import messagebox
import sys
import os
import random

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
        Warning: Raised if no bombing location found
        Error: Raised if two or more bombing locations found, out of scope and
        program terminates
    """
    
    #Extract coords of non zero element
    b_origin = numpy.nonzero(environment)
    # If one bombing location found, pass coordinates to a list
    if len(b_origin[0]) and len(b_origin[1]) == 1:
        bomb_origin = [int(b_origin[0]),int(b_origin[1])] 
        return bomb_origin
    # If more than one location found, terminate program. Out of scope for this
    # scenario
    elif len(b_origin[0]) >= 2 or len(b_origin[1]) >= 2:
        messagebox.showerror("Error", "More than one bombing location found. Scenario to be terminated")
        sys.exit()
    # If no bombing location found, assign as null in order to random assign
    # location within bacteria agent framework     
    else:
        bomb_origin = [random.randint(0, 300), random.randint(0, 300)]
        messagebox.showerror("Error", "No bombing location found. Random location to be used.")
        return bomb_origin        


def create_blank_heatmap(length):
    """Creates a blank square environment of defined size.

    This function creates a square enviroment containing exclusively zeros. To 
    be used to record the final landing positions of bacteria.
    
    Args:
        length: Length of square environment

    Returns:
        landscape: A square environmet containing purely '0'
    """
    # Create blank list
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
        
    """    
 
    # Initiate bacteria list
    bacteria = []
    for i in range(num_bact):
        # Add bacteria agent to list
        bacteria.append(framework.Bacteria(elevation, bomb_origin, wind_probabilities, heatmap))
        # End the movement of bacteria when it hits ground exits boundaries of
        # spatial domain or time exceeds 150 seconds
        while bacteria[i].elevation != 0 and bacteria[i].hangtime != 150 and bacteria[i].bacteria_y != 0 and bacteria[i].bacteria_x != 0 and bacteria[i].bacteria_y != 300 and bacteria[i].bacteria_x != 300:  
            # Move bacteria in Z plane
            bacteria[i].elevate()
            # Move bacteria in XY plane
            bacteria[i].plane_move()
        
        # If bacteria did land, mark on heatmap else alert user to unsuitable
        if bacteria[i].elevation == 0:    
            bacteria[i].mark_heatmap()
    return bacteria

    
def write_results(heatmap):
    """ Writes heatmap describing the final resting locations of the bacteria
    to a CSV file


    Args:
        heatmap: heatmap of landing locations of bacteria
        
    Returns:
        CSV file in directory from which this file is run
        
    """
    try:    
        data_list = heatmap
        # Define delimiter and file name to be written
        with open('ResultHeatmap.csv', 'w', newline='') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerows(data_list)
    except:
        messagebox.showerror("Error", "Unable to write CSV file. Please ensure you have write access to the directory {0}".format(os.getcwd()))
 
        



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
        if agents[i].elevation == 0:
        # Use pythagoras to define distances
            dist = ((bomb_origin[0] - agents[i].bacteria_y)**2+ (bomb_origin[1]
            - agents[i].bacteria_x)**2)**0.5
            distances.append(dist)
        else:
            next 
        #print(len(distances))
    return distances
        
        
def run(canvas, num_bact, elevation, prob_north, prob_west, prob_east, prob_south, prob_up, prob_level, prob_down):
    """Function used to pass parameters from GUI into bacterial bomb program itself

    Args:
        canvas: area in which heatmap is to be drawn
        num_bact: number of bacteria to move
        elevation: Elevation of bomb
        prob_north: Probability of particle moving in the positive y direction
        prob_south: Probability of particle moving in the negative y direction
        prob_west: Probability of particle moving in the negative x direction
        prob_east: Probability of particle moving in the positive x direction
        prob_up: Probability of particle moving in the positive z direction
        prob_level: Probability of particle keeping a constant z value
        prob_down: Probability of particle moving in the negative z direction
    """
    
    # Construct wind probabilites into a list to reduce arguements within functions
    wind_probabilities = [prob_north, prob_west, prob_east, prob_south, 
                         prob_up, prob_level, prob_down]
    
    # Open eniviroment containing bomb origin and find this coordinate
    environment = open_environment()
    bomb_origin = find_bomb_origin(environment)
    # Create heatmap on which landing locations are to be recorded
    heatmap = create_blank_heatmap(len(environment)+1)
    # Move bacteria
    bacteria = move_bacteria(bomb_origin, num_bact, elevation,
                             wind_probabilities, heatmap)
    
    # Plot results on GUI canvas
    matplotlib.pyplot.title('Bacterial Bomb - Landing Locations',fontsize= 12)
    matplotlib.pyplot.imshow(bacteria[0].heatmap, cmap = "RdYlGn_r")
    matplotlib.pyplot.xlim(0, len(environment))
    matplotlib.pyplot.ylim(0, len(environment))
    scale_bar = matplotlib.pyplot.colorbar()
    scale_bar.set_label('Number of Bacteria',fontsize= 12,rotation =90)
    # Plot bomb origin for some context
    bombstar = matplotlib.pyplot.scatter(bomb_origin[1], bomb_origin[0], s = 8, color = "yellow", marker  = "*")
    matplotlib.pyplot.legend((bombstar,), ('Bomb Origin',), bbox_to_anchor=(1,0), loc="lower right", fontsize= 6)
    # Write out results
    write_results(bacteria[0].heatmap)
    print('RUN COMPLETED')
    canvas.draw()

    # Prepare Statistics 
    # Calculate max and min distances travelled by bacteria
    distances = calc_distances(bomb_origin, bacteria)
    # Account for case where no bacteria hit ground
    if len(distances) == 0:
        max_dist = None
        min_dist = None
    else:
        max_dist = round(max(distances), 1)
        min_dist = round(min(distances), 1)
    
    hangtime = []
    bact_counter = 0
    # Calculate hangtimes and number of bacteria to hit ground
    for i in range(len(bacteria)):
        hangtime.append(bacteria[i].hangtime)
        # If bacteria hit the ground then add 1
        if bacteria[i].elevation == 0:
            bact_counter += 1    
    max_hangtime = max(hangtime)  
    min_hangtime = min(hangtime)       
        
    # Display statistics within messagebox
    messagebox.showinfo("Run Statistics", " Number of Bacteria:    {0} \n Bacteria to hit ground:    {1} \n Furthest distance travelled:    {2} \n Least distance travelled:    {3} \n Max hangtime:    {4} \n Min hangtime:    {5} ".format(num_bact, bact_counter, max_dist, min_dist, max_hangtime, min_hangtime))





if __name__ == "__main__":
    
    # Define initial parameters for model. These are the parameters that are
    # to used if the user chooses not to redefine them.   
    num_bact = 5000
    elevation = 75
    prob_north = 0.1
    prob_west = 0.05
    prob_east =  0.75
    prob_south = 0.1
    prob_up = 0.2
    prob_level = 0.1
    prob_down = 0.7
      
    """Function used to pass parameters from GUI into bacterial bomb program itself

    Args:
        canvas: area in which heatmap is to be drawn
        num_bact: number of bacteria to move
        elevation: Elevation of bomb
        prob_north: Probability of particle moving in the positive y direction
        prob_south: Probability of particle moving in the negative y direction
        prob_west: Probability of particle moving in the negative x direction
        prob_east: Probability of particle moving in the positive x direction
        prob_up: Probability of particle moving in the positive z direction
        prob_level: Probability of particle keeping a constant z value
        prob_down: Probability of particle moving in the negative z direction
    """
    
    # Construct wind probabilites into a list to reduce arguements within functions
    wind_probabilities = [prob_north, prob_west, prob_east, prob_south, 
                         prob_up, prob_level, prob_down]
    
    # Open eniviroment containing bomb origin and find this coordinate
    environment = open_environment()
    bomb_origin = find_bomb_origin(environment)
    # Create heatmap on which landing locations are to be recorded
    heatmap = create_blank_heatmap(len(environment)+1)
    # Move bacteria
    bacteria = move_bacteria(bomb_origin, num_bact, elevation,
                             wind_probabilities, heatmap)
    
    # Plot results on GUI canvas
    matplotlib.pyplot.title('Bacterial Bomb - Landing Locations',fontsize= 12)
    matplotlib.pyplot.imshow(bacteria[0].heatmap, cmap = "RdYlGn_r")
    matplotlib.pyplot.xlim(0, len(environment))
    matplotlib.pyplot.ylim(0, len(environment))
    scale_bar = matplotlib.pyplot.colorbar()
    scale_bar.set_label('Number of Bacteria',fontsize= 12,rotation =90)
    # Plot bomb origin for some context
    bombstar = matplotlib.pyplot.scatter(bomb_origin[1], bomb_origin[0], s = 8, color = "yellow", marker  = "*")
    matplotlib.pyplot.legend((bombstar,), ('Bomb Origin',), bbox_to_anchor=(1,0), loc="lower right", fontsize= 6)
    # Write out results
    write_results(bacteria[0].heatmap)
    print('RUN COMPLETED')


    # Prepare Statistics 
    # Calculate max and min distances travelled by bacteria
    distances = calc_distances(bomb_origin, bacteria)
    # Account for case where no bacteria hit ground
    if len(distances) == 0:
        max_dist = None
        min_dist = None
    else:
        max_dist = round(max(distances), 1)
        min_dist = round(min(distances), 1)
    
    hangtime = []
    bact_counter = 0
    # Calculate hangtimes and number of bacteria to hit ground
    for i in range(len(bacteria)):
        hangtime.append(bacteria[i].hangtime)
        # If bacteria hit the ground then add 1
        if bacteria[i].elevation == 0:
            bact_counter += 1    
    max_hangtime = max(hangtime)  
    min_hangtime = min(hangtime)       
        
    # Display statistics within messagebox
    messagebox.showinfo("Run Statistics", " Number of Bacteria:    {0} \n Bacteria to hit ground:    {1} \n Furthest distance travelled:    {2} \n Least distance travelled:    {3} \n Max hangtime:    {4} \n Min hangtime:    {5} ".format(num_bact, bact_counter, max_dist, min_dist, max_hangtime, min_hangtime))
    


__author__ = "Michael Gibson"
__copyright__ = "Copyright 2020, Michael Gibson"
__license__ = "MIT"
__version__ = "1"
__maintainer__ = "Michael Gibsosn"
__email__ = "mjggibson4@gmail.com"
__status__ = "Production"  
    
    
    