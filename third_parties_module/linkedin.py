import os
import requests
import json


def linkedin_scraper(profile_url: str):
    """
    scraping info directly from linked-in has its own complexity, so we can use third party
    proxy services whihc makes it easier to scrape the info from linkedin.
    """

    # one of the famouse third party proxy for linked in scraping is https://nubela.co/proxycurl/linkedin
    # it give 10 points on sighup whihc can be used to put 10 api calls

    # following code is provided by proxycurl documentaiton to make linked in request

    
    api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
    api_key = "arpi-phkl2hzzWrMN7JGvg"
    header_dic = {'Authorization': 'Bearer ' + api_key}
    params = {'url': profile_url  }

    response = requests.get(api_endpoint, params=params, headers=header_dic)

    #print(response._content)


    return response._content
