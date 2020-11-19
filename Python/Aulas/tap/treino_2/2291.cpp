#include <iostream>

using namespace std;

long long tabela[1000001];
long long n;

long long crivo(int n)
{
	int i = 1;
	while (i * i <= n)
	{
		tabela[i * i] += i;
		
		for(int j = i * i + i; j <= n; j += i)
		{
			tabela[j] += i + int(j/i);
		}
		i++;
	}
	
	for (int i = 1; i <= n; i++)
	{
		tabela[i] += tabela[i - 1];
	}
		
}

int main()
{
	crivo(1000000);
	cin >> n;
	while (n > 0)
	{
		cout << tabela[n] << endl;
		cin >> n;
	}
	return 0;
}
