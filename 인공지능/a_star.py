from queue import PriorityQueue

map = {}
h = {}
edges = int(input())

v = {}
for i in range(0, 26):
    map [ chr(ord('A')+i)] = {}
    v[chr(ord('A')+i)] = False
    h[chr(ord('A') +i)] = 0
for i in range(0, edges):
    a,b,d = str(input()).split(' ')
    map[a][b] = int(d)
    map[b][a] = int(d)

cnt = int(input())
for i in range(0,cnt):
    vtx, d = str(input()).split(' ')
    h[vtx] = int(d)

q = PriorityQueue()
q.put((0,'A', 0))
while not q.empty():
    dt, vtx, d = q.get()
    print(dt,vtx,d)
    if vtx == 'B':
        print(d)
        break
    if v[vtx]:
        continue
    v[vtx] = True
    for k in map[vtx].keys():
        if not v[k]:
            q.put((d + map[vtx][k] + h[k], k, d+map[vtx][k]))

    