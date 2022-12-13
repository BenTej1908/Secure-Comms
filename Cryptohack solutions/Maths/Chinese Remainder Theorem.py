
from sympy.ntheory.modular import crt


m = [5,11,17]
v = [2,3,5]

crt_m_v = crt(m, v)
print((crt_m_v[0]))
