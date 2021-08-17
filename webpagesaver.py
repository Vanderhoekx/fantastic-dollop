#saves html from webpages using requests
#written by Kelly Schmidt

#import modules
import re
import requests
import pyinputplus as pyip
import pyperclip as pclip

#compile out the DNS from the url for filename
filename_compile = re.compile(r'''(http://|https://)
                                  (www.)?
                                  ([a-zA-Z0-9_-]*)
                                  [.][a-zA-Z]*[/]
                                  ([a-zA-Z0-9_-]*)?''', re.VERBOSE)

#if user has webpage copied to clipboard they can use that, otherwise manually enter the url
def ask_for_webpage():
    print("Would you like to pull the website url from the clipboard?(y/n): ")
    cut_and_paste = pyip.inputYesNo()
    if cut_and_paste == 'yes':
        user_request = pclip.paste()
        get_webpage(user_request)
    else:
        print('Please enter the URL you would like to get the HTML for: ')
        user_request = pyip.inputURL('Must start with http(s):// : ')
        get_webpage(user_request)

#request content from url
def get_webpage(user_request):
    req = requests.get(user_request)
    req.raise_for_status()
    filename = filename_compile.search(user_request)
    
#save webpage
    with open('web scraping progs/savedpages/{}.html'.format(filename.group(3) + filename.group(4)), 'wb') as webpage:
        for chunk in req.iter_content(chunk_size = 10_000):
           webpage.write(chunk)

ask_for_webpage()
