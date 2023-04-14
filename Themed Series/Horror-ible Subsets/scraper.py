import requests
import os

# define the base URL for the images
base_url = "https://www.youknowthewebsite.com/gallery/"
# define the total number of stickers in each series
num_stickers = [15, 10, 15, 10, 10, 15, 5, 15, 15]
prefixes = ["80horror", "80scifi", "classicfilm", "classic", "folklore", "modhorror", "modscifi", "rethorror", "retscifi"]
counter = 1
# iterate through each series
for i in range(1, 10):
    prefix = "oth"
    # generate the series folder name and file name prefix
    series_folder = prefix
    file_prefix = prefix + "_" + prefixes[i-1] + "_"
    
    # iterate through each sticker in the series
    for j in range(1, num_stickers[i-1]+1):
        # generate the URLs for the "a" and "b" stickers
        url_a = base_url + series_folder + "/" + file_prefix + str(j) + "a.jpg"
        url_b = base_url + series_folder + "/" + file_prefix + str(j) + "b.jpg"
         
        # make a GET request for the "a" sticker and save the image
        if not os.path.exists(file_prefix + str(j) + "a.jpg"):
            response_a = requests.get(url_a)
            with open(file_prefix + str(j) + "a.jpg", "wb") as f:
                f.write(response_a.content)
    
        # make a GET request for the "b" sticker and save the image
        if not os.path.exists(file_prefix + str(j) + "b.jpg"):
            response_b = requests.get(url_b)
            with open(file_prefix + str(j) + "b.jpg", "wb") as f:
                f.write(response_b.content)
        counter += 1