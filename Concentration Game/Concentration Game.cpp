#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>
#include <map>

using namespace std;

int main(int argc, char const *argv[])
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, cardA, cardB, matches = 0;
    string line, aux;

    cin >> n;
    cin.ignore();

    map<int, int> cards;

    for (int i = 1; (i <= n) && (matches != n); i++)
    {
        cout << i << " " << 2 * n - i + 1 << endl;
        getline(cin, line);

        if (line == "MATCH")
        {
            matches++;
        }
        else
        {
            istringstream iss(line);
            iss >> cardA >> cardB;

            if (cards.find(cardA) == cards.end())
            {
                cards[cardA] = i;
            }
            else
            {
                cout << cards[cardA] << " " << i << endl;
                getline(cin, aux);
                matches++;
            }

            if (cards.find(cardB) == cards.end())
            {
                cards[cardB] = 2 * n - i + 1;
            }
            else
            {
                cout << cards[cardB] << " " << 2 * n - i + 1 << endl;
                getline(cin, aux);
                matches++;
            }
        }
    }

    cout << -1 << endl;
    return 0;
}
