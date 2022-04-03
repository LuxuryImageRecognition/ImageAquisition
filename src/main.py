import os
from tkinter.tix import IMAGE 

# importing google_images_download module
from google_images_download import google_images_download 

IMAGE_FOLDER = "images"

# creating object
client = google_images_download.googleimagesdownload() 
  
search_query = "Louis Vuitton Alma bag"
      
def downloadimages(query):
    print(query)
    # keywords is the search query
    # format is the image file format
    # limit is the number of images to be downloaded
    # print urs is to print the image file url
    # size is the image size which can
    # be specified manually ("large, medium, icon")
    # aspect ratio denotes the height width ratio
    # of images to download. ("tall, square, wide, panoramic")
    arguments = {"keywords": query,
                 "format": "jpg",
                 "limit":10,
                 "print_urls":True,
                 "size": "medium",
                 "output_directory": IMAGE_FOLDER
                 }
  
    client.download(arguments)

if not os.path.exists(IMAGE_FOLDER):
    os.makedirs(IMAGE_FOLDER)   
  
# Driver Code
downloadimages(search_query) 
 
