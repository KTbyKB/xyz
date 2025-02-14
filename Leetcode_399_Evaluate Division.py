# 399. Evaluate Division
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def dfs(src, dst, visited):
            if src not in adj_list or dst not in adj_list:
                return -1.0
            if dst in adj_list[src]:
                return adj_list[src][dst]
            for ele in adj_list[src]:
                if ele not in visited:
                    visited.add(ele)
                    temp = dfs(ele, dst, visited)
                    if temp == -1:
                        continue
                    else:
                        return adj_list[src][ele]*temp
            return -1

        adj_list = collections.defaultdict(dict)
        for i in range(len(equations)):
            v1, v2 = equations[i]
            w = values[i]
            adj_list[v1][v2] = w
            adj_list[v2][v1] = 1.0/w
        
        res = [] 
        for query in queries:
            res.append(dfs(query[0], query[1],set()))
        return res
