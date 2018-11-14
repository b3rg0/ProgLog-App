#include <iostream>

int main(int argc, char *argv[]) {
    int a=5;
    int b=0;

    do{
    	a-=1;    	
    }while(a%3==0);
    std::cout << "a = " << a << std::endl;    

    return 0;
}