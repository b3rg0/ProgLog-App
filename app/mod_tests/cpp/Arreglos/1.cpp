#include <iostream>

int main(int argc, char *argv[]) {
    int a [5];
    a[0]=5;
    a[1]=4;
    a[2]=3;
    a[3]=2;
    a[4]=1;
    int v=a[1]+a[2];
    std::cout << "v = " << v <<std::endl;  
    return 0;
}