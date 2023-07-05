from faker import Faker
from random import randint
from random import sample
from pathlib import Path

from file_operations import render_template
from src.letters_mapping import letters_mapping

RANGE_START = 3
RANGE_STOP = 18

fake = Faker("ru_RU")
skills = ["Стремительный прыжок", "Электрический выстрел", "Ледяной удар", "Стремительный удар", "Кислотный взгляд", 
          "Тайный побег", "Ледяной выстрел", "Огненный заряд"]

def generate_content() -> dict:
    charachter_skills = sample(skills, 3)
    ruinic_skills = []

    for skill in charachter_skills:
        for letter in skill:
            skill = skill.replace(letter, letters_mapping[letter])
        ruinic_skills.append(skill)

    content = {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "job": fake.job(),
        "town": fake.city(),
        "strength": randint(RANGE_START, RANGE_STOP),
        "agility": randint(RANGE_START, RANGE_STOP),
        "endurance": randint(RANGE_START, RANGE_STOP),
        "intelligence": randint(RANGE_START, RANGE_STOP),
        "luck": randint(RANGE_START, RANGE_STOP),
        "skill_1": ruinic_skills[0],
        "skill_2": ruinic_skills[1],
        "skill_3": ruinic_skills[2]
    }
    return content

def main():
    Path("out").mkdir(parents=True, exist_ok=True)
    for card_number in range(11):
        content = generate_content()
        render_template("src\charsheet.svg", f"out\\charsheet_{card_number}.svg", content)

if __name__ == '__main__'    :
    main()