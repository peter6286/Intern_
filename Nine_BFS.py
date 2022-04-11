import collections
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = []

class Solution:

    # 经典BFS
    def getdistance(self,node):
        queue = collections.deque([node])
        distance = {node:0}
        # distacne 有两个作用，一是判断是否已经访问过，二是记录点的距离
        while queue:
        # 不断访问队列
        # while 循环 + 每次pop队列中的一个点出来
            node = queue.popleft()
            for neighbor in node.get_neighbors():
                # 拓展相邻的节点
                if neighbor in distance:
                    continue
                distance[neighbor] = distance[node]+1
                queue.append(neighbor)


    # 133. Clone Graph
    # BFS
    def cloneGraph(self, node):
        if not node:
            return None

        nodes = self.find_node_bfs(node)
        mapping = self.copy_nodes(nodes)
        self.copy_edges(nodes, mapping)

        return mapping[node] if node else None

    def find_node_bfs(self, node):
        queue = collections.deque([node])
        visited = set([node])       # set可以去重
        while queue:
            curr_node = queue.popleft()
            for neighbor in curr_node.neighbors:
                if neighbor in visited:
                    # 如果之前已经找到了这个点，无需再次BFS
                    continue
                queue.append(neighbor)
                visited.add(neighbor)
        return list(visited)

    # 复制所有的点
    def copy_nodes(self, nodes):
        # （旧点->新点）的映射
        mapping = {}
        for node in nodes:
            mapping[node] = Node(node.val)
        return mapping

    # 复制所有的边
    def copy_edges(self, nodes, mapping):
        for node in nodes:
            new_node = mapping[node]
            # 因为前面已经有了映射，这里只要把新旧邻居连接上
            for neighbor in node.neighbors:
                new_neighbor = mapping[neighbor]
                new_node.neighbors.append(new_neighbor)

    # DFS
    def clonegraphdfs(self,node):
        oldtonew = {}
        def dfs(node):
            if node in oldtonew:
                return oldtonew[node]

            copy = Node(node.val)
            oldtonew[node] = copy      #新旧邻居之前的映射
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))     #给新的node添加上邻居
            return copy
        return dfs(node) if node else None




    #     120 · 单词接龙
    def ladder_length(self, start,end, dict):
        dict.add(end)
        queue = collections.deque([start])
        visited = set([start])
        distance = 0
        while queue:
            distance += 1
            size = len(queue)
            # 当前层有多少个元素
            for i in range(size):
                word = queue.popleft()
                # 将当前层的元素依次pop出去
                if word == end:
                    return distance
                    # 如果当前层的词为词尾，直接返回当前的长度
                for next_word in self.get_next_words(word, dict):
                    # 如果没有继续去找下一个
                    if next_word in visited:
                        continue
                    queue.append(next_word)
                    visited.add(next_word)
        return 0

    def get_next_words(self, word, wordList):
        # 找到可以和word接龙的所有的单词
        next_words = []
        for i in range(len(word)):
            left,right = word[:i],word[i+1:]
            for char in 'abcdefghijklmnopqrstuvwxyz':
                if word[i]==char:
                    continue
                # 在s中，把位置index的字母替换成c，返回替换后的字符串
                new_word = left + char + right
                # 如果字母替换后的单词存在于dict，加入next_words
                if new_word in wordList:
                    next_words.append(new_word)
        return next_words


    # 127. Word Ladder
    def ladderLength2(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            return 0

        nei = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                nei[pattern].append(word)
        # 设置一个每个单词空一个词的dictionary  {h*t:hit,h*t:hot}

        visit = set([beginWord])
        q = deque([beginWord])
        res = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1:]
                    for neiWord in nei[pattern]:    #在dictionary中循环
                        if neiWord not in visit:    #如果在dictionary中找到了加入visit并放入queue中
                            visit.add(neiWord)
                            q.append(neiWord)
            res += 1
        return 0


    # 200. Number of Islands
    def numIslands(self, grid):
        if not grid:
            return 0
        def bfs(r,c):
            q = []
            visit.add((r,c))
            q.append((r,c))
            while q:
                row,col = q.pop(0)
                direction = [[1,0],[-1,0],[0,1],[0,-1]] #在四个方向找
                for dr,dc in direction:
                    r,c = row+dr,col+dc     # 加上方向的值
                    if ( r in range (rows) and   #在bfs中找连续是1的点然后加入queue和visit当中
                        c in range(cols) and    # 确定当前的点在grid中并且有1
                        grid[r][c] == "1" and
                        (r,c ) not in visit):
                        q.append((r,c))
                        visit.add((r,c))

        rows, cols = len(grid), len(grid[0])
        visit = set()
        island = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and (r,c) not in visit:
                    # 找到有"1"的点后做bfs，如果当前的点没有被visited过
                    bfs(r,c)
                    island+=1

        return island

    # 611 · 骑士的最短路线
    def shortest_path(self, grid, source, destination):
        OFFSETS = [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, 2)]
        queue = collections.deque([(source.x,source.y)])
        point_dict = {(source.x,source.y):0}

        while queue:
            x,y= queue.popleft()
            if (x,y) == (destination.x,destination.y):
                return point_dict[(x,y)]
            for dx,dy in OFFSETS:
                next_x,next_y = x+dx,y+dy
                if not self.is_valid(next_x,next_y,grid):
                    continue
                if (next_x,next_y) in point_dict:
                    continue
                queue.append((next_x,next_y))
                point_dict[(next_x,next_y)]=point_dict[(x,y)]+1
        return -1

    def is_valid(self,x,y,grid):
        n,m=len(grid),len(grid[0])
        if x < 0 or x>=n or y<0 or y>=m:
            return False
        return not grid[x][y]


    # 616 · 课程表 II
    def findOrder(self, numCourses, prerequisites):
        graph = [[] for i in range(numCourses)]
        # 构建图 做一个先修课和后修课的映射
        in_degree = [0] * numCourses
        # 1。统计每个点的入度，并构建图
        for node_in,node_out in prerequisites:
            graph[node_out].append(node_in)
            in_degree[node_in]+=1

        # 2。将每个入度为0的点放入队列中作为起始点
        queue = collections.deque()
        num_choose = 0
        topo_order = []
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)

        # 不断地从队列中取出一个点，去掉这个点的所有边
        # 其他点的入度也相应的减1
        while queue:
            new_pos = queue.popleft()
            topo_order.append(new_pos)
            num_choose +=1
            for next_pos in graph[new_pos]:
                # 4。一旦发现新的入度为0，丢回队列中
                # 表示先修课已经完成
                in_degree[next_pos] -=1
                if in_degree[next_pos] == 0:
                    queue.append(next_pos)

        return topo_order if num_choose == numCourses else []



    # 127 · 拓扑排序
    def topSort(self, graph):
        node_indegree = self.get_indegree(graph)
        start_nodes = [n for n in graph if node_indegree[n] == 0]
        queue = collections.deque(start_nodes)

        order = []
        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor in node.neighbors:
                node_indegree[neighbor] -= 1
                if node_indegree[neighbor] == 0:
                    queue.append(neighbor)

        return order

    def get_indegree(self, graph):
        node_to_indegree = {x: 0 for x in graph}
        for node in graph:
            for neighbor in node.neighbors:
                node_to_indegree[neighbor] += 1
        return node_to_indegree



















object = Solution()
#print(object.ladderLength("hit","cog",["hot","dot","dog","lot","log","cog"]))
print(object.findOrder(2,[[1,0]]))