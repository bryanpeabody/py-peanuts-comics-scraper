from datetime import datetime
from datetime import timedelta
import urllib.request
import requests
from bs4 import BeautifulSoup
from urllib import request
import magic
import os
from sys import argv

def downloadPeanuts():
    filename = "./images/peanuts"
    url = "https://www.gocomics.com/peanuts/" + datetime.today().strftime('%Y') + "/" + datetime.today().strftime('%m') + "/" + datetime.today().strftime('%d')
    parseHTMLAndSave(filename, url)

def downloadPeanutsBegins():
    filename = "./images/peanuts-begins"
    url = "https://www.gocomics.com/peanuts-begins/" + datetime.today().strftime('%Y') + "/" + datetime.today().strftime('%m') + "/" + datetime.today().strftime('%d')
    parseHTMLAndSave(filename, url)

def downloadCalvinAndHobes():
    filename = "./images/calvinandhobbes"
    url = "https://www.gocomics.com/calvinandhobbes/" + datetime.today().strftime('%Y') + "/" + datetime.today().strftime('%m') + "/" + datetime.today().strftime('%d')
    parseHTMLAndSave(filename, url)

def parseHTMLAndSave(filename, url):
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
        print("Strip not found!")

#
# Main
#
downloadPeanuts()
downloadPeanutsBegins()
downloadCalvinAndHobes()