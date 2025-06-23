#include <iostream>
#include <vector>
#include <queue>
#include <limits>

using namespace std;

const int INF = numeric_limits<int>::max();

// Dijkstra's algorithm to find the shortest path from a single source
int dijkstra(int start, int end, int N, const vector<vector<pair<int, int>>>& adj) {
    if (start == end) {
        return 0;
    }

    vector<int> dist(N, INF);
    dist[start] = 0;

    // Priority queue to store {distance, vertex}
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    pq.push({0, start});

    while (!pq.empty()) {
        int d = pq.top().first;
        int u = pq.top().second;
        pq.pop();

        if (u == end) {
            return d;
        }

        if (d > dist[u]) {
            continue;
        }

        for (auto& edge : adj[u]) {
            int v = edge.first;
            int weight = edge.second;
            if (dist[u] + weight < dist[v]) {
                dist[v] = dist[u] + weight;
                pq.push({dist[v], v});
            }
        }
    }

    // If the end is not reachable, though problem implies it always is.
    return INF;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int N, E;
    cin >> N >> E;

    vector<vector<pair<int, int>>> adj(N);
    for (int i = 0; i < E; ++i) {
        int u, v, w;
        cin >> u >> v >> w;
        adj[u].push_back({v, w});
        adj[v].push_back({u, w});
    }

    long long total_time = 0;
    for (int i = 0; i < N - 1; ++i) {
        total_time += dijkstra(i, i + 1, N, adj);
    }

    cout << total_time << endl;

    return 0;
}
