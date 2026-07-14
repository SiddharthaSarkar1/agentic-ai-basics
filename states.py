# Creating a graph
# First thing is to create a state


import os

# Approach - 1) Create state using - TypedDict 

from typing import TypedDict

class State(TypedDict):
    topic: str
    summery: str
    score: int

# Approach - 2)  pydantic approach 
#it is very good at data validation and type checking at 
#runtime 

from pydantic import BaseModel, field_validator

class State(BaseModel):
    topic: str
    summery: str = ""
    score: int

    @field_validator('score')
    def score_positive(cls, v):
        if v < 0:
            raise ValueError('score must be positive')
        return v


# Approach - 3)  python dataclaseess 
#standard python dataclass but it is used very rarelty

from dataclasses import dataclass, field

@dataclass
class State:
    topic: str = ""
    summary: str = ""
    message: list = field(default_factory=list)


# Approach - 4)  Using base langraph directly

from langgraph.graph import MessagesState

class State(MessagesState):
    # messages field is already included with add_messages reducer
    # just add your extra fields
    user_name: str
    language: str