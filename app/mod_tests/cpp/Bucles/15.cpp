#include <iostream>

int main(int argc, char *argv[]) {
    int a=0;
    int b=2;

    for(int i=0; i<b; i++){
    	b=a+i;
    }

    std::cout << "b = " << b << std::endl;    
    return 0;
}