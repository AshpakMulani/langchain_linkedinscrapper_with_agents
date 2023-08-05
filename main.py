import os
from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

import third_parties_module.linkedin as tpm
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent

# output parser file whihc we created to define output structure of results
import output_parser as op


# function is going to return tuple of PersonalIntelobject from outputparser and 
# str with profile pic url to display on webpage
def process_info(user_name:str) -> tuple[op.PersonalIntel, str]:
    response = ""
    linkedin_profile_url = linkedin_lookup_agent(name=user_name)

    # use linkedin module to read data for perticuler profile 
    data = tpm.linkedin_scraper(linkedin_profile_url)


    # creating operation details what we want chain to process 
    summary_template = """
                    given information {information} of a person please create following things:
                    1. a short summary
                    2. two interesting facts about the person 
                    /n{format_instructions}
    """
    # adding {format_instructions} in template to hookup our output parser

    input_vars = ['information']

    # creating prompt template object and define the variable details 
    prompt_template = PromptTemplate(
            input_variables=input_vars,
            template=summary_template,
            # add formating variable to feed in how we want final output
            partial_variables={"format_instructions": op.personal_intel_parser.get_format_instructions()}
    )

    # creating a chat model using langchain. Here temperature defines
    # how much creative model can be, zero mean no creativity 
    llm =  ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")


    # creating a chain to process prompt template with chat model
    
    chain = LLMChain(llm=llm, prompt=prompt_template)

    response = chain.run(information=data)

    print(data)

    # parse the response with output parser
    return op.personal_intel_parser.parse(response), data.get("profile_pic_url")

if __name__ == "__main__":

    results = process_info(user_name='ashpak mulani barclays')