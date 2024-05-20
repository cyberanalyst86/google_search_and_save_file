from google_search import *
import time

def main():

    site = " site:cisa.gov | site:crowdstrike.com | site:recordedfuture.com | site:mandiant.com | site:IBM.com | site:microsoft.com "

    search_term_list = ["apt29" + site + "filetype:pdf"]

    for search_term in search_term_list:

        print("search : " + str(search_term))

        # Define output filename
        output_filename = str(search_term) + ".xlsx"

        #Go to Google Search Module
        #google_search(search_term, output_filename, regex_string)
        google_search(search_term, output_filename)

        time.sleep(5)

if __name__ == "__main__":
    main()








