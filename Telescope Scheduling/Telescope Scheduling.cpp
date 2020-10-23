#include <iostream>
#include <algorithm>
#include <cstring>

using namespace std;

struct star
{
    int start, finish, desirability;
};

bool compareStars(star a, star b)
{
    return a.finish < b.finish;
}

int main(int argc, char const *argv[])
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, maxHour = 0;
    star ss;

    cin >> n;
    star stars[n];

    for (int i = 0; i < n; i++)
    {
        cin >> ss.start >> ss.finish >> ss.desirability;
        stars[i] = ss;
        maxHour = max(maxHour, ss.finish);
    }

    sort(stars, stars + n, compareStars);

    int tdp[2][maxHour + 1], newStart;
    memset(tdp, 0, sizeof tdp);

    for (int i = 1; i <= n; i++)
    {
        for (int j = 0; j <= maxHour; j++)
        {
            ss = stars[i - 1];
            if (ss.finish <= j)
            {
                newStart = max(0, ss.start - 1);
                tdp[1][j] = max(ss.desirability + tdp[0][newStart], tdp[0][j]);
            }
            else
            {
                tdp[1][j] = tdp[0][j];
            }
        }
        copy(tdp[1], tdp[1] + maxHour + 1, tdp[0]);
    }

    cout << tdp[1][maxHour] << endl;

    return 0;
}
