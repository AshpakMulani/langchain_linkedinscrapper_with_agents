import os
from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

import third_parties_module.linkedin as tpm
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent




if __name__ == "__main__":


    linkedin_profile_url = linkedin_lookup_agent(name="ashpak mulani barclays")

    # use linkedin module to read data for perticuler profile 
    data = tpm.linkedin_scraper(linkedin_profile_url)


    # creating operation details what we want chain to process 
    summary_template = """
                    given information {information} of a person please create following things:
                    1. a short summary
                    2. two interesting facts about the person 
    """
    input_vars = ['information']

    # creating prompt template object and define the variable details 
    prompt_template = PromptTemplate(input_variables=input_vars, template=summary_template)

    # creating a chat model using langchain. Here temperature defines
    # how much creative model can be, zero mean no creativity 
    llm =  ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")


    # creating a chain to process prompt template with chat model
    
    chain = LLMChain(llm=llm, prompt=prompt_template)

    # execute a chain by giniving info as info we want to process
    print(chain.run(information=data))



    """
    ==================   outout ===========================

    1. Short Summary:
    Ashpak Mulani is a Solution Designer at Barclays with 13 years of combined experience in team management, solution designing, and tech lead roles. He specializes in AWS backend development with Python and Node JS, as well as sales support for technical SOW scoping and developing customer experience for voice and chat with Amazon Connect and Amazon Lex chatbot. Ashpak also has expertise in process automation and business reporting.

    2. Two Interesting Facts:
    - Ashpak has worked at Dell in various roles, including Systems Integration Advisor and Software Engineer Analyst, where he gained experience in cloud (AWS) technologies and developed automation scripts using Boto3 library.
    - He is certified in Python programming by Microsoft and holds the AWS Certified Solutions Architect - Associate certification from Amazon Web Services. Additionally, Ashpak is a certified scrum master by Scrum Alliance.

    """     
