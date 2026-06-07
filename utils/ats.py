import re

def ats_score(text, resume_skills, jd_skills):

    score = 0
    text = text.lower()

    # -------------------------------
    # BASIC STRUCTURE (30 MARKS)
    # -------------------------------

    if re.search(r"\S+@\S+", text):
        score += 5

    if re.search(r"\d{10}", text):
        score += 5

    if "education" in text:
        score += 5

    if "skills" in text:
        score += 5

    if "experience" in text:
        score += 5

    if "project" in text:
        score += 5

    # -------------------------------
    # SKILL MATCH (50 MARKS)
    # -------------------------------

    if len(jd_skills) > 0:

        matched = len(
            set(resume_skills).intersection(set(jd_skills))
        )

        skill_score = (matched / len(jd_skills)) * 50

        score += skill_score

        # -------------------------------
        # PENALTY FOR MISSING SKILLS
        # -------------------------------

        missing = len(jd_skills) - matched

        penalty = (missing / len(jd_skills)) * 20

        score -= penalty

    # -------------------------------
    # NORMALIZE SCORE
    # -------------------------------

    score = max(0, min(score, 100))

    return round(score, 2)