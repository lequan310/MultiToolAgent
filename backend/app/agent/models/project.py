from typing import List
from langchain_core.pydantic_v1 import Field
from typing_extensions import Annotated, TypedDict, Optional


class Project(TypedDict):
    project_title: Optional[Annotated[str, Field(description="Project Title")]] = None
    project_duration: Optional[
        Annotated[str, Field(description="Project Duration")]
    ] = None
    project_description: Optional[
        Annotated[List[str], Field(description="Project Description")]
    ] = None
