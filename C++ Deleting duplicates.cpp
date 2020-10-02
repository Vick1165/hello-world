#include <iostream>
using namespace std;

void deleteDup(st)
{
  int n = st.size();
  vector<char> rv;
  int flag;
  for (int i = 0; i < n; i++)
  {

    flag == 0;
    for (int j = 0; j < i; j++)
      if (st[i] == st[j])
        flag++;
    if (flag == 0)
      rv.push(st[i]);
  }
  for (int i = 0; i < rv.size(); i++)
    cout << rv[i];
}

int main()
{
  string st;
  getline(cin, st);
  deleteDup(st);
  return 0;
}