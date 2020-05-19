import requests
from bs4 import BeautifulSoup as bs
import os

# which year for which we want our comics for
year = input("Enter Year: ")
url = "http://explosm.net/comics/archive" #basic page of explosm

# setting up directory
os.mkdir("comics")
curr_path = os.path.join(os.getcwd(), "comics")

for i in range(1,13):
    # setting url for souping
    # if else due to site design of urls
    if i < 10:
        new_url = url + "/" + year + "/0" + str(i)
    else:
        new_url = url + "/" + year + "/" + str(i)

    # setting up page soup
    code = requests.get(new_url).text
    soup = bs(code, 'html.parser')
    
    k = 1    # image number for current month
    for link in soup.find_all("div", {"class":"small-3 medium-3 large-3 columns"}):

        # setting up new page url, code and soup
        page_url = "http://explosm.net" + link.a.get("href")
        page_code = requests.get(page_url).text
        page_soup = bs(page_code, 'html.parser')

        # setting image url
        image = page_soup.find("img", {"id":"main-comic"})
        image_url = "http:" + image.get("src")

        # catchy image name :p
        image_name = "Image_" + year + "_" + str(i) + "_" + str(k) + ".png"

        # location for img download
        img_path = os.path.join(curr_path, image_name)
        
        # downloading the image
        r = requests.get(image_url)
        with open(img_path, 'wb') as f:
            f.write(r.content)

        print(image_name + " downloaded")
        k = k + 1