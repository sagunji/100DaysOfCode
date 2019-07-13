NAMES = [
    "arnold schwarzenegger",
    "alec baldwin",
    "bob belderbos",
    "julian sequeira",
    "sandra bullock",
    "keanu reeves",
    "julbob pybites",
    "bob belderbos",
    "julian sequeira",
    "al pacino",
    "brad pitt",
    "matt damon",
    "brad pitt",
]


def dedup_and_title_case_names(names):
    """Should return a list of names, each name appears only once"""
    unique_names = list(dict.fromkeys(names))
    return [name.title() for name in unique_names]


def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)
    rev_names = []
    sorted_names = []
    for name in names:
        rev_name = name.split(" ")[::-1]
        rev_names.append(" ".join(rev_name))
    rev_names = sorted(rev_names, reverse=True)
    for rev_name in rev_names:
        sorted_name = rev_name.split(" ")[::-1]
        sorted_names.append(" ".join(sorted_name))

    return sorted_names


def shortest_first_name(names):
    """Returns the shortest first name (str).
       You can assume there is only one shortest name.
    """
    names = dedup_and_title_case_names(names)
    short_name = names[0].split(" ")[0]
    for name in names:
        first_name = name.split(" ")[0]
        if len(short_name) > len(first_name):
            short_name = first_name
    return short_name
