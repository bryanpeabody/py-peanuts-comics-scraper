import datetime
from datetime import timedelta
import urllib.request
import requests
from bs4 import BeautifulSoup
import giphypop
from urllib import request

start_date = datetime.datetime(2019, 6, 1)
end_date = datetime.datetime(2019, 7, 1)
#end_date = datetime.datetime(2000, 1, 3)

# Loop over all the date range
while start_date <= end_date:
    filename = start_date.strftime('%Y-%m-%d') + ".gif"    
    url = "https://www.gocomics.com/peanuts/" + start_date.strftime('%Y') + "/" + start_date.strftime('%m') + "/" + start_date.strftime('%d')

    # Read in the HTML from the URL
    fp = urllib.request.urlopen(url)
    mybytes = fp.read()

    peanutsHTML = mybytes.decode("utf8")
    fp.close()

    # Setup parser
    soup = BeautifulSoup(peanutsHTML, 'html.parser')

    # Filter to the picture tag and specific class
    picture = soup.find("picture", {"class": "item-comic-image"})

    try:
        # Extract the img tag
        img = picture.img
        
        # Get the image src - will be the comic strip as a gif
        comicStripURL = img['src']

        g = giphypop.Giphy()
        request.urlretrieve(comicStripURL, filename)
    except:
        print(url)    

    # Increment the date
    start_date += timedelta(days=1)
