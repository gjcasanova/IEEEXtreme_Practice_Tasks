#include <bits/stdc++.h>

using namespace std;

int main(int argc, char const *argv[])
{
    int t, n;
    cin >> t;

    while (t--)
    {
        cin >> n;
        bool has_dice = true;
        int total_alice = 0, total_bob = 0, first_dice_six = 0, second_dice_six = 0;

        for (int i = 0; i < n; i++)
        {
            int a, b;
            cin >> a >> b;
            total_alice += a;
            total_bob += b;
            if (a == 6)
                has_dice ? first_dice_six++ : second_dice_six++;

            if (b == 6)
                has_dice ? second_dice_six++ : first_dice_six++;

            if (total_alice != total_bob)
                has_dice = !has_dice;
        }

        cout << (first_dice_six > second_dice_six ? 1 : 2) << endl;
    }

    return 0;
}
