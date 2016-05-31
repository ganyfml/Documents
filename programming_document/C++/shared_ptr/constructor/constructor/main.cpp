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
  int i = 6;
  shared_ptr<myClass> test = std::make_shared<myClass>(i);
  test->display();
}
