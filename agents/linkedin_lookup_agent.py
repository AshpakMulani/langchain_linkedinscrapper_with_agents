from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI

from langchain.agents import initialize_agent, Tool, AgentType

from tools import tools as agent_tools

"""
Every agent need different things to understand and break down given operation in plain language
into smaller pieces and perform them using given tools

1. Tools to perform operaitons like hit and get data from linkedin api, get data from google drive etc...
2. LLM for language capabilities
3. Agent type, we will use 'zero-shot React' whihc is most common
"""

def lookup(name : str) -> str:
    # create llm model instance
    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")

    # define prompt template
    template = """ given a full name of a person {name_of_person} I want you to get me link to their LinkedIn profile page.
                Your final answer should only contain URL.
                """
    

    # defining tools whihc will be used by agent to perform operaitons 
    # name : name of the tool (we can gie anything)
    # func : our function whihc agent will be calling to perform the operaiton. This function is 
    #        defined in tools pachage we have written seperately 
    # description : SUPER important, because using description agent will decide if this tool is suitable
    #                for given operation    
    tools_for_agent = [Tool(
                            name="linkedin profile page crawler tool", 
                            func=agent_tools.get_linked_in_profile_url,
                            description="useful for when you need to get linkedin profile URL using user name"
                        )
                    ]
    
    # initialize agent with tools, llm, type and verbose flag so that we can see what all things agent is doing
    agent = initialize_agent(tools=tools_for_agent, 
                             llm=llm,
                             agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION,
                             verbose = True
                             )
    
    prompt_template = PromptTemplate(template=template, input_variables=['name_of_person'])

    # run agent to find linkedin profile url using name of user
    linkedin_profile_url = agent.run(prompt_template.format_prompt(name_of_person=name))

    
    return linkedin_profile_url
