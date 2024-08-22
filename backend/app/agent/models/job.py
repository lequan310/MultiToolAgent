from langchain_core.pydantic_v1 import Field
from typing_extensions import Annotated, TypedDict, Optional


class Job(TypedDict):
    core_responsibilities: Optional[
        Annotated[str, Field(description="Core Responsibilities")]
    ] = None
    major_skill_requirements: Optional[
        Annotated[str, Field(description="Major Skill Requirements")]
    ] = None
    soft_skill_requirements: Optional[
        Annotated[str, Field(description="Soft Skill Requirements")]
    ] = None
    educational_requirements: Optional[
        Annotated[str, Field(description="Educational Requirements")]
    ] = None
    experience_level_requirements: Optional[
        Annotated[str, Field(description="Experience Level Requirements")]
    ] = None
    compensation_and_benefits: Optional[
        Annotated[str, Field(description="Compensation and Benefits")]
    ] = None
