#include <iostream>

using namespace std;

long int calcSteps(long int, long int);

int main(int argc, char const *argv[])
{
    long int n, a, b, result;

    cin >> n;

    for (int i = 0; i < n; i++)
    {
        cin >> a >> b;
        result = calcSteps(a, b);
        cout << result << endl;
    }
    return 0;
}

long int calcSteps(long int a, long int b)
{
    long int result = 0;
    while (a != b)
    {
        result++;
        if (a < b)
            b /= 2;
        else
            a /= 2;
    }
    return result;
}
