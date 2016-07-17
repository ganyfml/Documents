// vim: set noexpandtab tabstop=2:

#include <iostream>
#include <array>
using namespace std;

int main()
{
	array<bool, 4> a{};
	cout << a.size() << endl;
	for(int i = 0; i < 4; ++i)
	{
		cout << a[i] << endl;
	}
}
