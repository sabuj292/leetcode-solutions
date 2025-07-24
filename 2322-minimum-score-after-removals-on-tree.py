from collections import defaultdict

class Solution(object):
    def minimumScore(self, nums, edges):
        n = len(nums)
        tree = defaultdict(list)
        
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)
        
        parent = [-1] * n
        xor = [0] * n
        in_time = [0] * n
        out_time = [0] * n
        time = 0

        # Step 1: DFS to compute subtree XOR and timestamps
        time = [0]
        def dfs(node, par):
            # nonlocal time
            parent[node] = par
            in_time[node] = time[0]
            time[0] += 1
            xor[node] = nums[node]
            for nei in tree[node]:
                if nei != par:
                    dfs(nei, node)
                    xor[node] ^= xor[nei]
            out_time[node] = time[0]
            time[0] += 1

        dfs(0, -1)
        total = xor[0]

        # Step 2: Try every pair of edges
        result = float('inf')
        edge_nodes = []

        # Get all edges (child node only)
        for i in range(1, n):
            edge_nodes.append(i)

        def is_ancestor(u, v):
            return in_time[u] <= in_time[v] and out_time[v] <= out_time[u]

        for i in range(len(edge_nodes)):
            for j in range(i + 1, len(edge_nodes)):
                a, b = edge_nodes[i], edge_nodes[j]

                if is_ancestor(a, b):
                    x = xor[b]
                    y = xor[a] ^ xor[b]
                    z = total ^ xor[a]
                elif is_ancestor(b, a):
                    x = xor[a]
                    y = xor[b] ^ xor[a]
                    z = total ^ xor[b]
                else:
                    x = xor[a]
                    y = xor[b]
                    z = total ^ xor[a] ^ xor[b]

                vals = [x, y, z]
                result = min(result, max(vals) - min(vals))

        return result


sol = Solution()
print(sol.minimumScore([1,5,5,4,11], [[0,1],[1,2],[1,3],[3,4]]))  # Output: 9
print(sol.minimumScore([5,5,2,4,4,2], [[0,1],[1,2],[5,2],[4,3],[1,3]]))  # Output: 0
