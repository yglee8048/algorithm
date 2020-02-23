#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

const int SIZE = 5001;
vector<vector<int>> cycles; // cycle 의 목록을 저장하는 목록
vector<int> graph[SIZE];
bool checked[SIZE];
int visit_node_order[SIZE]; // visit_node_order[n] = m : n번 노드에 방문한 순서 = m
int visit_order_node[SIZE]; // visit_order_node[m] = n : m번째로 방문한 노드 = n

// dfs 를 통해 cycle 및 cycle에 속하는 node의 목록을 구한다.
void dfs(int current, int past, int order)
{
  // 한 번이라도 방문한 노드를 체크
  checked[current] = true;
  for (int i = 0; i < graph[current].size(); i++)
  {
    int nxt = graph[current][i];
    // 바로 이전 노드이거나, 이미 확인이 끝난 노드라면 재방문하지 않는다.
    if (nxt == past)
    {
      continue;
    }

    // 방문 순서가 현재보다 작다면, 이미 방문한 노드이며, 사이클이다.
    if (visit_node_order[nxt] < order)
    {
      // 방문 경로에 있던 node의 목록을 기록한다.
      vector<int> cycle;
      for (int i = visit_node_order[nxt]; i <= order; i++)
      {
        cycle.push_back(visit_order_node[i]);
      }
      // cycle의 목록을 정렬해서 기록
      sort(cycle.begin(), cycle.end());
      cycles.push_back(cycle);
    }
    else
    {
      visit_node_order[nxt] = order + 1;
      visit_order_node[order + 1] = nxt;
      dfs(nxt, current, order + 1);
    }
  }
}

// greedy하게 중복된 node를 찾는다.
vector<int> find_duplicated_nodes(vector<int> a, vector<int> b)
{
  vector<int> duplicated_nodes;
  int i = 0, j = 0;
  while (i < a.size() && j < b.size())
  {
    if (a[i] == b[j])
    {
      duplicated_nodes.push_back(a[i++]);
      j++;
    }
    else if (a[i] < b[j])
    {
      i++;
    }
    else
    {
      j++;
    }
  }
  return duplicated_nodes;
}

int solution(int n, vector<vector<int>> edges)
{
  // input
  for (int i = 0; i < edges.size(); i++)
  {
    graph[edges[i][0]].push_back(edges[i][1]);
    graph[edges[i][1]].push_back(edges[i][0]);
  }

  // dfs
  for (int i = 1; i <= n; i++)
  {
    // dfs를 통해 한 번이라도 탐색된 노드 그룹은 더 이상 탐색할 필요가 없다.
    if (!checked[i])
    {
      // init
      fill_n(visit_node_order, n + 1, SIZE);
      fill_n(visit_order_node, n + 1, 0);
      visit_node_order[i] = 1;
      visit_order_node[1] = i;
      // dfs
      dfs(i, 0, 1);
    }
  }

  // cycle에 포함된 노드 중 중복된 노드를 찾는다.
  vector<int> duplicated_nodes = cycles[0];
  for (int i = 1; i < cycles.size(); i++)
  {
    vector<int> cycle = cycles[i];

    // TODO:
    cout << "cycle!" << '\n';
    for (int j = 0; j < cycle.size(); j++)
    {
      cout << cycle[j] << ' ';
    }
    cout << '\n';

    duplicated_nodes = find_duplicated_nodes(duplicated_nodes, cycle);
  }

  // TODO:
  cout << "DUP!" << '\n';
  for (int i = 0; i < duplicated_nodes.size(); i++)
  {
    cout << duplicated_nodes[i] << '\n';
  }

  // answer
  int answer = 0;
  for (int i = 0; i < duplicated_nodes.size(); i++)
  {
    answer += duplicated_nodes[i];
  }
  return answer;
}

int main()
{

  vector<vector<int>> v;
  vector<int> tmp;

  tmp.push_back(1);
  tmp.push_back(2);
  v.push_back(tmp);
  tmp.clear();

  tmp.push_back(1);
  tmp.push_back(3);
  v.push_back(tmp);
  tmp.clear();

  tmp.push_back(2);
  tmp.push_back(3);
  v.push_back(tmp);
  tmp.clear();

  tmp.push_back(2);
  tmp.push_back(4);
  v.push_back(tmp);
  tmp.clear();

  tmp.push_back(3);
  tmp.push_back(4);
  v.push_back(tmp);
  tmp.clear();

  int ans = solution(4, v);
  cout << "ans!" << '\n';
  cout << ans << '\n';

  return 0;
}