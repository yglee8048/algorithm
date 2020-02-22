#include <string>
#include <vector>
#include <unordered_set>

using namespace std;

const int SIZE = 101;

// g_set[0][number] : number에게 진 사람들의 set
// g_set[1][number] : number를 이긴 사람들의 set
unordered_set<int> g_set[2][SIZE];
bool is_checked[2][SIZE];

// x > y, y > z 라면, x > z 이다.
// number에게 진/이긴 사람들의 목록을 반환한다.
unordered_set<int> dfs(int is_losed, int number)
{
  // 이미 확인했으면 다시 한 번 확인할 필요는 없다.
  if (is_checked[is_losed][number])
  {
    return g_set[is_losed][number];
  }

  // 확인했다고 체크
  is_checked[is_losed][number] = true;

  // insert를 위한 임시 set
  unordered_set<int> l_set = g_set[is_losed][number];

  // target = number에게 진/이긴 사람
  for (auto target : g_set[is_losed][number])
  {
    // target of targets = target에게 진/이긴 사람
    for (auto target_of_targets : dfs(is_losed, target))
    {
      // number는 target에게 진/이긴 사람들에게 이길/질 수 있다.
      l_set.insert(target_of_targets);
    }
  }

  // dfs를 통해 number에게 진/이긴 사람들을 모두 반환한다.
  return g_set[is_losed][number] = l_set;
}

int solution(int n, vector<vector<int>> results)
{
  int answer = 0;

  for (vector<int> result : results)
  {
    int winner = result[0];
    int loser = result[1];

    // g_set[0][number] : number에게 진 사람들의 set
    g_set[0][winner].insert(loser);
    // g_set[1][number] : number를 이긴 사람들의 set
    g_set[1][loser].insert(winner);
  }

  for (int i = 1; i <= n; i++)
  {
    // i를 이긴 사람의 수 + i가 이긴 사람의 수 = n - 1 이면, i의 순위는 결정될 수 있다.
    if (dfs(0, i).size() + dfs(1, i).size() == n - 1)
    {
      answer++;
    }
  }

  return answer;
}