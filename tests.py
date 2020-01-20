import main

def test_read_file():
    if main.read_file(0) != ['ccabab\n', ['ba -> ab\n', 'ca -> ac\n', 'cb -> bc\n']]:
        print("Error read_file on test #1")
    if main.read_file(1) != ['aababab\n', ['ab -> \n', 'a -> b\n']]:
        print("Error read_file on test #2")
    if main.read_file(2) != ['aaa\n', ['b ->. a\n', 'a -> b\n']]:
        print("Error read_file on test #3")
    if main.read_file(3) != ['|||||||||\n', ['||| -> \n', '|| ->. \n', '| ->. \n', ' ->. |']]:
        print("Error read_file on test #4")
    if main.read_file(4) != ['ababa\n', ['*a ->. \n', '*b ->. \n', '* ->. \n', ' -> *']]:
        print("Error read_file on test #5")
    if main.read_file(5) != ['1010101\n', ['0b ->. 1\n', '1b -> b0\n', 'b ->. 1\n', 'a0 -> 0a\n', 'a1 -> 1a\n', '0a -> 0b\n', '1a -> 1b\n', ' -> a']]:
        print("Error read_file on test #6")


def test_parse():
    if main.parse(["1b ->. b1"]) != [['1b', 'b1', 1]]:
        print("Error test_parse")
    if main.parse([" ->. |"]) != [['', '|', 1]]:
        print("Error test_parse")
    if main.parse([" ->. 111\n", "123 -> 4"]) != [['', '111', 1], ['123', '4', 0]]:
        print("Error test_parse")
    if main.parse([" -> "]) != [['', '', 0]]:
        print("Error test_parse")
    if main.parse([" ->. \n"]) != [['', '', 1]]:
        print("Error test_parse")


def test_can_apply():
    if not main.can_apply("abacaba", ['aca', 'a', 0]):
        print("Error test_can_apply")
    if not main.can_apply("Borodinyar", ['or', '', 1]):
        print("Error test_can_apply")
    if not main.can_apply("abaa", ['aa', 'bb', 0]):
        print("Error test_can_apply")
    if not main.can_apply("tomorrow", ['ow', 'wo', 0]):
        print("Error test_can_apply")
    if not main.can_apply("fab", ['b', 'il', 0]):
        print("Error test_can_apply")
    if not main.can_apply("error", ['rr', 'r', 0]):
        print("Error test_can_apply")
    if not main.can_apply("wwww", ['', 'aba', 1]):
        print("Error test_can_apply")
    if main.can_apply("yyyy", ['b', 'aaa', 0]):
        print("Error test_can_apply")
    if main.can_apply("asdasd", ['hi', 'bye', 1]):
        print("Error test_can_apply")
    if main.can_apply("st", ['guf', 'xxx'], ):
        print("Error test_can_apply")
    if main.can_apply("cool", ['fward', 'aaa']):
        print("Error test_can_apply")


def test_apply_substitution():
    if main.apply_substitution("abacaba", ['aca', 'a', 0]) != "ababa":
        print("Error test_apply_substitution")
    if main.apply_substitution("Borodinyar", ['yar', '', 0]) != "Borodin":
        print("Error test_apply_substitution")
    if main.apply_substitution("abaa", ['aa', 'bb', 0]) != "abbb":
        print("Error test_apply_substitution")
    if main.apply_substitution("tomorrow", ['ow', 'wo', 0]) != "tomorrwo":
        print("Error test_apply_substitution")
    if main.apply_substitution("fab", ['b', 'il', 0]) != "fail":
        print("Error test_apply_substitution")
    if main.apply_substitution("error", ['rr', 'r', 0]) != "eror":
        print("Error test_apply_substitution")
    if main.apply_substitution("wwww", ['', 'aba', 0]) != "abawwww":
        print("Error test_apply_substitution")


def test_apply_once():
    if main.apply_once("ccabab", [['ba', 'ab', False], ['ca', 'ac', False], ['cb', 'bc', False]]) != ['ccaabb', 0]:
        print("Error test_apply_once")
    if main.apply_once("aababab", [['ab', '', False], ['a', 'b', False]]) != ['aabab', 0]:
        print("Error test_apply_once")
    if main.apply_once("aaa", [['b', 'a', True], ['a', 'b', False]]) != ['baa', 0]:
        print("Error test_apply_once")
    if main.apply_once("|||||||||", [['|||', '', False], ['||', '', True], ['|', '', True], ['', '|', True]]) != ['||||||', 0]:
        print("Error test_apply_once")
    if main.apply_once("ababa", [['*a', '', True], ['*b', '', True], ['*', '', True], ['', '*', False]]) != ['*ababa', 0]:
        print("Error test_apply_once")
    if main.apply_once("1010101", [['0b', '1', True], ['1b', 'b0', False], ['b', '1', True], ['a0', '0a', False], ['a1', '1a', False], ['0a', '0b', False], ['1a', '1b', False], ['', 'a', False]]) != ['a1010101', 0]:
        print("Error test_apply_once")
        

def test_apply_scheme():
    if main.apply_scheme("ccabab", [['ba', 'ab', False], ['ca', 'ac', False], ['cb', 'bc', False]]) != "aabbcc":
        print("Error test_apply_scheme")
    if main.apply_scheme("aababab", [['ab', '', False], ['a', 'b', False]]) != "b":
        print("Error test_apply_scheme")
    if main.apply_scheme("aaa", [['b', 'a', True], ['a', 'b', False]]) != "aaa":
        print("Error test_apply_scheme")
    if main.apply_scheme("|||||||||", [['|||', '', False], ['||', '', True], ['|', '', True], ['', '|', True]]) != "|":
        print("Error test_apply_scheme")
    if main.apply_scheme("ababa", [['*a', '', True], ['*b', '', True], ['*', '', True], ['', '*', False]]) != "baba":
        print("Error test_apply_scheme")
    if main.apply_scheme("1010101", [['0b', '1', True], ['1b', 'b0', False], ['b', '1', True], ['a0', '0a', False], ['a1', '1a', False], ['0a', '0b', False], ['1a', '1b', False], ['', 'a', False]]) != "1010110":
        print("Error test_apply_scheme")


test_read_file()
test_parse()
test_can_apply()
test_apply_substitution()
test_apply_once()
test_apply_scheme()


