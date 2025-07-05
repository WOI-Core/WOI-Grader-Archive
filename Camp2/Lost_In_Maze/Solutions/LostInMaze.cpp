
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int main() {
    int n, m;
    cin >> n >> m;

    vector<string> maze(n);
    for (int i = 0; i < n; ++i) {
        cin >> maze[i];
    }

    int start_x, start_y;
    cin >> start_x >> start_y;

    int end_x, end_y;
    cin >> end_x >> end_y;

    queue<tuple<int, int, int>> q;
    q.push({start_x, start_y, 0});

    vector<vector<bool>> visited(n, vector<bool>(m, false));
    visited[start_x][start_y] = true;

    int min_dist = -1;

    while (!q.empty()) {
        int x = get<0>(q.front());
        int y = get<1>(q.front());
        int dist = get<2>(q.front());
        q.pop();

        if (x == end_x && y == end_y) {
            min_dist = dist;
            break;
        }

        // Possible moves (up, down, left, right)
        int dx[] = {0, 0, 1, -1};
        int dy[] = {1, -1, 0, 0};

        for (int i = 0; i < 4; ++i) {
            int new_x = x + dx[i];
            int new_y = y + dy[i];

            if (new_x >= 0 && new_x < n && new_y >= 0 && new_y < m && maze[new_x][new_y] == '.' && !visited[new_x][new_y]) {
                q.push({new_x, new_y, dist + 1});
                visited[new_x][new_y] = true;
            }
        }
    }

    cout << min_dist << endl;

    return 0;
}