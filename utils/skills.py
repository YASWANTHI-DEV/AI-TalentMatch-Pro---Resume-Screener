SKILLS = [
    "python",
    "java",
    "c",
    "c++",
    "sql",
    "mysql",
    "html",
    "css",
    "javascript",
    "react",
    "nodejs",
    "aws",
    "docker",
    "git",
    "power bi",
    "excel",
    "machine learning",
    "deep learning",
    "nlp",
    "data analysis",
    "streamlit"
]

def extract_skills(text):

    text = text.lower()

    found_skills = []

    for skill in SKILLS:

        if skill in text:

            found_skills.append(skill)

    return found_skills