import numpy as np
import matplotlib.pyplot as plt


#coef:the coefficients of the polynomial starting from z^0
#width,heigth: image resolution
#real_min,real_max: Maximum and minimum of real axis
# imag_min, imag_max: Maximum and minimum in the imaginary axis
# max_iter:Maximum iteration of the loop that iterates the function


def julia_set(coef:list, width:float, height:float, real_min:float, real_max:float, imag_min:float, imag_max:float, max_iter:int)-> list:
    real_vals = np.linspace(real_min, real_max, width)
    imag_vals = np.linspace(imag_min, imag_max, height)
    picture = np.zeros((width, height))

    
    #returns the p(z) where p is the polynomial with the specified coefficients

    def polynomial(coefficients:list,z:complex):
        return(sum([coefficients[i]*z**i for i in range(len(coefficients))]))
    bound=5/(abs(coef[len(coef)-1])**(1/(len(coef)-1)))
    for x in range(width):
        for y in range(height):
            z = complex(real_vals[x], imag_vals[y])
            iteration = 0
            while abs(z) <= bound  and iteration < max_iter:
                z = polynomial(coef,z)
                iteration += 1
            picture[x, y] = iteration / max_iter
    
    return picture

def plot_julia_set(coef, width, height, real_min, real_max, imag_min, imag_max, max_iter):
    picture = julia_set(coef, width, height, real_min, real_max, imag_min, imag_max, max_iter)
    #this is an array with a number corresponding to each pixel on the screen. 
    # Pixels are determined by width and height and each number between 0 and 1 shows what percentage of max iterations each point used before becoming large enough. 
    # Points in the filled Julia set always use all iterations. 
    
    plt.imshow(picture, extent=(real_min, real_max, imag_min, imag_max),cmap="plasma")
    #this plots the 2d array. cmap tells you the color, extend tells you the frame dimensions of the picture


    plt.title(f"Julia Set for poly = {coef}")
    plt.xlabel('Real')
    plt.ylabel('Imaginary')
    plt.colorbar()
    plt.show()
#these add labels
    
# Define parameters
width, height = 1000, 1000
real_min, real_max = -2, 2
imag_min, imag_max = -2, 2
max_iter =200

# List of coefficients to plot Julia sets for
coef_values = [complex(-0.7, 0.27015), complex(-0, 0),complex(1,0)]

# Plot Julia sets for each value of c

plot_julia_set(coef_values, width, height, real_min, real_max, imag_min, imag_max, max_iter)
