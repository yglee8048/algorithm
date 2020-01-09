#include <iostream>
#include <vector>

using namespace std;

const int INF = 9876543210;
const int SIZE = 20001;
int v, e, k;                        // v : 정점의 개수, e : 간선의 개수, k : 시작 정점의 번호
int dis[SIZE];                      // 정점 k에서 idx 까지의 거리
vector<pair<int, int>> graph[SIZE]; // graph[a] = (b, w), a에서 b까지의 가중치 w의 간선

int dfs(int now, int sum)
{
  for (int i = 0; i < graph[now].size(); i++)
  {
    int nxt = graph[now][i].first;
    int weight = graph[now][i].second;

    if (dis[nxt] > sum + weight)
    {
      dfs(nxt, sum + weight);
    }
  }
}

int main()
{
  // 입력
  cin >> v >> e;
  cin >> k;
  for (int i = 0; i < v; i++)
  {
    int a, b, w;
    cin >> a >> b >> w;

    graph[a].push_back(make_pair(b, w));
    graph[b].push_back(make_pair(a, w));
  }

  for (int i = 0; i < v; i++)
  {
    dis[i] = INF;
  }
  dis[k] = 0;

  return 0;
}