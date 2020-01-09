#include <iostream>

using namespace std;

const int SIZE = 501;
int n, m;
char map[SIZE][SIZE];     // 문자 정보를 기록
bool done[SIZE][SIZE];    // 탐색 여부를 기록
bool can_out[SIZE][SIZE]; // 탈출 가능한 칸을 기록
int cnt = 0;              // 탈출 가능한 칸의 개수를 기록

bool dfs(int i, int j)
{
  // 밖으로 나옴
  if (i < 0 || i >= n || j < 0 || j >= m)
  {
    return true;
  }

  // 이미 확인 한 칸은 더 이상 확인할 필요 없음
  if (done[i][j])
    return can_out[i][j];

  // 확인했다고 체크
  done[i][j] = true;

  // 이동
  switch (map[i][j])
  {
  case 'U':
    if (dfs(i - 1, j))
    {
      can_out[i][j] = true;
      cnt++;
      return true;
    }
    return false;
  case 'R':
    if (dfs(i, j + 1))
    {
      can_out[i][j] = true;
      cnt++;
      return true;
    }
    return false;
  case 'D':
    if (dfs(i + 1, j))
    {
      can_out[i][j] = true;
      cnt++;
      return true;
    }
    return false;
  case 'L':
    if (dfs(i, j - 1))
    {
      can_out[i][j] = true;
      cnt++;
      return true;
    }
    return false;
  }
}

int main()
{
  // 입력
  cin >> n >> m;
  for (int i = 0; i < n; i++)
  {
    for (int j = 0; j < m; j++)
    {
      cin >> map[i][j];
    }
  }

  // dfs + dp 탐색
  for (int i = 0; i < n; i++)
  {
    for (int j = 0; j < m; j++)
    {
      dfs(i, j);
    }
  }

  cout << cnt << '\n';

  return 0;
}