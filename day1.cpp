#include <iostream>
#include <fstream>
#include <string>
#include <list>
#include <vector>
#include <unordered_map>
using namespace std;

int main() {
    string filename = "day1.txt";
    ifstream inputFile(filename);

    // (not sure if i should use vector or lists)
    // seems vectors i can index, lists i cant.
    vector<int> left_vec;
    vector<int> right_vec;

    // for part 2
    unordered_map<int, int> right_map;

    if (inputFile.is_open()) {
        string line;
        while (getline(inputFile, line)) {
            // idk how to use strings in cpp this is so scuffed
            int index = 0;
            int left = stoi(&line[index]);
            int right;

            while (line[index] != ' ') {
                index++;
            }

            right = stoi(&line[index]);

            // left_nums.push_back(left);
            // right_nums.push_back(right);
            left_vec.push_back(left);
            right_vec.push_back(right);

            if (right_map.find(right) == right_map.end()) {
                right_map[right] = 1;
            } else {
                right_map[right] += 1;
            }

        }
        inputFile.close();

        sort(left_vec.begin(), left_vec.end());
        sort(right_vec.begin(), right_vec.end());

        int part1 = 0;

        for (int i  = 0; i < left_vec.size(); ++i) {
            part1 += abs(left_vec[i] - right_vec[i]);
        }

        cout << part1 << endl;

        int part2 = 0;
        for (int i  = 0; i < left_vec.size(); ++i) {
            int freq = 0;
            if (right_map.find(left_vec[i]) != right_map.end()) {
                freq = right_map[left_vec[i]];
            }
            part2 += left_vec[i] * freq;
        }

        cout << part2 << endl;
        
    } else {
        cerr << "unable to open file" << endl;
    }
}