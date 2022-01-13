import pandas as pd
from pytrends.request import TrendReq
from datetime import date
import plotly.graph_objects as go
from plotly.subplots import make_subplots

pytrend = TrendReq()

def google_lookup(term):

    locations = {"Canada":"CA",
                "Alberta":"CA-AB",
                 "British Columbia":"CA-BC",
                 "Saskatchewan":"CA-SK",
                 "Manitoba":"CA-MB",
                 "Ontario":"CA-ON",
                 "Quebec":"CA-QC",
                 "Newfoundland":"CA-NL",
                 "Nova Scotia":"CA-NS",
                 "New Brunswick":"CA-NB",
                 "Prince Edward Island":"CA-PE",
                 "Yukon":"CA-YT",
                 "Northwest Territories":"CA-NT",
                 "Nunavut":"CA-NU"}
    combined_df = None

    for key, value in locations.items():
    #    print(key,value)
        try:
            pytrend.build_payload(kw_list= [term],timeframe=f'2017-01-01 {date.today()}', geo=value)
            dataframe = pytrend.interest_over_time()
            if combined_df is None:
                combined_df = dataframe.copy()
                combined_df.rename({term:key},axis = 1, inplace = True)
            else:
                combined_df[key] = dataframe[term]
        except:
            combined_df[key] = -1

    return combined_df