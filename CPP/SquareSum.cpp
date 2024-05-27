#include <vector>
#include <iostream>

using namespace std;

int square_sum(const std::vector<int>& numbers){
    int totalSum = 0;
    for(const int& i : numbers) 
        totalSum += i*i;
    return totalSum;
}

int main(){
    cout << square_sum({1,2,2});
}

// Original kata: https://www.codewars.com/kata/515e271a311df0350d00000f
// My solution: https://www.codewars.com/kata/reviews/5902209f33364eb08900033e/groups/66542d767978997d6306bbab