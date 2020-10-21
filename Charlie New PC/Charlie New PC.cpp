#include <iostream>
#include <algorithm>

using namespace std;

int calcMaxPrice(int, int, int **, int *, int, int, int);

int main(int argc, char const *argv[])
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t, b, n, result, _min, _max;

    cin >> t;

    for (int i = 0; i < t; i++)
    {
        cin >> b;
        cin >> n;
        _min = _max = 0;

        int *sizes = new int[n];
        int **prices = new int *[n];

        for (int j = 0; j < n; j++)
        {
            cin >> sizes[j];
            int a = 1 / (sizes[j] - 1);
            prices[j] = new int[sizes[j]];
        }

        for (int j = 0; j < n; j++)
        {
            for (int k = 0; k < sizes[j]; k++)
            {
                cin >> prices[j][k];
                
            }
            sort(prices[j], prices[j] + sizes[j]);
            // _min += prices[j][0];
            _max += prices[j][sizes[j] - 1];
        }

        // cout << _min << " " << _max << endl;

        result = b - calcMaxPrice(b, 0, prices, sizes, n, _min, _max);
        cout << (result < 0 ? 0 : result) << endl;
    }
    return 0;
}

int calcMaxPrice(int b, int index, int **matrix, int *sizes, int size_s, int _min, int _max)
{
    if (index == size_s)
        return b;

    if (_max <= b)
        return b - _max;

    if (_min > b)
        return 2000000001;

    int *options = matrix[index];
    int result = 2000000001, auxiliar;

    _min -= options[0];
    _max -= options[sizes[index] - 1];

    for (int i = 0; i < sizes[index]; i++)
    {
        if (options[i] <= b)
        {
            auxiliar = calcMaxPrice(b - options[i], index + 1, matrix, sizes, size_s, _min, _max);
            result = min(result, auxiliar);

            if (result == 0)
                return result;
        }
    }
    return result;
}
