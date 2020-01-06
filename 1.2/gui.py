#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Launches a GUI from which the plume model can be run.

This script constructs a User Interface from which a population model is run.
The GUI contains two menus: model and help. This GUI allows users to change
the initial conditions of the model and calls the script MainCode from which
contains the code by which the model is actually run.

  Typical usage example:

  launch_GUI
"""

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot
import Maincode
import tkinter as tk
from tkinter import messagebox


    
def launch_gui():
    """Launches master GUI window from which the Population Model can be run.
 
    Launces a GUI in which the user can edit the initial conditions of the
    population model and run a simulation. This GUI hosts a canvas in which 
    the spatial behaviour of the agents (wolves and sheep) can be observed.

    Args:
        N/A

    Returns:
        A fully formed GUI with the following menus available for the user to
        interact with a run the population model:
            
            Cascade Menu - Run:
                Run - Commands program to run the population model using the
                parameters defined.
                
                Set Parameters - Calls the function SetParameters() in which
                the default values of num_of_sheep, num_of_iterations, 
                neighbourhood and num_of_wolves, wolf_threshold and 
                sheep_threshold can all be redefined.
                
                Exit - Closes model window
                
                
            Cascade Menu: Help
                Help: Opens a URL directing the user to the help files
                associated with this population model,
                About: Provides the users with some rudimentary details of the
                program itself such as version number and author.

    Raises:
        N/A
    """
    
    # Define user parameters as global variables. This allows for the function
    # SetParameters() to redefine these values if needed.
    global num_bact
    global elevation 
    global prob_north 
    global prob_west
    global prob_east
    global prob_south 
    global prob_up
    global prob_level 
    global prob_down
  
    num_bact = 5000
    elevation = 75
    #   Define initial parameters for model. These are the parameters that are
    #   to used if the user chooses not to redefine them.
    prob_north = 0.1
    prob_west = 0.05
    prob_east =  0.75
    prob_south = 0.1
    prob_up = 0.2
    prob_level = 0.1
    prob_down = 0.7
    

    
    #Create main GUI window and associate it with a canvas 
    fig = matplotlib.pyplot.figure()
    
    root = tk.Tk()
    root.wm_title("Model")
    canvas = (matplotlib.backends.backend_tkagg.
              FigureCanvasTkAgg(fig, master=root))
    canvas.draw()
    canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    
    #Create menu bar for the main GUI window
    menu_bar = tk.Menu(root)
    root.config(menu=menu_bar)
    model_menu = tk.Menu(menu_bar)
    
    #Add Model menu to the GUI with the commands Run, SetParameters and Exit
    menu_bar.add_cascade(label="Model", menu=model_menu)
    (model_menu.add_command(label="Run model", command = lambda: 
    Maincode.run(canvas, num_bact, elevation, prob_north, prob_west, prob_east, 
                        prob_south, prob_up, prob_level, prob_down)))
    (model_menu.add_command(label="Set Parameters", 
                            command = lambda: set_parameters()))
    model_menu.add_separator()
    model_menu.add_command(label="Exit", command= lambda: root.destroy())
    
    
    #Add help menu with the commands help and about   
    help_menu = tk.Menu(menu_bar)
    menu_bar.add_cascade(label="Help", menu=help_menu)
    help_menu.add_command(label="About", command = lambda: show_about_info())
    help_menu.add_command(label="Help", command= lambda: show_help_info())
       
    tk.mainloop()


def set_parameters():
    """Creates a GUI in which users can redefine initial model conditions.

    Creates a GUI in which the model variables num_of_sheep, num_of_iterations, 
    neighbourhood and num_of_wolves, wolf_threshold and sheep_threshold can be 
    redefined by the user. These variables are validated and redefined within 
    the pass_entry_fields function

    Args:
        6 user inputs:
            
       num_of_sheep = Number of sheep in initial iteration
       num_of_wolves = Number of wolves in initial iteration
       neighbourhood = range at which sheep can share resources
       num_of_iterations = number of moves allowed from each agent
       wolf_threshold = Number of sheep needed to be consumed for 
                        wolves to reproduce
       sheep_threshold = Store size needed for sheep to reproduce
            
    Returns:
        N/A: Redefined model conditions returned within pass_entry_fields 
        function

    Raises:
        N/A: Parameters validated within pass_entry_fields function
        
        
    Acknowledgements: Code modified from https://www.python-course.eu/
    tkinter_entry_widgets.php

    Klein, B. (2019). Entry Widgets. Available: https://www.python-course.eu/
    tkinter_entry_widgets.php. Last accessed 1st Dec 2019.    
    """

  
    def pass_entry_fields():
        """Validates user input from Set_Parameter module.
        
        Takes the values that the user has entered into the set parameters 
        window and checks that these values are integers. If these
        values are valid the global variables num_of_sheep, num_of_iterations, 
        neighbourhood, num_of_wolves wolf_threshold and sheep_thershold
        are all redefined. If values are negative, absolute values are taken 
        to prevent system errors
        
        Args:
            e1: temp variable for num_of_sheep
            e2: temp variable for num_of_wolves
            e3: temp variable for neighbourhood
            e4: temp variable for num_of_iterations
            e5: temp variable for wolf_threshold
            e6: temp variable for sheep_threshold
 
        
        Returns:
            num_of_sheep
            num_of_iterations
            neighbourhood
            num_of_wolves
            wolf_threshold 
            sheep_threshold
        
        Raises:
            Message Box: "All values must be positive integers"
        """   
      
        try:
            global num_bact
            global elevation 
            global prob_north 
            global prob_west
            global prob_east
            global prob_south 
            global prob_up
            global prob_level 
            global prob_down
            
            xy_prob = [float(e3.get()), float(e4.get()), float(e5.get()), float(e6.get())]
            z_prob = [float(e7.get()), float(e8.get()), float(e9.get())]
            

            
#            xy_prob_total = abs(float(e3.get())) + abs(float(e4.get())) + abs(float(e5.get())) + abs(float(e6.get()))
#            z_prob_total = abs(float(e7.get())) + abs(float(e8.get())) + abs(float(e9.get()))
                
            if all(i >= 0 for i in xy_prob) == True and sum(xy_prob) == 1 and sum(z_prob) ==1 and all(i >= 0 for i in z_prob) == True:
                
                prob_north = float(e3.get())
                prob_west = float(e4.get())
                prob_east =  float(e5.get())
                prob_south = float(e6.get())
                prob_up = float(e7.get())
                prob_level = float(e8.get())
                prob_down = float(e9.get())
                
            else:
                print('Wank')
                messagebox.showerror("Error", "Probabilities must add to 1")
                print(float(e3.get()) + float(e5.get()) + float(e6.get()) + float(e7.get()))        
                
            if int(e1.get()) > 0 and int(e2.get()) > 0:
                num_bact = int(e1.get())
                elevation = int(e2.get())
                master.destroy()  
            else: 
                messagebox.showerror("Error", "Number of Bacteria and Elevation values must be positive integers") 
        except:
            messagebox.showerror("Error", "Values must be numeric")
    # Create Set Parameters Window
    master = tk.Tk()   
    master.wm_title("Set Parameters")   
    # Define entry box labels
    tk.Label(master, text= "Initial Conditions").grid(row=0, column= 0,
            sticky='W')
    tk.Label(master, text= "Number of Bacteria").grid(row=1, column= 0,
            sticky='W', pady=4)
    tk.Label(master, text= "Elevation").grid(row=2, column= 0,
            sticky='W')
    tk.Label(master, text= "XY Probabilities").grid(row=3, column= 0,
            sticky='W')
    tk.Label(master, text= "Z Probabilities").grid(row=3, column= 3,
            sticky='W')
    tk.Label(master, text= "North").grid(row=4, column= 0,
            sticky='W')
    tk.Label(master, text= "West").grid(row=5, column= 0,
            sticky='W')
    tk.Label(master, text= "East").grid(row=6,
            column= 0, sticky='W', pady=4)
    tk.Label(master, text= "South").grid(row=7,
            column= 0, sticky='W')
    tk.Label(master, text= "Up").grid(row=4,
            column= 3, sticky='W')
    tk.Label(master, text= "Level").grid(row=5,
            column= 3, sticky='W')
    tk.Label(master, text= "Down").grid(row=6,
            column= 3, sticky='W')


    
    # Define entry boxes
    e1 = tk.Entry(master)
    e2 = tk.Entry(master)
    e3 = tk.Entry(master)
    e4 = tk.Entry(master)
    e5 = tk.Entry(master)
    e6 = tk.Entry(master)
    e7 = tk.Entry(master)
    e8 = tk.Entry(master)
    e9 = tk.Entry(master)
    
    # Insert default values for user input boxes
    e1.insert(10, num_bact)
    e2.insert(10, elevation)
    e3.insert(10, prob_north)
    e4.insert(10, prob_west)
    e5.insert(10, prob_east)
    e6.insert(10, prob_south)
    e7.insert(10, prob_up)
    e8.insert(10, prob_level)
    e9.insert(10, prob_down)

    
    # Define location of entry boxes
    e1.grid(row=1, column=2)
    e2.grid(row=2, column=2)
    e3.grid(row=4, column=2)
    e4.grid(row=5, column=2)
    e5.grid(row=6, column=2)
    e6.grid(row=7, column=2)
    e7.grid(row=4, column=4)
    e8.grid(row=5, column=4)
    e9.grid(row=6, column=4)
        
    #Create button to apply new parameters 
    tk.Button(master, text='Apply', command = lambda: pass_entry_fields()).grid(row=11, 
                                                                   column=0, 
                                                                   sticky=tk.W, 
                                                                   pady=4)
    # Creat button to close Set parameters window
    tk.Button(master, 
              text='Cancel', 
              command = lambda: master.destroy()).grid(row=11, 
                                        column=1, 
                                        sticky=tk.W, 
                                        pady=4)    

        
def show_about_info():
# Function to show rudimental information regarding population model   
    messagebox.showinfo("About", "Population Model \n\n" "Author: Michael Gibson\n" 
                        "Version: 1\n" "Released: Dec, 2019")
 
    
def show_help_info():
# Function to show help information regarding population model
    messagebox.showinfo("Help", "Instructions on running this program and troubleshooting tips can be found here:\n" 
                        "https://github.com/mjggibson4/Practical1/tree/master")

if __name__ == "__main__":
    #If main program launch GUI and wait for user interaction
    launch_gui()
    
__author__ = "Michael Gibson"
__copyright__ = "Copyright 201i, Michael Gibson"
__license__ = "MIT"
__version__ = "1"
__maintainer__ = "Michael Gibsosn"
__email__ = "mjggibson4@gmail.com"
__status__ = "Production"  
    
    
    