## Me: nice.meme@getbackinthe.kitchen
## All filenames should be named the tracker and the same as in the lists.
## All tracker names should be the same across files.
import os
files = [f for f in os.listdir('.') if os.path.isfile(f)]
trackers = {}
for filename in files:
    if 'txt' not in filename:
        continue        
    with open(filename) as f:
        trackers[filename.split('.')[0].lower()]=[x.lower() for x in f.read().splitlines()]

def backtrace(parent, start, end):
    _path = [end]
    while _path[-1] != start:
        _path.append(parent[_path[-1]])
    _path.reverse()
    return _path

def bfs(graph, start, end):
    parent = {}
    visited = {}
    queue = []
    queue.append(start)
    for node in trackers.keys():
        visited[node]=False
        for x in trackers[node]:
            visited[x]=False
    while queue:
        node = queue.pop(0)
        if node == end:
            return backtrace(parent, start, end)
        for adjacent in graph.get(node, []):
            if visited[adjacent] == False:
                visited[adjacent] = True
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
while 1:
    tyw = input('What tracker do  you want?').lower()
    for x in trackers.keys():
        lel = path(trackers, str(x), tyw)
        if lel != None : print(lel)
