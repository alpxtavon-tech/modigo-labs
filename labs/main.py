def compare_hobbies(person1_hobbies, person2_hobbies):
    dicts = {}
    dicts["shared"] = person1_hobbies & person2_hobbies
    dicts["only_person1"] = person1_hobbies - person2_hobbies
    dicts["only_person2"] = person2_hobbies - person1_hobbies
    return dicts

print(compare_hobbies({"reading", "coding"}, {"coding", "gaming"}))