def compare_skills(resume_skills, job_skills):
    """
    Compare resume skills with job description skills.
    """

    resume_set = set(skill.lower() for skill in resume_skills)
    job_set = set(skill.lower() for skill in job_skills)

    matched = sorted(resume_set.intersection(job_set))
    missing = sorted(job_set.difference(resume_set))

    return matched, missing