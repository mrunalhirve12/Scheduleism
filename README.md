Scheduling Simulator for CS 533 Spring 2018
Group Members: Nandadeep Davuluru, Manpreet Bahl, Thomas Salata, Saral Bhagat, Mrunal Hirve

Language: Python 3.5.2

IMPORTANT
    Before running the simulator, please install the Python packages detailed in the
    requirements.txt file. The pip command to do this is:
        pip3 install -r requirements.txt

Instructions for running the Web Application:
    Type the following command:
        python3 app.py
    Visit the site on: http://localhost:8000

Instructions for running the simulator through the Command Line:
    usage: simulator.py [-g] [-h] interrupt

    Required Arguments:
    interrupt         Timer Interrupt Value

    Optional Arguments:
    -g , --generate   Number of processes to generate for scheduler
    -h, --help        Show this help message.

Folders/Directories Navigation:
    legacy: Contains code and ZIP files of ways we tried to implement the simulator but ended up
            not being used. Rather than deleting them, they were moved to this folder
    
    report: Contains the final report of this project. This also contains a subfolder called 
            average_times which contains the raw data for the average graph in the report
    
    schedulers: Contains the implementation of the schedulers

    static: Where the graphs are saved as PNG files. Python Flask requires a folder called static
            for handling static files (JS, CSS etc.) and this also includes images
    
    templates: The HTML files are kept here. They are rendered through the Jinja templating engine
               when running the web application

Data Processing:
    When the simulation is done, there will be CSV files containing the raw data of the results
    for each of the schedulers. The script, procPlot.py, in the utils folder tackles the data
    processing and graph generation. The main() function in this script is called by both the
    web application and command line. The graphs are created as PNG files.
    

