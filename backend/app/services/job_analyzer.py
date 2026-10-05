from app.models.job import Job


def analyze_job(job: Job) -> Job:
    """Return the validated job information."""
    return job