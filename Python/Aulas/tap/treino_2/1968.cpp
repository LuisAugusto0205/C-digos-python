#include <iostream>
#include <math.h>

using namespace std;
typedef unsigned long long ll;

ll tabela[10000001];
ll a, b, k, lideres, pessoas, resp;

ll crivo(ll a, ll n, ll k)
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
	
	ll lid = 0;
	for (ll i = a; i <= n; i++)
	{
		if (tabela[i] == k) 
		{
			lid = (ll)(lid + 1);
		}
	}
	
	return lid;	
}

ll pont(ll base, ll exp)
{
	ll r = 1;
	while (exp > 0)
	{
		r = (ll)(r * base) ;
		r %= 1000000007;
		exp -= 1;
	}
	return r;
}

int main()
{
	cin >> a >> b >> k;
	lideres = crivo(a, b, k);
	pessoas = ((b - a) + 1) - lideres;

	cout << pont(lideres, pessoas) << endl;
}
