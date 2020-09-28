# Thank you for checking out my project. Hope you like it. The comments might help you for understanding. 
# Read the readme.md file for successful run of this program.

# ALL IMPORTS

from PIL import Image
import sys

# Function to split images in 5X5 grid.
def tileimage(image,count):
    image = Image.open(image)
    print(image.size[0],image.size[1])
    tile_width = image.size[0]/5
    tile_height = image.size[1]/5

    if image.size[0] % tile_width == 0 and image.size[1] % tile_height ==0 :
        currentx = 0
        currenty = 0
        offset = 5
        while currenty < image.size[1]:
            while currentx < image.size[0]:
    ##            print (currentx,",",currenty)
                tile = image.crop((currentx+offset,currenty+offset,currentx + tile_width - offset,currenty + tile_height - offset))
                tile.save(str(count)+".png","PNG")
                currentx += tile_width
                count+=1                
            currenty += tile_height
            currentx=0
    else:
        print ("sorry your image does not fit neatly into",
                    tile_width,"*",tile_height,"tiles")
