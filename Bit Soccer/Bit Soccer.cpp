#include <iostream>

using namespace std;

bool isPosible(long long int *, long long int, int);
bool isValid(long long int, long long int);

int main(int argc, char const *argv[])
{
    int n, q;
    long long int g;

    cin >> n;
    long long int p[n];

    for (int i = 0; i < n; i++)
        cin >> p[i];

    cin >> q;

    for (int i = 0; i < q; i++)
    {
        cin >> g;
        if (isPosible(p, g, n))
            cout << "YES" << endl;
        else
            cout << "NO" << endl;
    }
    return 0;
}

bool isPosible(long long int *p, long long int q, int size)
{
    long long int result = 0;
    for (int i = 0; i < size; i++)
    {
        if (isValid(q, p[i]))
        {
            result |= p[i];
        }
    }
    return result == q;
}

bool isValid(long long int base, long long int n)
{
    bool result = true;
    while (n != 0)
    {
        if (base % 2 == 0 && n % 2 == 1)
        {
            result = false;
            break;
        }
        base >>= 1;
        n >>= 1;
    }
    return result;
}