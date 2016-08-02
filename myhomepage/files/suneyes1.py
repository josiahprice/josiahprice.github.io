'''hillarySunEyes demonstrates PIL.Image.paste()
Unpublished work (c)2013 Project Lead The Way
CSE Activity 1.3.7 PIL API
Version 8/01/2016 '''

import numpy as np
import PIL
import matplotlib.pyplot as plt
import os.path
import PIL.ImageDraw              


# Open the files in the same directory as the Python script
directory = os.path.dirname(os.path.abspath(__file__))  
hillary_file = os.path.join(directory, 'hillary.jpg')

# Open and show the hillary image in a new Figure window
hillary_img = PIL.Image.open(hillary_file)

width = hillary_img.size[0]
length = hillary_img.size[1]

my_mask = PIL.Image.new('RGBA', (width, length), (0, 0, 0, 0))
drawing_layer = PIL.ImageDraw.Draw(my_mask)
drawing_layer.ellipse((0, 0, width, length), fill=(255, 0, 0, 255))

result = PIL.Image.new('RGBA', (width, length))
result.paste(hillary_img, (0, 0), mask=my_mask)

fig, axes = plt.subplots(1, 3)
for i in range(3):
    axes[i].axis('off')
axes[0].imshow(hillary_img, interpolation='none')
axes[0].set_title('hillary_img')
axes[1].imshow(my_mask, interpolation='none')
axes[1].set_title('my_mask')
axes[2].imshow(result, interpolation='none')
axes[2].set_title('result')
fig.show()

fig, axes = plt.subplots(1, 2)
axes[0].imshow(hillary_img, interpolation='none')
axes[0].set_xlim(35, 416) #coordinates measured in plt, and tried in iPython
axes[0].set_ylim(501, 33)

def round_corners(original_image, percent_of_side):
    """ Rounds the corner of a PIL.Image
    
    original_image must be a PIL.Image
    Returns a new PIL.Image with rounded corners, where
    0 < percent_of_side < 1
    is the corner radius as a portion of the shorter dimension of original_image
    """
    #set the radius of the rounded corners
    width, height = original_image.size
    radius = int(percent_of_side * min(width, height)) # radius in pixels
    
    ###
    #create a mask
    ###
    
    #start with transparent mask
    rounded_mask = PIL.Image.new('RGBA', (width, height), (127,0,127,0))
    drawing_layer = PIL.ImageDraw.Draw(rounded_mask)
    
    # Overwrite the RGBA values with A=255.
    # The 127 for RGB values was used merely for visualizing the mask
    
    # Draw two rectangles to fill interior with opaqueness
    drawing_layer.polygon([(radius,0),(width-radius,0),
                            (width-radius,height),(radius,height)],
                            fill=(127,0,127,255))
    drawing_layer.polygon([(0,radius),(width,radius),
                            (width,height-radius),(0,height-radius)],
                            fill=(127,0,127,255))

    #Draw four filled circles of opaqueness
    drawing_layer.ellipse((0,0, 2*radius, 2*radius), 
                            fill=(0,127,127,255)) #top left
    drawing_layer.ellipse((width-2*radius, 0, width,2*radius), 
                            fill=(0,127,127,255)) #top right
    drawing_layer.ellipse((0,height-2*radius,  2*radius,height), 
                            fill=(0,127,127,255)) #bottom left
    drawing_layer.ellipse((width-2*radius, height-2*radius, width, height), 
                            fill=(0,127,127,255)) #bottom right
                         
    # Uncomment the following line to show the mask
    # plt.imshow(rounded_mask)
    
    # Make the new image, starting with all transparent
    result = PIL.Image.new('RGBA', original_image.size, (0,0,0,0))
    result.paste(original_image, (0,0), mask=rounded_mask)
    return result
    
def get_images(directory=None):
    """ Returns PIL.Image objects for all the images in directory.
    
    If directory is not specified, uses current directory.
    Returns a 2-tuple containing 
    a list with a  PIL.Image object for each image file in root_directory, and
    a list with a string filename for each image file in root_directory
    """
    
    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified
        
    image_list = [] # Initialize aggregaotrs
    file_list = []
    
    directory_list = os.listdir(directory) # Get list of files
    for entry in directory_list:
        absolute_filename = os.path.join(directory, entry)
        try:
            image = PIL.Image.open(absolute_filename)
            file_list += [entry]
            image_list += [image]
        except IOError:
            pass # do nothing with errors tying to open non-images
    return image_list, file_list

def round_corners_of_all_images(directory=None):
    """ Saves a modfied version of each image in directory.
    
    Uses current directory if no directory is specified. 
    Places images in subdirectory 'modified', creating it if it does not exist.
    New image files are of type PNG and have transparent rounded corners.
    """
    
    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified
        
    # Create a new directory 'modified'
    new_directory = os.path.join(directory, 'modified')
    try:
        os.mkdir(new_directory)
    except OSError:
        pass # if the directory already exists, proceed  
    
    #load all the images
    image_list, file_list = get_images(directory)  

    #go through the images and save modified versions
    for n in range(len(image_list)):
        # Parse the filename
        filename, filetype = os.path.splitext(file_list[n])
        
        # Round the corners with radius = 30% of short side
        new_image = round_corners(image_list[n],.30)
        #save the altered image, suing PNG to retain transparency
        new_image_filename = os.path.join(new_directory, filename + '.png')
        new_image.save(new_image_filename)    
# Display hillary in second axes and set window to the right eye
axes[1].imshow(hillary_img, interpolation='none')
axes[1].set_xlim(176,276) #coordinates measured in plt, and tried in iPython
axes[1].set_ylim(160, 126)

sun_file = os.path.join(directory, 'sun_1.jpg')
sun_img = PIL.Image.open(sun_file)
sun_small = sun_img.resize((21, 8)) #eye width and height measured in plt
fig2, axes2 = plt.subplots(1, 2)
axes2[0].imshow(sun_img)
axes2[1].imshow(sun_small)

result.paste(sun_small, (189, 148))
result.paste(sun_small, (245, 143)) 
# Display
fig3, axes3 = plt.subplots(1, 2)
for i in range(2):
    axes[i].axis('off')
axes3[0].imshow(result, interpolation='none')
axes3[1].imshow(result, interpolation='none')
axes3[1].set_xlim(176, 276)
axes3[1].set_ylim(160, 120)

fig3.show()