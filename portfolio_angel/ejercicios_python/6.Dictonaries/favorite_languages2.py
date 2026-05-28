favorite_languages = {
    "jen": ["python", "rust"],
    "sarah": ["c"],
    "edward": ["go", "rust"],
    "phil": ["python"],
}

for name, languages in favorite_languages.items():
    if len(languages) == 1:
        print(f"\n{name.title()}'s favourite language is:")
        for language in languages:
            print(f"\t{language.title()}")
    else:
        print(f"\n{name.title()}'s favourite languages are:")
        for language in languages:
            print(f"\t{language.title()}")