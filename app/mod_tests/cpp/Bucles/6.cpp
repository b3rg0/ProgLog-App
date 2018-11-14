#include <iostream>

int main(int argc, char *argv[]) {
    int a=5;
    int b=0;

    do{
    	b+=1;    	
    }while(b%3!=0);
    std::cout << "b = " << b << std::endl;    

    return 0;
}