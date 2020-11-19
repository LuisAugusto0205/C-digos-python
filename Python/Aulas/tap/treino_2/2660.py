def mdc(a, b):
    if not b: return a
    return mdc(b, a%b)

def mmc(*numeros):
	mmc = numeros[0]
	for x in numeros[1:]:
		mmc *= (x//mdc(mmc, x))
	return mmc

def main():
    n, lim = [int(x) for x in input().split()]
    periodos = [int(x) for x in input().split()]
    
    a = mmc(*periodos)
    resp = mmc_resp = 0

    for b in range(1, lim + 1):
        mmc_davez = mmc(a, b)
        
        if mmc_davez <= lim and mmc_resp < mmc_davez:
            
            mmc_resp = mmc_davez
            resp = b

    print(resp)

main()
