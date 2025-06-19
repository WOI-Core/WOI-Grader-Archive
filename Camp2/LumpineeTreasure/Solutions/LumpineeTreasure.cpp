#include <iostream>

using namespace std;

int arr[11][11];

int solve(int x, int y, int k) {
  if (x <= 0 || y <= 0 || k == 0)
    return 0;

  return max(solve(x - 1, y, k - 1), solve(x, y - 1, k - 1)) + arr[x][y];
}

int main() {
  ios_base::sync_with_stdio(0), cin.tie(0);

  int m, n, k;
  cin >> m >> n >> k;

  for (int i = 1; i <= m; i++) {
    for (int j = 1; j <= n; j++) {
      cin >> arr[i][j];
    }
  }

  int ans = 0;
  for (int i = 1; i <= m; i++) {
    for (int j = 1; j <= n; j++) {
      ans = max(ans, solve(i, j, k));
    }
  }
  cout << ans << '\n';

  return 0;
}
