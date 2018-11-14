#include <iostream>

int main(int argc, char *argv[]) {
    int a=0;
    int b=1;

    do{
    	b=10*a;    	
    }while(b>a);

    std::cout << "b = " << b << std::endl;    
    return 0;
}