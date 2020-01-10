#include <iostream>
#include <vector>
#include <queue>

using namespace std;

const int INF = 98765432;
const int SIZE = 801;
int n, e, x, y;
int dis[SIZE][SIZE];
vector<pair<int, int>> graph[SIZE];

void bfs(int begin) {

	priority_queue<pair<int, int>> pq;

	fill_n(dis[begin], n + 1, INF);
	dis[begin][begin] = 0;
	pq.push(make_pair(0, begin));

	while (!pq.empty()) {
		int now = pq.top().second;
		int sum = -pq.top().first;
		pq.pop();

		if (dis[begin][now] < sum) {
			continue;
		}

		for (int j = 0; j < graph[now].size(); j++) {
			int nxt = graph[now][j].first;
			int weight = graph[now][j].second;

			if (dis[begin][nxt] > sum + weight) {
				dis[begin][nxt] = sum + weight;

				pq.push(make_pair(-dis[begin][nxt], nxt));
			}
		}
	}
}

int main() {

	cin >> n >> e;
	for (int i = 0; i < e; i++) {
		int a, b, c;
		cin >> a >> b >> c;

		graph[a].push_back(make_pair(b, c));
		graph[b].push_back(make_pair(a, c));
	}
	cin >> x >> y;

	bfs(1);
	bfs(x);
	bfs(y);

	int root_a = dis[1][x] + dis[x][y] + dis[y][n];
	int root_b = dis[1][y] + dis[y][x] + dis[x][n];

	if (root_a >= INF && root_b >= INF) {
		cout << -1 << '\n';
	}
	else {
		root_a < root_b ? cout << root_a << '\n' : cout << root_b << '\n';
	}
	
	return 0;
}