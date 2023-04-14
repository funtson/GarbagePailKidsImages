import requests
import os

# define the base URL for the images
base_url = "https://www.youknowthewebsite.com/gallery/"

# define the total number of stickers in each series
num_stickers = [25, 10, 5, 7, 5, 10, 10, 10, 10, 6, 10]
prefixes = ["80s", "influence", "interp", "comic", "cutting", "button", "kids", "pets", "pres", "lost", "zoom"]
counter = 1
# iterate through each series
for i in range(3, 12):
    prefix = "xxx"
    # generate the series folder name and file name prefix
    series_folder = "xxx"
    file_prefix = "xxx_" + prefixes[i-1] + "_"
    
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
