def build_profile(first, last, **kwargs):
    """It builds a dictionary containing everything we know about an user"""
    kwargs["first"] = first
    kwargs["last"] = last
    return kwargs

profile = build_profile("ángel", "gómez rodríguez",
                        location="málaga",
                        field="economics",
                        hobbies="computing")
print(profile)