import requests
import os

# define the base URL for the images
base_url = "https://www.youknowthewebsite.com/gallery/"

# define the total number of stickers in each series
num_stickers = [41, 42, 41, 42, 40, 44, 42, 42, 44, 39, 42, 41, 40, 40, 40, 41]

counter = 1
# iterate through each series
for i in range(1, 17):
    
    # generate the series folder name and file name prefix
    series_folder = "os" + str(i)
    file_prefix = "os" + str(i) + "_back_"
    
    # iterate through each sticker in the series
    for j in range(1, num_stickers[i-1]+1):
        # generate the URLs for the "a" and "b" stickers
        url_a = base_url + series_folder + "/backs/" + file_prefix + str(counter) + "ab.jpg" 
         
        # make a GET request for the "a" sticker and save the image
        if not os.path.exists(file_prefix + str(counter) + "ab.jpg"):
            response_a = requests.get(url_a)
            with open(file_prefix + str(counter) + "ab.jpg", "wb") as f:
                f.write(response_a.content) 
        counter += 1
