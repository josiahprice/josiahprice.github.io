import matplotlib.pyplot as plt
import os.path

def create_graph():

    # Naming the current directory
    directory = os.path.dirname(os.path.abspath(__file__))  
    
    # Create lists for x and y values
    years=[]
    number_of_deaths=[]
    
    # For each year from 1880 to 2012...
    filename = os.path.join(directory, 'CausesOfDeath_France_2001-2008.csv')
    datafile = open(filename,'r') # 'r' means 'read-only'
    next(datafile)
        
    # For each line in the file...
    for line in datafile:
        # Split the line into the three separate pieces of info
        year, cause_of_death, number = line.split(',')
        
        # line_data = line.split(',')
        # year = line_data[1]
        
        # If the name matches...
        if cause_of_death == 'Influenza':
            # Add the x and y values to the lists
            years.append(year)
            number_of_deaths.append(number)           
    datafile.close()
        
    fig, ax = plt.subplots(1,1)
    ax.bar(years, number_of_deaths)
    ax.set_ylabel('Number of Deaths')
    ax.set_xlabel('Year')
    ax.set_title('Influenza Deaths in France over Time')
    fig.show()

create_graph()