from pydantic import ValidationError

from app.models.job import Job


def test_job_with_skills() -> None:
    job = Job(
        title="Machine Learning Engineer",
        company="Example AI",
        description="Build and deploy machine learning systems.",
        required_skills=["Python", "Machine Learning", "SQL"],
        preferred_skills=["LangChain", "Docker"],
    )

    assert job.title == "Machine Learning Engineer"
    assert job.company == "Example AI"
    assert "Python" in job.required_skills
    assert "Docker" in job.preferred_skills


def test_job_requires_title_and_description() -> None:
    try:
        Job()  # type: ignore[call-arg]
    except ValidationError as exc:
        errors = exc.errors()

        assert len(errors) == 2
        assert errors[0]["loc"] == ("title",)
        assert errors[1]["loc"] == ("description",)
    else:
        raise AssertionError("Job should reject missing required fields")