#include <iostream>
#include <vector>

using namespace std;

const int SIZE = 10;
bool is_used[SIZE];
char symbol[SIZE];
int n;
vector<int> max_num, min_num;

bool dfs(int, int, bool);
bool max_dfs(int, int);
bool min_dfs(int, int);

// 백트래킹 DFS
bool dfs(int nxt, int right, bool is_max)
{
  // 아직 사용하지 않은 숫자라면
  if (!is_used[right])
  {
    // push number
    is_used[right] = true;
    is_max ? max_num.push_back(right) : min_num.push_back(right);

    // do Next Step
    if (is_max)
    {
      if (max_dfs(nxt, right))
      {
        return true;
      }
    }
    else
    {
      if (min_dfs(nxt, right))
      {
        return true;
      }
    }

    // pop after fail
    is_used[right] = false;
    is_max ? max_num.pop_back() : min_num.pop_back();
  }

  return false;
}

// 최대 정수를 구하는 DFS
bool max_dfs(int now, int left)
{
  // END
  if (now >= n)
  {
    return true;
  }

  // 부등호가 '<' 인 경우
  if (symbol[now] == '<')
  {
    // left 보다 큰 최댓값을 선택
    for (int i = 9; i > left; i--)
    {
      if (dfs(now + 1, i, true))
      {
        return true;
      }
    }
  }
  // 부등호가 '>' 인 경우
  else
  {
    // left 보다 작은 최댓값을 선택
    for (int i = left - 1; i >= 0; i--)
    {
      if (dfs(now + 1, i, true))
      {
        return true;
      }
    }
  }
  return false;
}

// 최소 정수를 구하는 DFS
bool min_dfs(int now, int left)
{
  // END
  if (now >= n)
  {
    return true;
  }

  // 부등호가 '<' 인 경우
  if (symbol[now] == '<')
  {
    // left 보다 큰 최솟값을 선택
    for (int i = left + 1; i <= 9; i++)
    {
      if (dfs(now + 1, i, false))
      {
        return true;
      }
    }
  }
  // 부등호가 '>' 인 경우
  else
  {
    // left 보다 작은 최솟값을 선택
    for (int i = 0; i < left; i++)
    {
      if (dfs(now + 1, i, false))
      {
        return true;
      }
    }
  }
  return false;
}

int main()
{
  // input
  cin >> n;
  for (int i = 0; i < n; i++)
  {
    cin >> symbol[i];
  }

  // 최대 정수
  int max_ans = 0;
  // is_used 배열 초기화
  fill_n(is_used, SIZE, 0);
  for (int i = 9; i >= 0; i--)
  {
    if (max_dfs(0, i))
    {
      for (int j = 0; j <= n; j++)
      {
        max_ans = max_ans * 10 + max_num[j];
      }
      break;
    }
  }
  // 최소 정수
  int min_ans = 0;
  // is_used 배열 초기화
  fill_n(is_used, SIZE, 0);
  for (int i = 0; i <= 9; i++)
  {
    if (min_dfs(0, i))
    {
      for (int j = 0; j <= n; j++)
      {
        min_ans = min_ans * 10 + min_num[j];
      }
      break;
    }
  }

  cout << max_ans << '\n';
  cout << min_ans << '\n';

  return 0;
}