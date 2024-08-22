from typing import List
from langchain_core.pydantic_v1 import Field
from typing_extensions import Annotated, TypedDict, Optional


class Position(TypedDict):
    job_title: Optional[Annotated[str, Field(description="Job Title")]] = None
    company: Optional[Annotated[str, Field(description="Company Name")]] = None
    position_duration: Optional[
        Annotated[str, Field(description="Position Duration")]
    ] = None
    experience_description: Optional[
        Annotated[List[str], Field(description="Experience Description")]
    ] = None
