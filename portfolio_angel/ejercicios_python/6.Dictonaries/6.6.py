# Polling
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'phil': 'python',
}

poll_list = ["edward", "jen", "angel", "marina"]

for name in poll_list:
    if name in favorite_languages.keys():
        print(f"\n{name.title()}, thanku for responding but u have already taken the poll")
    else:
        print(f"\n{name.title()}, I see you have not yet taken the poll, would u like it?\nIt will only take a feew minutes of ur time")
