// vim: set noexpandtab tabstop=2:

#include <iostream>
#include <vector>

using namespace std;

int main()
{
	vector<int> v(2);
	v[1] = 1;
	v[2] = 2;
	auto iter1 = ++v.begin();
	auto iter2 = iter1;
	--iter2;
	cout << *iter1 << ", " << *iter2 << endl;
}
