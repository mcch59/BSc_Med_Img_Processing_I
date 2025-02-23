import matplotlib.pyplot as plt 
import numpy as np 

def my_filter_1(image, filter_radius = 1): 
    
    max_filtered_image = np.zeros(shape = image.shape)
    for row in range(filter_radius, image.shape[0]-filter_radius):
        for column in range(filter_radius,image.shape[1]-filter_radius):
            new_val = np.max(image[row-filter_radius:row+filter_radius+1, 
                                   column-filter_radius:column+filter_radius+1])

            max_filtered_image[row, column] = new_val
            

    return max_filtered_image


def my_filter_2(image, filter_radius = 1):
    min_filtered_image = np.zeros(shape = image.shape)
    for row in range(filter_radius, image.shape[0]-filter_radius):
        for column in range(filter_radius,image.shape[1]-filter_radius):
            new_val = np.min(image[row-filter_radius:row+filter_radius+1, 
                                   column-filter_radius:column+filter_radius+1])

            min_filtered_image[row, column] = new_val
    return min_filtered_image