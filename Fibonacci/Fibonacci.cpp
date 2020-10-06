#include <iostream>

using namespace std;

long int fibonacci(int);

long int cache[60];

int main(int argc, char const *argv[])
{
    int n;
    cin >> n;

    long long int generation;

    for (int i = 0; i < n; i++)
    {
        cin >> generation;
        cout << fibonacci(generation % 60) % 10 << endl;
    }
    return 0;
}

long int fibonacci(int number){
    if(cache[number]) return cache[number];
    if(number<=1) return 1;
    long int result = fibonacci(number-1) + fibonacci(number-2);
    cache[number] = result;
    return result;
}
