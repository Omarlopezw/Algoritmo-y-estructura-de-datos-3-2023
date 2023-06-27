#include <iostream>

using namespace std;


double sum(double data_1, double data_2);
double subtraction(double data_1, double data_2);
double division(double data_1, double data_2);
double multiplication(double data_1, double data_2);

void option();

int main () {

    sum(3,3); 
    subtraction(5,8); 
    division(9,5);
    multiplication(3,8);

    
	return 0;
}




double sum(double data_1, double data_2)
{
    return data_1 + data_2;
}


double subtraction(double data_1, double data_2)
{

    return data_1 - data_2;
}


double division(double data_1, double data_2)
{
    return data_1 / data_2;
}

double multiplication(double data_1, double data_2)
{

    return data_1 * data_2;;
}