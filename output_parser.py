from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import List

## pydantic is data validation librabrary for python 

#This class is going to represent the output we are going to extract 
#from nlp model. This class inherits BaseModel class from Pydantic
class PersonalIntel(BaseModel):
    # define fields in data class 
    summary:str = Field(description="summary of a person")
    facts:List[str] = Field(description="interesting facts about person")


    # method to convert object in dict, so that during serialization this will be used
    def to_dict(self):
        return {"summary":self.summary , "facts":self.facts}


# this provides output parser object whihc can be plugged into LLM so that
# it can understand in what format output should be genrated 
personal_intel_parser:PydanticOutputParser = PydanticOutputParser(pydantic_object=PersonalIntel)