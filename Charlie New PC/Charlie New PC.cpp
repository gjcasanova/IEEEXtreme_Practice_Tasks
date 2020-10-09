#include <iostream>
#include <algorithm>

using namespace std;

int calcMaxPrice(int, int, int **, int *, int);

int main(int argc, char const *argv[])
{
    int t, b, n, result;

    cin >> t;

    for (int i = 0; i < t; i++)
    {
        cin >> b;
        cin >> n;

        int *sizes = new int[n];
        int **prices = new int *[n];

        for (int j = 0; j < n; j++)
        {
            cin >> sizes[j];
            prices[j] = new int[sizes[j]];
        }

        for (int j = 0; j < n; j++)
        {
            for (int k = 0; k < sizes[j]; k++)
            {
                cin >> prices[j][k];
            }
            sort(prices[j], prices[j] + sizes[j]);
        }

        result = b - calcMaxPrice(b, 0, prices, sizes, n);
        cout << (result < 0 ? 0 : result) << endl;
    }
    return 0;
}

int calcMaxPrice(int b, int index, int **matrix, int *sizes, int size_s)
{
    if (index == size_s)
        return b;

    int *options = matrix[index];
    int result = 2000000001, auxiliar;
    for (int i = 0; i < sizes[index]; i++)
    {
        if (options[i] <= b)
        {
            auxiliar = calcMaxPrice(b - options[i], index + 1, matrix, sizes, size_s);
            result = min(result, auxiliar);

            if (result == 0)
                return result;
        }
    }
    return result;
}
