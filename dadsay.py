#!/usr/bin/env python3
import sys, textwrap, random, string, itertools

dad_fingerguns = """
      \       _____
       \     /---- \\
        \   [&]/ [&]
            ( (c   /)
              ===; |
             _\__/ |____
            /  < >      |
           /   / \   /  /
          /  / | |  /  /
 ___/)___/  /_/)___/  /
'--;______'--;_______/
            |  | /   ]
            /  \/    \\
"""

dad_thaenkin = """
       \      _____
        \    /---- \\
         \  [&]/ [&]
            ( (c   /)
             \===; |
            ,---(\ \____
           / ¯¯\  )     |
          /  / < \ \ |  /
         /  /__|__\ \/  /
         [______ __\___/
            \  | |   /
            |  | /   ]
            /  \/    \\
"""

dad_wave = """
        \      _____
         \    /---- \\
          \  [&]/ [&]
             ( (c   /)
               ===' |
    ,\|/     __\__/ |____
     \ )/   /   < >      |
      \ \  /    / \   \  |
       \ \  /   | |   |  |
        \__/    | |   |  |
             |  | |   |  |
             |  | /   /  /
             /  \/   /  /
"""

dadjokes = [
    (dad_fingerguns, "How do you make holy water?\nYou boil the hell out of it.", ["water", "religion", "hell", "boil"]),
    (dad_thaenkin, "If a robot gets new shoes, does that mean they rebooted?", ["robot", "shoe", "shoes", "reboot"]),
    (dad_fingerguns, "Why are Pride events held in the Summer?\nBecause Pride comes before the fall.", ["pride", "lgbt", "gay", "bi", "lesbian", "trans", "summer", "fall", "autumn"]),
    (dad_thaenkin, "What has 4 letters, sometimes has 9 letters, but never has 5 letters.", ["letters", "character", "letter", "word", "sometimes", "always", "never"]),
    (dad_wave, "Don't forget to take a nap today - you don't want to be caught resisting a rest.", ["nap", "sleep", "rest", "arrest"]),
    (dad_thaenkin, "It's actually good if you aren't convinced to buy fruit from a street vendor. It means you can resist pear pressure.", ["peer", "pressure", "fruit", "pear", "vendor"]),
]

reverse_index = {}
for j,joke in enumerate(dadjokes):
    for word in joke[2]:
        if word in reverse_index:
            reverse_index[word] += j
        else:
            reverse_index[word] = [j]

def words_in_string(s):
    return s.lower().translate(s.maketrans(string.ascii_lowercase, string.ascii_lowercase, string.punctuation)).split()

def find_or_make_dad_joke(s):
    words = words_in_string(s)
    if "im" in words:
        ind = words.index("im")
        rest = " ".join(s.split()[ind+1:])
        return dad_wave, "Hi {}, I'm Dad.".format(rest), 0
    if "make" in words:
        ind = words.index("make")
        if (len(words) > ind + 2 and words[ind + 1] == "me"):
            rest = " ".join(s.split()[ind + 2:])
            return dad_fingerguns, "Poof, you're {}".format(rest), 0
    # If none of the formulas work, see if we have a relevant dadjoke
    for word in words:
        if word in reverse_index:
            return dadjokes[random.choice(reverse_index[word])]
    # Nothing to go on here, so just do some freestyle dadjoking
    return random.choice(dadjokes)

def puts(s):
    print(s, end="")

def pad(s, width):
    if (len(s) < width):
        s = s + " " * (width - len(s))
    return s

def string_to_lines(s):
    return list(itertools.chain.from_iterable(textwrap.wrap(l) for l in s.split("\n")))

def printbox(s):
    lines = string_to_lines(s)
    if (len(s) < 70): width = len(s)
    else: width = 70

    puts(" ")
    for i in range(width + 2): puts("_")
    puts("\n")
    if (len(lines) == 1):
        puts("( ")
        puts(lines[0])
        puts(" )\n")
    else:
        for i, line in enumerate(lines):
            if i == 0:
                puts("/ ")
                puts(pad(line, width))
                puts(" \\\n")
            elif i == len(lines) - 1:
                puts("\\ ")
                puts(pad(line, width))
                puts(" /\n")
            else:
                puts("| ")
                puts(pad(line, width))
                puts(" |\n")
    puts(" ")
    for i in range(width + 2): puts("¯")
    puts("\n")

def dadsay(s):
    art, joke, _ = find_or_make_dad_joke(s)
    printbox(joke)
    print(art[1:])

if __name__ == "__main__":
    if len(sys.argv) == 1:
        dadsay(sys.stdin.read())
    else:
        dadsay(" ".join(sys.argv[1:]).strip())



