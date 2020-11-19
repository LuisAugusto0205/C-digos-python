#include <iostream>

using namespace std;
typedef long long ll;

ll tabela[2000001];
ll n, resp = 0;
int pref[2000001];

ll crivo(ll n)
{
	ll i = 1;
	while (i * i <= n)
	{
		tabela[i * i] += 1;
		
		for(ll j = i * i + i; j <= n; j += i)
		{
			tabela[j] += 2;
		}
		i++;
	}
	
}

int main()
{
	crivo(2000001);
	for (ll i = 2; i <= n; i++)
	{
		pref[i] = pref[i - 1];
		if (tabela[tabela[i]] == 2)
		{
			pref[i] += 1;
		}
	}
	
	while(cin >> n)
	{
		cout <<	pref[n] << endl;
	}
	return 0;
}
