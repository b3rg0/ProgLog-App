#include <iostream>

int main(int argc, char *argv[]) {
    int a = 10, b = 5;
    int c = 10/2;
    a= a + c;

    if(a%2==0){    	
        a=a*c;
    }
    else if(a%5==0){    	
        a=b*c;
    }
    else{
        a=c;
    }
    std::cout << "a = " << a << std::endl;	  
    
    return 0;
}