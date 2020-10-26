#include <iostream>

using namespace std;

int main(int argc, char const *argv[])
{
    int n, cb, cp, b, p, bt = 0, pt = 0, npb, npp;

    cin >> n >> cb >> cp;

    for (int i = 0; i < n; i++)
    {
        cin >> b >> p;
        bt += b;
        pt += p;
    }

    npb = bt / 10 + (bt % 10 == 0 ? 0 : 1);
    npp = pt / 10 + (pt % 10 == 0 ? 0 : 1);

    cout << npb * cb + npp * cp << endl;

    return 0;
}
