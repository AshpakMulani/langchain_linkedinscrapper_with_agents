
from langchain.serpapi import SerpAPIWrapper

# we are writing functions whihc will be used by Agent tools
# each function might be called by agent multiple times until it gets desired result
# so it is important to give docstring for each function so that agent can understand
# what that function is doing and call related functions


# writting custom wrapper which extends exsiting SerpAPI wrapper.
# below code is copied from existing SerpAPI wrapper but have made 
# few tweaks so that it can return linked in URL as result 
class CustomSerpAPIWrapper(SerpAPIWrapper):
    def __init__(self):
        super(CustomSerpAPIWrapper, self).__init__()

    @staticmethod
    def _process_response(res: dict) -> str:
        """Process response from SerpAPI."""
        if "error" in res.keys():
            raise ValueError(f"Got error from SerpAPI: {res['error']}")
        if "answer_box" in res.keys() and "answer" in res["answer_box"].keys():
            toret = res["answer_box"]["answer"]
        elif "answer_box" in res.keys() and "snippet" in res["answer_box"].keys():
            toret = res["answer_box"]["snippet"]
        elif (
            "answer_box" in res.keys()
            and "snippet_highlighted_words" in res["answer_box"].keys()
        ):
            toret = res["answer_box"]["snippet_highlighted_words"][0]
        elif (
            "sports_results" in res.keys()
            and "game_spotlight" in res["sports_results"].keys()
        ):
            toret = res["sports_results"]["game_spotlight"]
        elif (
            "knowledge_graph" in res.keys()
            and "description" in res["knowledge_graph"].keys()
        ):
            toret = res["knowledge_graph"]["description"]
        elif "snippet" in res["organic_results"][0].keys():
            # this line is tweaked to return link from results
            toret = res["organic_results"][0]["link"]

        else:
            toret = "No good search result found"
        return toret






# in this function we will be using SerpAPI (third party) whihc will be using google
# to query the results
def get_linked_in_profile_url(text: str) ->str:
    """searches for linkedin profile URL"""

    search = CustomSerpAPIWrapper()
    res = search.run(f"{text}")
    return res


