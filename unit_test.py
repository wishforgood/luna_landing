import tifffile

# Read the TIFF file
img = tifffile.imread('./luna_landing_data/Lunar_LRO_LOLA_ClrShade_Global_128ppd_v04.tif')

# Display the image using matplotlib
import matplotlib.pyplot as plt

plt.imshow(img, cmap='gray')  # Use 'gray' for grayscale images
plt.show()