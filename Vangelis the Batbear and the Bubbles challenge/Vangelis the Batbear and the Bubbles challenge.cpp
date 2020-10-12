#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int **createMatrix(int);
int travel(int, int, int **, int, vector<int>);

int main(int argc, char const *argv[])
{
    int t, n, m, a, b;
    cin >> t;

    for (int i = 0; i < t; i++)
    {
        cin >> n >> m;
        int **adjMatrix = createMatrix(n);

        for (int j = 0; j < m; j++)
        {
            cin >> a >> b;
            adjMatrix[a][b] = 1;
            adjMatrix[b][a] = 1;
        }

        int loop = 0;
        for (int j = 0; j < n; j++)
        {
            vector<int> visited;
            if (travel(-1, j, adjMatrix, n, visited))
            {
                loop = 1;
                break;
            }
        }
        cout << loop << endl;
    }

    return 0;
}

int travel(int pre, int current, int **adjMat, int size, vector<int> visited)
{
    if (find(visited.begin(), visited.end(), current) != visited.end())
        return 1;

    visited.insert(visited.end(), current);

    int *destinies = adjMat[current];

    for (int i = 0; i < size; i++)
    {
        if (i != pre && destinies[i] == 1)
        {
            int loop = travel(current, i, adjMat, size, visited);
            if (loop == 1)
                return 1;
        }
    }
    return 0;
}

int **createMatrix(int size)
{
    int **mat;
    mat = new int *[size];

    for (int i = 0; i < size; i++)
    {
        mat[i] = new int[size];

        for (int j = 0; j < size; j++)
        {
            mat[i][j] = 0;
        }
    }
    return mat;
}
