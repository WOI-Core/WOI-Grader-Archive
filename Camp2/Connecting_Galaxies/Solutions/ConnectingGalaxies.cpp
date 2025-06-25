
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Edge {
    int u, v, w;
};

int find(vector<int>& parent, int i) {
    if (parent[i] == i)
        return i;
    return parent[i] = find(parent, parent[i]);
}

void unite(vector<int>& parent, vector<int>& rank, int u, int v) {
    u = find(parent, u);
    v = find(parent, v);

    if (u != v) {
        if (rank[u] < rank[v])
            swap(u, v);
        parent[v] = u;
        if (rank[u] == rank[v])
            rank[u]++;
    }
}

int main() {
    int n, m;
    cin >> n >> m;

    vector<Edge> edges(m);
    for (int i = 0; i < m; ++i) {
        cin >> edges[i].u >> edges[i].v >> edges[i].w;
    }

    sort(edges.begin(), edges.end(), [](const Edge& a, const Edge& b) {
        return a.w < b.w;
    });

    vector<int> parent(n + 1);
    vector<int> rank(n + 1, 0);
    for (int i = 1; i <= n; ++i) {
        parent[i] = i;
    }

    int mst_weight = 0;
    for (const Edge& edge : edges) {
        if (find(parent, edge.u) != find(parent, edge.v)) {
            mst_weight += edge.w;
            unite(parent, rank, edge.u, edge.v);
        }
    }

    cout << mst_weight << endl;

    return 0;
}