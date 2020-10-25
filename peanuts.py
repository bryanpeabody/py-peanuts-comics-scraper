from datetime import datetime
from datetime import timedelta
import urllib.request
import requests
from bs4 import BeautifulSoup
from urllib import request
import magic
import os
from sys import argv

# Get the start and end dates from the passed in parameters
start_date = ""
end_date = ""

try:
    start_date = datetime.strptime(argv[1], '%Y-%m-%d')
    end_date = datetime.strptime(argv[2], '%Y-%m-%d')
except:
    print("Please pass in valid start and end date parameters! ")
    exit(-1)

# Start and end dates were good, lets grab each comic strip for the date range
while start_date <= end_date:
    filename = "./images/" + start_date.strftime('%Y-%m-%d')  
    url = "https://www.gocomics.com/peanuts/" + start_date.strftime('%Y') + "/" + start_date.strftime('%m') + "/" + start_date.strftime('%d')

    # Read in the HTML from the URL
    fp = urllib.request.urlopen(url)
    asbytes = fp.read()

    peanutsHTML = asbytes.decode("utf8")
    fp.close()

    # Setup parser
    soup = BeautifulSoup(peanutsHTML, 'html.parser')

    # Filter to the picture tag and specific class
    picture = soup.find("picture", {"class": "item-comic-image"})

    # Extract the img tag
    try:
        img = picture.img

        # Get the image src - will be the comic strip as a gif
        comicStripURL = img['src']
        request.urlretrieve(comicStripURL, filename)

        # Determine the mime type. Either jpg or gif
        mime = magic.Magic(mime=True)
        mimetype = mime.from_file(filename)
    
        ext = '.'

        if mimetype == 'image/jpeg':
            ext += 'jpg'
        elif mimetype == 'image/gif':
            ext += 'gif'
        else:
            raise Exception("Failed to get mime type for: " + comicStripURL)

        # Rename the file
        os.rename(filename, filename + ext)
    except:
        print("Strip not found for date: " + str(start_date))

    # Increment the date
    start_date += timedelta(days=1)

# Finished
print("Finished. See the /images directory for the comic strips.")
