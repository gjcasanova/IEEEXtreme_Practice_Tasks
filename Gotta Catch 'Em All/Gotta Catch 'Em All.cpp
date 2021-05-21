#include <bits/stdc++.h>

using namespace std;

int main(int argc, char const *argv[])
{
    int r, c;

    cin >> r >> c;

    vector<vector<long long>> grid(r + 1, vector<long long>(c + 1, 0)),
        dp_op(r + 1, vector<long long>(c + 1, LLONG_MAX)),
        dp_ac(r + 1, vector<long long>(c + 1, LLONG_MIN));

    for (int i = 1; i <= r; i++)
    {
        for (int j = 1; j <= c; j++)
        {
            cin >> grid[i][j];
        }
    }

    for (int i = 1; i <= r; i++)
    {
        for (int j = 1; j <= c; j++)
        {
            long long best_previous = (i == 1 && j == 1) ? 0 : max(dp_ac[i - 1][j], dp_ac[i][j - 1]);
            dp_ac[i][j] = best_previous + grid[i][j];
        }
    }

    for (int i = 1; i <= r; i++)
    {
        for (int j = 1; j <= c; j++)
        {
            long long best_previous = (i == 1 && j == 1) ? 1 : min(dp_op[i - 1][j], dp_op[i][j - 1]);
            dp_op[i][j] = max(best_previous, 1 - dp_ac[i][j]);
        }
    }

    cout << dp_op[r][c] << endl;
    return 0;
}
