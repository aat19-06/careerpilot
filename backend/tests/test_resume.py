from pydantic import ValidationError

from app.models.resume import Education, Experience, Project, Resume


def test_resume_with_nested_data() -> None:
    resume = Resume(
        name="Aat",
        email="aat@example.com",
        skills=["Python", "Machine Learning"],
        education=[
            Education(
                institution="Ponjesly College of Engineering",
                degree="BE",
                field_of_study="Artificial Intelligence and Machine Learning",
                start_year=2024,
            )
        ],
        experience=[
            Experience(
                company="Example AI",
                role="ML Intern",
                description="Worked on machine learning applications.",
            )
        ],
        projects=[
            Project(
                name="CareerPilot",
                description="AI-powered career intelligence platform.",
                technologies=["Python", "FastAPI", "LangGraph"],
            )
        ],
    )

    assert resume.name == "Aat"
    assert resume.skills == ["Python", "Machine Learning"]
    assert resume.education[0].degree == "BE"
    assert resume.experience[0].role == "ML Intern"
    assert "LangGraph" in resume.projects[0].technologies

def test_resume_requires_name_and_email() -> None:
    try:
        Resume()  # type: ignore[call-arg]
    except ValidationError as exc:
        errors = exc.errors()

        assert len(errors) == 2
        assert errors[0]["loc"] == ("name",)
        assert errors[1]["loc"] == ("email",)
    else:
        raise AssertionError("Resume should reject missing required fields")