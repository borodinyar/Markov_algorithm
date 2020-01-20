def read_file(number):
    input_file = open("tests/test" + str(number) + ".in", "r")
    return [input_file.readline(), input_file.readlines()]


def parse(substitutions):
    parse_substitutions = []
    for substitution in substitutions:
        print(substitution.split(' '))
        find_str, arrow, replace_str = substitution.split(' ')
        replace_str = replace_str.strip()
        terminal = ("." in arrow)
        parse_substitutions.append([find_str, replace_str, terminal])
    return parse_substitutions


def can_apply(word, substitution):
    return substitution[0] in word


def apply_substitution(word, substitution):
    if substitution[0] == '':
        return substitution[1] + word
    return word.replace(substitution[0], substitution[1], 1)


def apply_once(word, substitutions):
    for substitution in substitutions:
        if can_apply(word, substitution):
            return [apply_substitution(word, substitution), substitution[2]]
    return [word, True]


def apply_scheme(word, substitutions):
    while True:
        word, end = apply_once(word, substitutions)
        if end:
            return word


for number in range(6):
    print("=" * 12 + " " + str(number) + " " + "=" * 12)
    word, substitutions = read_file(number)
    word = word.strip()
    scheme = parse(substitutions)
    print(apply_scheme(word, scheme))
