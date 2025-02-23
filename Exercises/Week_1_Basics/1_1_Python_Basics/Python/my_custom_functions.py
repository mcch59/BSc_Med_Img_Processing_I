def multiply(input_1, input_2):
    
    output = input_1 * input_2
    
    return output

def square_array(array):
    
    squared_array = array ** 2
    
    return squared_array


def search_for_large_values(array):
    
    rows = array.shape[0]
    columns = array.shape[1]
    
    for row in range(rows): 
        for column in range(columns):
            value = array[row, column]
            
            if value > array.max()/2: 
                print(value)