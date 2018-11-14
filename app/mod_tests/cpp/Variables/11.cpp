#include <iostream>

int main(int argc, char *argv[]) {
    int a = 10, b = 5;
    int c = a * (a/2) +b;
    a=b;
    std::cout << "c = " << b << std::endl;
    
    return 0;
}