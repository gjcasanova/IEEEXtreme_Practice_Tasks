#include <bits/stdc++.h>

using namespace std;

int m, n;
long long c;
char cell;

int countLiveNeighbours(vector<vector<bool>> &board, int idxI, int idxJ)
{
    int result = 0;
    for (int i = idxI - 1; i <= idxI + 1; i++)
    {
        for (int j = idxJ - 1; j <= idxJ + 1; j++)
        {
            if (board[i][j])
                result++;
        }
    }
    if (board[idxI][idxJ])
        result--;
    return result;
}

vector<vector<bool>> nextGen(vector<vector<bool>> &board)
{
    vector<vector<bool>> result = board;
    int numberOfNeighbours;
    for (int i = 1; i <= m; i++)
    {
        for (int j = 1; j <= n; j++)
        {
            numberOfNeighbours = countLiveNeighbours(board, i, j);
            if (board[i][j])
            {
                if (numberOfNeighbours < 2 || numberOfNeighbours > 3)
                {
                    result[i][j] = false;
                }
            }
            else
            {
                if (numberOfNeighbours == 3)
                {
                    result[i][j] = true;
                }
            }
        }
        result[i][0] = result[i][n];
        result[i][n + 1] = result[i][1];
    }
    result[0] = result[m];
    result[m + 1] = result[1];

    return result;
}

int main(int argc, char const *argv[])
{
    cin >> m >> n >> c;

    vector<vector<bool>> board;
    vector<vector<vector<bool>>> previousBoards;

    for (int i = 0; i < m; i++)
    {
        board.push_back(vector<bool>{});
        for (int j = 0; j < n; j++)
        {
            cin >> cell;
            board[i].push_back(cell == '*');
        }
        board[i].push_back(board[i][0]);
        board[i].insert(board[i].begin(), board[i][n - 1]);
    }
    board.push_back(board[0]);
    board.insert(board.begin(), board[m - 1]);

    while (c--)
    {
        vector<vector<vector<bool>>>::iterator posFinded = find(previousBoards.begin(), previousBoards.end(), board);
        if (posFinded == previousBoards.end())
        {
            previousBoards.push_back(board);
            board = nextGen(board);
        }
        else
        {
            int idx = distance(previousBoards.begin(), posFinded);
            board = previousBoards[idx + (c + 1) % (previousBoards.size() - idx)];
            break;
        }
    }

    for (int i = 1; i <= m; i++)
    {
        for (int j = 1; j <= n; j++)
        {
            if (board[i][j])
                cout << '*';
            else
                cout << '-';
        }
        cout << endl;
    }

    return 0;
}
