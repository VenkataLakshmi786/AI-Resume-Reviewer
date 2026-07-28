from skills import JOB_SKILLS, SKILL_ALIASES


def calculate_skill_match(resume_text, job_role):

    resume = resume_text.lower()

    required_skills = JOB_SKILLS[job_role]

    found = []
    missing = []

    for skill in required_skills:

        aliases = SKILL_ALIASES.get(skill, [skill.lower()])

        skill_found = False

        for alias in aliases:

            if alias.lower() in resume:

                found.append(skill)
                skill_found = True
                break

        if not skill_found:
            missing.append(skill)

    score = round((len(found) / len(required_skills)) * 100)

    return {
        "required": required_skills,
        "found": found,
        "missing": missing,
        "score": score
    }
def compare_all_roles(resume_text):

    results = {}

    for role in JOB_SKILLS.keys():

        score = calculate_skill_match(
            resume_text,
            role
        )["score"]

        results[role] = score

    return dict(
        sorted(
            results.items(),
            key=lambda x: x[1],
            reverse=True
        )
    )