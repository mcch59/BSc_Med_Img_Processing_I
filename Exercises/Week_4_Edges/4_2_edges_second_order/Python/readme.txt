Regarding "4_2_Demo.py": Use "Achteck.png" for the demonstration first and show two things: 

First, show that second order edges do not contain information about gradient directions. 

Second, show that there are two kinds of edges: The outermost pixels that are still part of the object and the other one being the pixels surrounding the object. Both are detected with Laplacian filter at the same time. The positive values belong to one kind of edge (part of object or part of the contour) and the negative values belong to the other kind of edge.