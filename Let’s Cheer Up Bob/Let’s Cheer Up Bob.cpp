#include <bits/stdc++.h>

using namespace std;

vector<pair<int, int>> bobMoves, result = {
                                     {0, 1},
                                     {0, 2},
                                     {0, 3},
                                     {1, 1},
                                     {1, 2},
                                     {1, 3},
                                     {2, 1},
                                     {2, 2},
                                     {2, 3},
};

vector<vector<int>> board = {
    {0, 0, 0},
    {0, 0, 0},
    {0, 0, 0}};

bool checkVictory(int player)
{
    return board[0][0] == player && board[0][1] == player && board[0][2] == player ||
           board[1][0] == player && board[1][1] == player && board[1][2] == player ||
           board[2][0] == player && board[2][1] == player && board[2][2] == player ||

           board[0][0] == player && board[1][0] == player && board[2][0] == player ||
           board[0][1] == player && board[1][1] == player && board[2][1] == player ||
           board[0][2] == player && board[1][2] == player && board[2][2] == player ||

           board[0][0] == player && board[1][1] == player && board[2][2] == player ||
           board[2][0] == player && board[1][1] == player && board[0][2] == player;
}

void play()
{
    int i;
    for (i = 0; i < 9; i++)
    {
        if (board[bobMoves[i].first][bobMoves[i].second] == 0)
        {
            board[bobMoves[i].first][bobMoves[i].second] = 1;
            break;
        }
    }

    if (checkVictory(1))
    {
        vector<pair<int, int>> myMovements;

        for (int i = 0; i < 3; i++)
        {
            for (int j = 0; j < 3; j++)
            {
                if (board[i][j] == 2)
                {
                    myMovements.push_back({i + 1, j + 1});
                }
            }
        }

        if (myMovements.size() < result.size())
        {
            result = myMovements;
        }
        board[bobMoves[i].first][bobMoves[i].second] = 0;
        return;
    }

    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            if (board[i][j] == 0)
            {
                board[i][j] = 2;
                if (!checkVictory(2))
                {
                    play();
                }
                board[i][j] = 0;
            }
        }
    }
    board[bobMoves[i].first][bobMoves[i].second] = 0;
}

int main(int argc, char const *argv[])
{
    int row, col;

    for (int i = 0; i < 9; i++)
    {
        cin >> row >> col;
        bobMoves.push_back({row - 1, col - 1});
    }

    play();

    for (pair<int, int> movement : result)
    {
        cout << movement.first << " " << movement.second << endl;
    }

    return 0;
}
