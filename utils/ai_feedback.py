def generate_feedback(resume_text, job_description):

    resume_text = resume_text.lower()
    job_description = job_description.lower()

    feedback = []

    # Strengths
    if "python" in resume_text:
        feedback.append("✔ Strong in Python development")

    if "machine learning" in resume_text:
        feedback.append("✔ Has Machine Learning experience")

    if "project" in resume_text:
        feedback.append("✔ Hands-on project experience")

    # Weakness
    if "communication" not in resume_text:
        feedback.append("⚠ Lacks mention of communication skills")

    if "team" not in resume_text:
        feedback.append("⚠ Team collaboration not highlighted")

    # Recommendation
    if "python" in resume_text and "project" in resume_text:
        feedback.append("✅ Recommended for interview")
    else:
        feedback.append("❌ Needs improvement before selection")

    return "\n".join(feedback)