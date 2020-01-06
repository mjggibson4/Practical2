"""A python script that defines the behaviour of a plume of bacteria

v1.4

This script defines a bacteria class. Tthe movement of bacteria from a single release point. This
origin is located via an associated .txt file from which the coordinates are
extracted. The bacteria are individually moved both vertically and horizontally
from this point based on predefined probably which model wind behaviour. The 
landing point of each bacterium is recorded from which a heat map is produced.

"""
import random

class Bacteria:
    """ Defines a bacteria agent within the model

    Bacteria class. Defines characteristics of the bacteria. The probabilities 
    governining this movement is held with a list containing six elements. 
    These elements are extracted and assigned to appropriately named variables.

    Attributes:
        elevation: elevation of bomb 
        bomb_origin: List containing XY coordinates of bomb location 
        wind_probabilities: List of wind probabilities
        heatmap: blank enviroment in which the landing locations of the bacteria
        will be recorded. 
    """


    def __init__(self, elevation, bomb_origin, wind_probabilities, heatmap):
        """Inits bacteria with environment, agents elevation, bomb_origin,
        wind_probabilities, heatmap
        ."""
        
        # extract bomb origin from list
        self.bacteria_y = bomb_origin[0]
        self.bacteria_x = bomb_origin[1]
            
        self.heatmap = heatmap
        self.elevation = elevation  
        
        # Extract contents of wind_probabilities list
        self.prob_north = wind_probabilities[0]
        self.prob_west = wind_probabilities[1]
        self.prob_east = wind_probabilities[2]
        self.prob_south = wind_probabilities[3]
        self.prob_up = wind_probabilities[4]
        self.prob_level = wind_probabilities[5]
        self.prob_down = wind_probabilities[6]
        
        # Set counter to record the time taken for particle to hit ground
        self.hangtime = 0

    def elevate(self):        
            """ Function that defines the movement of bacteria in z direction
            
            Function moves particle based on a set of probabilites in the up
            ,down and level direction above 75m. Below this the particle is set
            to fall 1m at every time step.
        
            Args:
                Self: Parameters defined within __init__ 
        
            Returns:
                N/A
       
            Raises:
                N/A    
                .
            """
            
            # Move bacteria in z direction
            # Generate random number from which elevation movement will be governed
            rand1 = random.random()
            # If random number is less or equal to "up" probability 
            # and elevation is greater or equal to 75 increase elevation
            if rand1 <= self.prob_up and self.elevation >= 75:
                self.elevation += 1
            # Sum up and level probabilities. If random number is less than
            # this and elevation is greater or equal to 75 hold elevation
            elif rand1 <= (self.prob_up + self.prob_level) and self.elevation >= 75:
                self.elevation = self.elevation 
            # Otherwise decrease height by 1 unit
            else:
                self.elevation -= 1
            # Increment time counter by 1    
            self.hangtime += 1
                
                
    def plane_move(self):
            """ Function that defines the movement of bacteria in XY direction
        
            The bacteria can move in four defined directions in the XY plane: 
            North, West, South and East. These four movements have associated probablities
            and the direction taken is governed by a randomly generated number. 
            
            Args:
                N/A
        
            Returns:
                N/A
        
            Raises:
                N/A        
            """    
            
            # Move bacteria in xy plane 
            # Generate random number from which xy movement will be decided
            randnum = random.random()
            # Move bacteria in -ve x direction
            if randnum  <= self.prob_west:
                self.bacteria_x -= 1#
            # Move bacteria in -ve y direction    
            elif randnum <= (self.prob_west + self.prob_south):
                self.bacteria_y  -= 1
            # Move bacteria in +ve y direction     
            elif randnum <= (self.prob_west + self.prob_south + self.prob_north):
                self.bacteria_y += 1
            # Move bacteria in +ve x direction       
            else:
                self.bacteria_x += 1             
                
    def mark_heatmap(self):
            # Function marks the final landing locations of the bacteria
            final_y = int(self.bacteria_y)
            final_x = int(self.bacteria_x)
            # Don't mark anything outside BCs
            if 0 <= final_y <= len(self.heatmap) and 0 <= final_x <= len(self.heatmap):
                self.heatmap[final_y][final_x] += 1

__author__ = "Michael Gibson"
__copyright__ = "Copyright 2020, Michael Gibson"
__license__ = "MIT"
__version__ = "1"
__maintainer__ = "Michael Gibsosn"
__email__ = "mjggibson4@gmail.com"
__status__ = "Production"  


 
                
