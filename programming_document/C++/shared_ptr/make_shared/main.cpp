#include <iostream>
#include <memory>

int main()
{
  std::shared_ptr<int> int_ptr = std::make_shared<int>(12);
  std::cout << *int_ptr << std::endl;
}

