import requests
import os

# define the base URL for the images
base_url = "https://www.youknowthewebsite.com/gallery/"
# define the total number of stickers in each series
num_stickers = [20 , 40, 20, 20, 42, 20, 9]
prefixes = ["alternative", "classicrock", "metal", "newwave", "pop", "rap", "hardrock"]

counter = 1
# iterate through each series
for i in range(1, len(num_stickers)+1):
    prefix = "bands"
    # generate the series folder name and file name prefix
    series_folder = prefix
    file_prefix = prefix + "_" + prefixes[i-1] + "_"
    
    # iterate through each sticker in the series
    for j in range(1, num_stickers[i-1]+1):
        # generate the URLs for the "a" and "b" stickers
        url_a = base_url + series_folder + "/" + file_prefix + str("{:03d}".format(j)) + ".jpg"
         
        # make a GET request for the "a" sticker and save the image
        if not os.path.exists(file_prefix + str(j) + ".jpg"):
            response_a = requests.get(url_a)
            with open(file_prefix + str(j) + ".jpg", "wb") as f:
                f.write(response_a.content)
        counter += 1
