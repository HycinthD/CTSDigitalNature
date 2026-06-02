def find_common_skills(skills1, skills2):
    if not isinstance(skills1, set) or not isinstance(skills2, set):
        print("Invalid input")
        return

    common_skills = skills1 & skills2
    print("Common Skills:", common_skills)

skills_set1 = {"Python", "Java", "SQL", "HTML"}
skills_set2 = {"Python", "C++", "SQL", "JavaScript"}

find_common_skills(skills_set1, skills_set2)