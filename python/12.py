from collections import defaultdict
from os import path
from pprint import pprint as pp

with open('input/12.in', 'r') as in_file:
    lines = list(map(str.strip, in_file.readlines()))
    link = defaultdict(list)
    for line in lines:
        fr, to = line.split('-')
        link[fr].append(to)
        link[to].append(fr)

print(link)


def dfs(start, visited: set = {'start'}, doneTwice: bool = False, current_path=[]):
    if start == 'end':
        return [current_path + [start]]

    paths = []

    for node in link[start]:
        if node == 'start':
            continue

        if node in visited and doneTwice:
            continue

        newDoneTwice = doneTwice or node in visited

        new_visted = visited.union({start}) if start[0].islower() else visited
        paths += dfs(node,
                     visited=new_visted,
                     doneTwice=newDoneTwice,
                     current_path=current_path + [start])

    return paths


paths = dfs('start')
print(len(paths))