#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

const int INF = 9876543210;
const int SIZE = 20001;
int v, e, k;                        // v : 정점의 개수, e : 간선의 개수, k : 시작 정점의 번호
int dis[SIZE];                      // 정점 k에서 idx 까지의 거리
vector<pair<int, int>> graph[SIZE]; // graph[a] = (b, w) : a에서 b까지의 가중치 w의 간선
priority_queue<pair<int, int>> pq;  // pair(d, node) : node 까지의 거리 d

void bfs(int start)
{
	// init
	dis[start] = 0;
	pq.push(make_pair(0, start));

	// bfs
	while (!pq.empty())
	{
		int now = pq.top().second;
		int distance = -pq.top().first;
		pq.pop();

		if (dis[now] < distance)
		{
			continue;
		}

		for (int i = 0; i < graph[now].size(); i++)
		{
			int nxt = graph[now][i].first;
			int weight = graph[now][i].second;

			if (dis[nxt] > distance + weight)
			{
				dis[nxt] = distance + weight;
				pq.push(make_pair(-1 * (distance + weight), nxt));
			}
		}
	}
}

int main()
{
	// 입력
	cin >> v >> e;
	cin >> k;
	for (int i = 0; i < e; i++)
	{
		int a, b, w;
		cin >> a >> b >> w;

		graph[a].push_back(make_pair(b, w));
	}

	for (int i = 1; i <= v; i++)
	{
		dis[i] = INF;
	}

	bfs(k);

	for (int i = 1; i <= v; i++)
	{
		dis[i] == INF ? cout << "INF" << '\n' : cout << dis[i] << '\n';
	}

	return 0;
}