import pandas as pd
import requests
import os
import matplotlib.pyplot as plt
import streamlit as st
# To set your environment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
# To set your enviornment variables in your terminal run the following line:
os.environ.setdefault('BEARER_TOKEN', 'AAAAAAAAAAAAAAAAAAAAAJT%2FbgEAAAAAb32JuiTo2HTpKpMSFFHjdD3Pg6E%3DDIXXfrUvJn5drQGGz8GaICYEB0PjGmdNPRZScjzvMR9fuPOmGQ')

bearer_token = os.environ.get("BEARER_TOKEN")

search_url = "https://api.twitter.com/2/tweets/counts/recent"



def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2RecentTweetCountsPython"
    return r


def connect_to_endpoint(url, params):
    response = requests.request("GET", search_url, auth=bearer_oauth, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


def main():
    search_term = st.text_input("search_term",value="kubernetes")
    #search_term = search_term
    # Optional params: start_time,end_time,since_id,until_id,next_token,granularity
    query_params = {'query': search_term, 'granularity': 'day'}

    json_response = connect_to_endpoint(search_url, query_params)
    #print(json.dumps(json_response, indent=4, sort_keys=True))
    results = pd.DataFrame(json_response['data'])
    
    st.bar_chart(results['tweet_count'])




if __name__ == "__main__":
    main()

