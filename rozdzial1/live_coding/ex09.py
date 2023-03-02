"""
Formatowanie tekstu

Uzupełnij kod tak, aby wykonywał określone zadania
"""

# korzystając z poniższych danych, utwórz tekst
# opisujący obliczanie obwodu koła w stylu
# "2 * 3.14 * 7.0 = 43.98"
# wykorzystaj 3 poznane metody formatowania tekstu
n = 2
pi = 3.141592
r = 7

res=n*pi*r

print(f"{n} * {pi:.2f} * {r} = {res:.2f}")
#print(str(n)+" * %.2f"%pi+" * "+str(r)+" = %.2f" %res)
print("%d * %.2f * %d = %.2f"%(n,pi,r,res))
print(("{} * {:.2f} * {} = {:.2f}").format(n,pi,r,res))
print(("{q} * {w:.2f} * {e} = {r:.2f}").format(w=pi,r=res,q=n,e=r))

