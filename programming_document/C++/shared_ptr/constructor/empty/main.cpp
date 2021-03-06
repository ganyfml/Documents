#include <iostream>
#include <memory>

using namespace std;

class myClass
{
  public:
    myClass(int a)
    {
      element = a;
      cout << "myClass constructed" << endl;
    }

    ~myClass()
    {
      cout << "myClass destroyed" << endl;
    }
    
    void display()
    {
      cout << element << endl;
    }

  private:
    int element;
};

int main()
{
  shared_ptr<myClass> test;
  if(test == nullptr)
  {
    cout << "empty shared_ptr \n";
  }
  else
  {
    cout << "pointer not empty \n";
  }
}
