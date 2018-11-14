#include <iostream>

int main(int argc, char *argv[]) {
    int a = 10, b = 5;
    int c = a * b;
    if(c==50/2){
    	std::cout << "c = " << ( a / b ) << std::endl;	
    }
    else if(c>30){
    	std::cout << "c = " << ( a + b ) << std::endl;		
    }
    else{
    	std::cout << "c = " << ( a * b ) << std::endl;	
    }   
    
    return 0;
}