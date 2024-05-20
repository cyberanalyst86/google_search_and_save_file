import time
import requests
import re
import pandas as pd
import os

def write_file_to_directory(response, filename):

  isExist = os.path.exists(filename)

  if isExist == False:

    with open(filename, 'wb') as f:
      for chunk in response.iter_content(1024):
        f.write(chunk)

    print(f"Downloaded PDF: {filename}")

  else:

    error = "error"


  return

def download_file(df):

    # file_directory = "C:\\Users\\ongye\\Downloads\\threat_report\\threat_actor\\"

    for index, row in df.iterrows():

        print(row["link"])

        filename = row["link"].split("/")[-1]

        print(filename)

        try:

            response = requests.get(row["link"], stream=True)
            response.raise_for_status()  # Raise an exception for unsuccessful downloads

            write_file_to_directory(response, filename)

        except Exception as e:

            print(e)

    return

