#include <iostream>

using namespace std;

void printArray(int[], char s, int);

int main(int argc, char const *argv[])
{
    int n, index = 0, corrects, auxiliar;
    cin >> n;

    int bits[n];

    for (int i = 0; i < n; i++)
        bits[i] = 0;

    printArray(bits, 'Q', n);
    cin >> corrects;

    do
    {
        bits[index] = 1;
        printArray(bits, 'Q', n);
        cin >> auxiliar;

        if (corrects > auxiliar)
            bits[index] = 0;
        else
            corrects = auxiliar;
        index++;
    } while (corrects != n);

    printArray(bits, 'A', n);
    return 0;
}

void printArray(int *array, char s, int size)
{
    cout << s << " ";
    for (int i = 0; i < size; i++)
        cout << array[i] << " ";
    cout << endl;
}
