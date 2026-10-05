from app.models.job import Job
from app.services.job_analyzer import analyze_job


def test_analyze_job_returns_job() -> None:
    job = Job(
        title="ML Engineer",
        description="Build machine learning systems.",
        required_skills=["Python", "Machine Learning"],
    )

    result = analyze_job(job)

    assert result is job
    assert result.title == "ML Engineer"
    assert result.required_skills == ["Python", "Machine Learning"]
    