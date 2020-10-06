#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main(int argc, char *argv[])
{
    int n;
    cin >> n;

    string name;
    int height;

    vector<string> data[131];

    for (int i = 0; i < n; i++)
    {
        cin >> name >> height;
        int rowIndex = height - 120;

        bool wasInserted = false;
        for (int j = 0; j < data[rowIndex].size(); j++)
        {
            if (data[rowIndex][j].compare(name) > 0)
            {
                data[rowIndex].insert(data[rowIndex].begin() + j, name);
                wasInserted = true;
                break;
            }
        }
        if (!wasInserted)
            data[rowIndex].insert(data[rowIndex].end(), name);
    }

    int min = 1, max;

    for (int i = 0; i < sizeof(data) / sizeof(*data); i++)
    {
        if (data[i].size())
        {
            for (int j = 0; j < data[i].size(); j++)
                cout << data[i][j] << " ";

            max = min + data[i].size() - 1;
            cout << min << " " << max << endl;
            min = max + 1;
        }
    }
}
