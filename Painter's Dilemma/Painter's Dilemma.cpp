#include <bits/stdc++.h>

using namespace std;

int solve(vector<int> c)
{
    int result = 0;
    vector<pair<int, int>> b(c.size());

    for (int i = 1; i < b.size(); i++)
    {
        if (c[i] != b[i - 1].first && c[i] != b[i - 1].second)
        {
            vector<int>::iterator first, second;
            first = find(c.begin() + i + 1, c.end(), b[i - 1].first);
            second = find(c.begin() + i + 1, c.end(), b[i - 1].second);
            if (first >= second)
            {
                b[i].first = c[i];
                b[i].second = b[i - 1].second;
            }
            else
            {
                b[i].second = c[i];
                b[i].first = b[i - 1].first;
            }
            result++;
        }
        else
        {
            b[i] = b[i - 1];
        }
    }
    return result;
}

int main(int argc, char const *argv[])
{
    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;
        vector<int> c(n + 1);
        for (int i = 1; i < c.size(); i++)
        {
            cin >> c[i];
        }
        cout << solve(c) << endl;
    }
    return 0;
}
