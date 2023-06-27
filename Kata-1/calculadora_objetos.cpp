#include <iostream>
using namespace std;


class Calculator
{
	private:
		int a;
		int b;
	public:
		Calculator(int , int); 
 	 
 		int add(); 
		int sub();
		int div();
		int mult();
		
};

Calculator::Calculator(int _a, int _b)
{
	a = _a;
	b = _b;
}

int Calculator::add()
{
	return a+b;
}

int Calculator::sub()
{
	return a-b;
}

int Calculator::div()
{
	return a/b;
}

int Calculator::mult()
{
	return a*b;
}
//-------------------------------------------------------------------------------
int main()
{
	Calculator* calculator = new Calculator(4,6);
	cout << calculator->add();
	delete calculator;
	return 0;
}