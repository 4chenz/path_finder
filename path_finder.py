## Me: nice.meme@getbackinthe.kitchen
## Might kill it's self sometimes, not sure why. Probably because copy pasta.
## All filenames should be named the tracker and the same as in the lists.
## All tracker names should be the same across files.
import os
files = [f for f in os.listdir('.') if os.path.isfile(f)]
trackers = {}
for filename in files:
    if 'txt' not in filename:
        continue
    with open(filename) as f:
        trackers[filename.split('.')[0]]=[x.strip("\n").strip("\\n") for x in f.readlines()]

def backtrace(parent, start, end):
    path = [end]
    while path[-1] != start:
        path.append(parent[path[-1]])
    path.reverse()
    return path

def bfs(graph, start, end):
    parent = {}
    queue = []
    queue.append(start)
    while queue:
        node = queue.pop(0)
        if node == end:
            return backtrace(parent, start, end)
        for adjacent in graph.get(node, []):
            parent[adjacent] = node
            queue.append(adjacent)

def path(graph, start, end):
    x = bfs(graph, start, end)
    if x != None:
        for d,n in enumerate(x):
            if len(x) > d+1:
                print(n,end=" -> ")
                continue
            print(n)

for x in trackers.keys():
    lel = path(trackers, str(x), 'AnimeBytes')
    if lel != None : print(lel)#change this to search for a particular path

