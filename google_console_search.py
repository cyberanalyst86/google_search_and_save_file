from googleapiclient.discovery import build
import math
import pandas as pd
import re
from download_and_save_file import *

def google_console_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)

    num_search_results = kwargs['num']
    if num_search_results > 100:
        raise NotImplementedError('Google Custom Search API supports max of 100 results')
    elif num_search_results > 10:
        kwargs['num'] = 10  # this cannot be > 10 in API call
        calls_to_make = math.ceil(num_search_results / 10)
    else:
        calls_to_make = 1

    kwargs['start'] = start_item = 1
    items_to_return = []
    while calls_to_make > 0:
        res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
        items_to_return.extend(res['items'])
        calls_to_make -= 1
        start_item += 10
        kwargs['start'] = start_item
        leftover = num_search_results - start_item + 1
        if 0 < leftover < 10:
            kwargs['num'] = leftover

    return items_to_return

def get_google_result(results, output_filename):

    df = pd.DataFrame()

    title_list = []
    link_list = []
    displayLink_list = []
    snippet_list = []
    date_list = []

    for element in results:

        title_list.append(element["title"])
        link_list.append(element["link"])
        displayLink_list.append(element["displayLink"])
        snippet_list.append(element["snippet"])
        date = element["htmlSnippet"].split("<b>")[0]
        date_list.append(date)


        # -----------------------------------Create Dataframe-----------------------------------#

    df["date"] = date_list
    df["title"] = title_list
    df["link"] = link_list
    df["displayLink"] = displayLink_list
    df["snippet_list"] = snippet_list

    #df.to_excel("xxx.xlsx", index=False)

    #print("result output to excel completed")

    return df