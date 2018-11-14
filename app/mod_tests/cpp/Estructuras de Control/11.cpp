#include <iostream>

int main(int argc, char *argv[]) {
    int a = 10, b = 5;
    int c = 10/2;
    a= a + c;
    int d=a*a;

    if(d%2==0){    	
        c=d;
    }
    else if(d%5==0){    	
        c=a*b;
    }
    else{
        c=a;
    }
    std::cout << "c = " << c << std::endl;	  
    
    return 0;
}