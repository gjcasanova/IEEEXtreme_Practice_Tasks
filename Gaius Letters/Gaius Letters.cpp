#include <bits/stdc++.h>

using namespace std;

const int MINUS_A = int('a');
const int MINUS_Z = int('z');
const int MAYUS_A = int('A');
const int MAYUS_Z = int('Z');
const int SPACE_JUMP = 14;

char decryptChar(char);

int main(int argc, char const *argv[])
{
    string ans, z;
    getline(cin, z);

    for (char c : z)
        ans += decryptChar(c);

    cout << ans << endl;
    return 0;
}

char decryptChar(char c)
{
    int ascii = int(c);
    int jumpedAscii = ascii + SPACE_JUMP;
    if (ascii >= MINUS_A && ascii <= MINUS_Z)
    {
        int space = MINUS_Z - jumpedAscii;
        return char(space < 0 ? MINUS_A - space - 1 : jumpedAscii);
    }
    else if (ascii >= MAYUS_A && ascii <= MAYUS_Z)
    {
        int space = MAYUS_Z - jumpedAscii;
        return char(space < 0 ? MAYUS_A - space - 1 : jumpedAscii);
    }

    return c;
}
