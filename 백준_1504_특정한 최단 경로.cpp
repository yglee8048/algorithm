#include <iostream>
#include <vector>
#include <queue>

/*
	1. 착각
	dis[begin][nxt] = sum + weight;
	dis[nxt][begin] = sum + weight;
	라고 저장해두면 더 효율적이라고 생각했다.
	하지만, 이렇게 하면 dis[nxt][begin] 으로 인해 nxt를 출발점으로 할 때 nxt -> begin 이 이미 갱신되어 있으므로 그 이상 진행하지 않고 멈추면서 부정확한 결과를 얻게 만든다.

	2. 비효율적인 공간 활용
	실질적으로 필요한 dis 배열은 1, x, y 3개 뿐이므로, SIZE 가 아니라 3으로 생성하여 활용하면 공간을 절약할 수 있다.

	3. 플로이드-와샬 로 푸는 방법도 생각해보면 좋을 것 같다.
*/

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