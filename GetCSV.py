#!/usr/bin/env python3
# Ref: https://realpython.com/pandas-python-explore-dataset/
#  Download the data
# = download script  (=> 1) source 2) repeat + refresh 3) - share csv)
# = (Alt + raw link) (=> static)
import requests

# str_download_url = "https://raw.githubusercontent.com/justmarkham/trump-lies/master/trump_lies.csv"
# requests.get(str_download_url) method returns a response object with all response data: content, encoding, status
response = requests.get("https://raw.githubusercontent.com/justmarkham/trump-lies/master/trump_lies.csv")
# response.status_code = 200  <=> success status
response.raise_for_status()
# relative/ absolute target_csv_path
target_csv_path = "Trump Lies.csv"
# Ref : https://docs.python.org/3/tutorial/inputoutput.html -> 7.2 Reading and writing files
# open(filename, mode)  returns a file object.
# filename: str , mode: str = way to use the file
# mode :  'r' (read) (default) , 'w'(write / overwrite existing file) , 'a' (appending), 'r+' read & write
# mode: text mode / binary mode (in form of bytes objects for non-text file)

# open(target_csv_path, "wb") => open file specified by target_csv_path to write in binary mode (for non-text file)
# with keyword when dealing with file objects
# => close the file after its suites finishes.   print(f.closed) = True

# f.write(response.content) => write all content of the response object to the file f
with open(target_csv_path, "wb") as f:
    f.write(response.content)
