
from typing import Any, Dict
from pydantic import BaseModel


class PromptItem(BaseModel):
    prompt: str


class ParameterDef(BaseModel):
    type: str


class ReturnsDef(BaseModel):
    type: str


class FunctionDef(BaseModel):
    name: str
    description: str
    parameters: Dict[str, ParameterDef]
    returns: ReturnsDef


class FunctionCallResult(BaseModel):
    prompt: str
    name: str
    parameters: Dict[str, Any]
