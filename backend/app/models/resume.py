from pydantic import BaseModel, Field


class Education(BaseModel):
    institution: str
    degree: str
    field_of_study: str | None = None
    start_year: int | None = None
    end_year: int | None = None


class Experience(BaseModel):
    company: str
    role: str
    description: str
    start_date: str | None = None
    end_date: str | None = None


class Project(BaseModel):
    name: str
    description: str
    technologies: list[str] = Field(default_factory=list)


class Resume(BaseModel):
    name: str
    email: str
    phone: str | None = None
    summary: str | None = None
    skills: list[str] = Field(default_factory=list)
    education: list[Education] = []
    experience: list[Experience] = []
    projects: list[Project] = []