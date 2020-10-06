#include <iostream>

using namespace std;

int main(int argc, char const *argv[])
{
    long int j, k, result = 0;

    cin >> j >> k;

    while ((j >= 1 && k >= 2) || (j >= 2 && k >= 1))
    {
        if (j >= 2 * k || k >= 2 * j)
        {
            result += min(j, k);
            break;
        }
        else if (j == k)
        {
            result += (j * 2) / 3;
            break;
        }
        else
        {
            result++;
            if (j < k)
            {
                j--;
                k -= 2;
            }
            else
            {
                k--;
                j -= 2;
            }
        }
    }

    cout << result << endl;
    return 0;
}
