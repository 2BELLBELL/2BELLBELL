import sys,heapq
input=sys.stdin.readline
INF=int(1e9)

# 다익스트라 구현
def Dijkstra():
    dp[1]=0
    heap=[]
    heapq.heappush(heap , (0,1))

    while heap:
        value,node=heapq.heappop(heap)
        if dp[node]<value:
            continue

        for next_value,next_node in graph[node]:
            next_value+=value
            if next_value<dp[next_node]:
                dp[next_node]=next_value
                check[next_node]=node
                heapq.heappush(heap, (next_value , next_node))


N,M=map(int,input().split())

graph=[[] for _ in range(N+1)]
dp=[INF]*(N+1)
check=[0]*(N+1)

ALL=[]

for i in range(M):
    A,B,C=map(int,input().split())
    graph[A].append((C,B))
    graph[B].append((C,A))
    ALL.append((A , B))

Dijkstra()
print(N-1)
for i in range(2,N+1):
    print(i , check[i])