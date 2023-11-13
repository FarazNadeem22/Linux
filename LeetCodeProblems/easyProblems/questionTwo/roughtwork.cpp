#include <iostream>
#include <cmath>

int main()
{
    int number = 21212;
    int numDigits = std::to_string(number).size()/2;
    int reversed = 0;

    int powerOfTen = std::pow(10, numDigits);
    int digit = number % powerOfTen;
    std::cout << number << " % " << powerOfTen << " = " << digit << std::endl;

    while (digit != 0)
    {
        int number = digit % 10;
        reversed = reversed * 10 + number;
        digit = digit /10;
    }

    std::cout<< "Reversed = " << reversed <<std::endl;
    return 0;
}