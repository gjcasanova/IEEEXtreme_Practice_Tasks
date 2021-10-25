#include <bits/stdc++.h>

using namespace std;

long long b, result;
int n;
vector<int> sizes;
vector<vector<long long>> prices;

void solve(int, long long);

int main(int argc, char const *argv[])
{
    int t;
    cin >> t;

    while (t--)
    {
        cin >> b;
        cin >> n;
        sizes = vector<int>(n);
        prices.clear();
        result = 0;

        for (int i = 0; i < n; i++)
        {
            cin >> sizes[i];
            prices.push_back(vector<long long>(sizes[i]));
        }

        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < sizes[i]; j++)
            {
                cin >> prices[i][j];
            }
        }

        solve(0, 0);
        cout << result << endl;
    }

    return 0;
}

void solve(int componentIdx, long long accum)
{
    if (componentIdx == n)
    {
        result = max(accum, result);
        return;
    }

    for (int i = 0; i < prices[componentIdx].size(); i++)
    {
        long long newAccum = prices[componentIdx][i] + accum;
        if (newAccum <= b)
        {
            solve(componentIdx + 1, newAccum);
        }
    }

    // result = 0;
    // for (int i = 0; i < prices.size(); i++)
    // {
    //     for (int j = 0; j < prices[i].size(); j++)
    //     {
    //         cout << prices[i][j] << " ";
    //     }
    //     cout << endl;
    // }
}