from pydantic import BaseModel, Field


class Job(BaseModel):
    title: str
    company: str | None = None
    description: str
    required_skills: list[str] = Field(default_factory=list)
    preferred_skills: list[str] = Field(default_factory=list)