import sys

def error(ac, av):
    av = sys.argv
    ac = len(sys.argv)
    for i in range(1, ac):
        if av[i].isdigit() != True or int(av[i]) < 0:
            exit(84)
    if ac != 2 and ac != 3:
        exit(84)
    if ac == 2 and int(av[1]) <= 0:
        exit(84)

    if ac == 3 and int(av[1]) < int(av[2]):
            exit(84)