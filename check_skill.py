required_skills = ["python", "SQL", "git", "Html"]


def check_skill(skill_name):
	"""Return whether the skill is in the required skills list."""
	if skill_name in required_skills:
		return "Skill available"
	return "Skill not available"


if __name__ == "__main__":
	skill_name = input("Enter a skill name: ").strip()
	print(check_skill(skill_name))