import os
import re

README_PATH = "README.md"
START_MARK = "<!-- PROGRESS-START -->"
END_MARK = "<!-- PROGRESS-END -->"

def count_problems_in_dir(course_dir):
    if not os.path.isdir(course_dir):
        return 0
    return sum(os.path.isdir(os.path.join(course_dir, f)) for f in os.listdir(course_dir))

def get_courses():
    # Ignore some files (README, .git, etc.) and only look for directories
    blacklist = {"README.md", ".git", ".github", "update_readme_progress.py"}
    return [d for d in os.listdir() if os.path.isdir(d) and d not in blacklist]

def generate_progress_table():
    lines = ["| Course | Problems Solved |", "|---|---:|"]
    for course in sorted(get_courses()):
        count = count_problems_in_dir(course)
        lines.append(f"| {course} | {count} |")
    return "\n".join(lines)

def replace_progress_section(readme, new_section):
    pattern = f"{START_MARK}.*?{END_MARK}"
    replacement = f"{START_MARK}\n{new_section}\n{END_MARK}"
    return re.sub(pattern, replacement, readme, flags=re.DOTALL)

def main():
    if not os.path.exists(README_PATH):
        print("README.md not found!")
        exit(1)
    with open(README_PATH, encoding="utf-8") as f:
        readme = f.read()
    table = generate_progress_table()
    if START_MARK not in readme or END_MARK not in readme:
        # Insert markers at the end if not present
        readme += f"\n\n{START_MARK}\n{table}\n{END_MARK}\n"
    else:
        readme = replace_progress_section(readme, table)
    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(readme)

if __name__ == "__main__":
    main()
