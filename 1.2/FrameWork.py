"""A python script that defines the behaviour of a plume of bacteria

v1.2

This script defines a bacteria class. Tthe movement of bacteria from a single release point. This
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
Initial Conditions dealt with in mark_heatmap
"""



import random

class Bacteria:
    """ Defines a bacteria agent within the model

    Bacteria class. Defines characteristics of the bacteria. The probabilities 
    governining this movement is held with a list containing six elements. 
    These elements are extracted and assigned to appropriately named variables.

    Attributes:
        agents: elevation of bomb 
        bomb_origin: List containing XY coordinates of bomb location 
        wind_probabilities: List containing probabilities which define which
        heatmap: blank enviroment in which the landing locations of the bacteria
        will be recorded. 
    """

    def __init__(self, elevation, bomb_origin, wind_probabilities, heatmap):
        """Inits Agent with environment, agents, _y and _x."""
    
        import random
        # If x null assign random value
        if (bomb_origin[0] == None):
            self.bomb_origin_y = random.randint(0,100)
        else:
            self.bomb_origin_y = bomb_origin[0]
        # If y null assign random value    
        if (bomb_origin[1] == None):
            self.bomb_origin_x = random.randint(0,100)
        else:
            self.bomb_origin_x = bomb_origin[1]
            
        # Set counter to record the time taken for particle to hit ground
        self.hangtime = 0
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

    def elevate(self):        
            """ Function that defines the movement of bacteria in z direction
        
            The bacteria can move in three defined directions: up, down or keep
            a constant z value. These three movements have associated probablities
            and the direction taken is governed by a randomly generated number. 
            
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
            # Move bacteria in z direction
            # Generate random number from which elevation movement will be defined
            rand1 = random.random()
            if rand1 <= self.prob_up and self.elevation >= 75:
                self.elevation += 1
            # 10% chance of bacteria keeping a constant z value    
            elif rand1 <= (self.prob_up + self.prob_level) and self.elevation >= 75:
                self.elevation = self.elevation # don't think this is needed maybe switch ifs about
            # 70% chance of bacteria moving in -ve z direction
            else:
                self.elevation -= 1
            self.hangtime += 1
                
                
    def plane_move(self):
            """ Function that defines the movement of bacteria in XY direction
        
            The bacteria can move in four defined directions in the XY plane: 
            North, West, South and East. These four movements have associated probablities
            and the direction taken is governed by a randomly generated number. 
            
            Args:
                N/A
        
            Returns:
                environment: list containing bombing location
        
            Raises:
                TODO: Scrape environment for web
                TODO: Raise error if file not found - although let program run if
                available.
                Try except set up in order to facilitate this.
            """    
            
            #Move bacteria in xy plane 
            # Generate random number from which xy movement will be decided
            randnum = random.random()
            # 5% chance of bacteria moving in -ve x direction
            if randnum  <= self.prob_west:
                self.bomb_origin_x -= 1#
            # 10% chance of bacteria moving in -ve y direction    
            elif randnum <= (self.prob_west + self.prob_south):
                self.bomb_origin_y  -= 1
            # 10% chance of bacteria moving in +ve y direction     
            elif randnum <= (self.prob_west + self.prob_south + self.prob_north):
                self.bomb_origin_y += 1
            # 75% chance of bacteria moving in ve x direction       
            else:
                self.bomb_origin_x += 1             
                
    def mark_heatmap(self):
            
            

            # Function marks the final landing locations of the bacteria
            final_y = int(self.bomb_origin_y)
            final_x = int(self.bomb_origin_x)
            # Don't mark anything outside BCs
            try:
                if 0 <= final_y <= len(self.heatmap) and 0 <= final_x <= len(self.heatmap):
                    self.heatmap[final_y][final_x] += 1
            except:
                print(final_y ,final_x)
                   
    
#    def distance_travelled(self, num_bact):
#        distances = []
#        for i in num_bact:   
#            dist = ((self.bomb_origin_y-final_loc[i][0])**2- (self.bomb_origin_x-final_loc[i][1])**2)
#            distances.append(dist)
#            return distances
        


 
                
