import numpy as np

def median_filter(image, filter_radius = 1): 
    
    filtered_image = image.copy() 
    
    for row in range(filter_radius, image.shape[0]-filter_radius): 
        for column in range(filter_radius, image.shape[1]-filter_radius): 
            
            umgebung = image[row-filter_radius:row+filter_radius+1, 
                             column-filter_radius:column+filter_radius+1]
            
            filtered_image[row, column] = np.median(umgebung)
            
    return filtered_image

def mean_filter(image, filter_radius = 1): 
    
    filtered_image = image.copy() 
    
    for row in range(filter_radius, image.shape[0]-filter_radius): 
        for column in range(filter_radius, image.shape[1]-filter_radius): 
            
            umgebung = image[row-filter_radius:row+filter_radius+1, 
                             column-filter_radius:column+filter_radius+1]
            
            filtered_image[row, column] = np.mean(umgebung)
            
    return filtered_image