from Crypto.Util.number import inverse, long_to_bytes
c = 62324783949134119159408816513334912534343517300880137691662780895409992760262021
p= 1899107986527483535344517113948531328331
q= 674357869540600933870145899564746495319033
phi = (p-1)*(q-1)
e =65537
d = inverse(e,phi)
n=1280678415822214057864524798453297819181910621573945477544758171055968245116423923
m= pow(c,d,n)

print(long_to_bytes(m))