from typing import List
from langchain_core.pydantic_v1 import Field
from typing_extensions import Annotated, TypedDict, Optional
from app.agent.models.position import Position
from app.agent.models.project import Project


class Resume(TypedDict):
    skills: Optional[Annotated[str, Field(description="Skills")]] = None
    educational_level: Optional[
        Annotated[str, Field(description="Educational Level")]
    ] = None
    positions: Optional[
        Annotated[List[Position], Field(description="List of Positions")]
    ] = None
    projects: Optional[
        Annotated[List[Project], Field(description="List of Projects")]
    ] = None
    certificates: Optional[
        Annotated[List[str], Field(description="List of Certificates")]
    ] = None
