import numpy as np
from ipywidgets import interact, fixed
from PIL import Image

img= Image.open("C:\Users\sfdra\Desktop\FAU 1st semester\DSSS\Exercise3\du82dady\home.jpg")

print(type(img))

numpy= np.array(img)
print(numpy.dtype)
print(numpy.shape)
print(img.size)


resize= img.resize((400,400))
print(resize)
resize.show()
  
 
