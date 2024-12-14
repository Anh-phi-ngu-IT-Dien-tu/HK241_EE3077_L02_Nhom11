## In python we need these library
    * numpy (can be installed by type "pip install numpy" in terminal)
    * opencv (can be installed by type "pip install opencv-contrib-python" in terminal)
    * matplotlib (can be installed by type "pip install matplotlib" in terminal )
## Download Matlab R2023a to run these code 

## Note: in opencv, every images are read in color image even though they are black and white image
      if we want to have a true grayscale image, we must add this line of code
            I=cv.cvtColor(I,cv.COLOR_RGB2GRAY)

## Note: if we use grayscale code like above, it could generate weird image in plt.imshow()