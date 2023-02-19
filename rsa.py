import math
import random
import sys

# print(sys.getrecursionlimit())
sys.setrecursionlimit(2000)

# p = 0x00e8802fc975ea7957c4cd52eefb94bc525b2a3b3425ca096809e3278fb07898b702944d99acc78c9c80cf9af564254ed43514b2a4d3f6962e81722c2831464873
# q = 0x00de7031c331f2f803529e00d4ac9c2733ec0c5166c666c9071581b904568695b6dfee552b453ebe2984616346a6e413d30d38c1f478f95f87dd6e2ba72e9a7919

e = 65537
p = 12177051251161569372485386095581113995371981564467682170333375059009389171930701692589020961154555611385680445095313611346232424278997853670169398181513331
q = 11650036942066247175050685961854390555508503339169222225100688631870953124897669163245852687602781587985777228316285895516366794992212771145580299129878809

phi = (p - 1) * (q - 1)

def createTestVals(k, N):
    #This is simply a function I wrote to make a random array of k a values
    testVals = []
    for a in range(0, k):
        val = random.randint(1, N-1)
        testVals.append(val)
    return testVals

def mod_exp(x, y, N):
    #This is an implementation of modular exponentiation
    #Time complexity: O(n^3)
    #Space complexity: O(n^2)
    if y == 0:
        return 1
    z = mod_exp(x, math.floor(y/2), N)
    if y % 2 == 0:
        return (z**2) % N
    else:
        return (x * z**2) % N

def gcd(a, b):
    if (b == 0):
        return a
    else:
        return gcd(b, a % b)

def miller_rabin(N,k):
    #Time complexity: O(kn^4)
    #Space complexity: O(n^2)
    testVals = createTestVals(k, N)
    #Miller rabin applies the modular exponentiation found in Fermat's theorem
    for a in testVals:
        n = N - 1
        if mod_exp(a, n, N) != 1:
            return 'composite'
        #If the first check fails, it keeps on using modular exponentiation, taking the square root of the result each time, until the exponent becomes odd and that is no longer possible
        while (n % 2 == 0):
            if mod_exp(a, n, N) == N - 1:
                break
            elif mod_exp(a, n, N) != 1:
                return 'composite'
            n = n/2
    return 'prime'

# function inverse(a, n)
#     t := 0;     newt := 1
#     r := n;     newr := a
#
#     while newr ≠ 0 do
#         quotient := r div newr
#         (t, newt) := (newt, t − quotient × newt)
#         (r, newr) := (newr, r − quotient × newr)
#
#     if r > 1 then
#         return "a is not invertible"
#     if t < 0 then
#         t := t + n
#
#     return t

# check if (e*d)%phi(n) == 1
n = p * q
print(n)
def extended_euclid(e, n):
    d = 0
    new_d = 1
    r = n
    new_r = e

    while new_r != 0:
        quotient = math.floor(r / new_r)
        # temp_d = d
        # temp_n_d = new_d
        # temp_r = r
        # temp_n_r = new_r
        (d, new_d) = (new_d, d - quotient * new_d)
        (r, new_r) = (new_r, r - quotient * new_r)
        print(new_r)

    if (r > 1):
        return "e not invertible"
    if (d < 0):
        d = d + n

    return d

d = extended_euclid(e, phi)

print(d)

m = 116683724595995812415204464800220046341847098708219974939871659063834910712369644695807211401823863407765494139162777372661207968602781295442240230046184096272458683361364027901361097924496220894827290343024413733260672139113765662110977531659380880716669505166695417691640702760225045741088003161711582312912

encrypt = mod_exp(m, e, n)
print("encrypt: ", encrypt)

k = 119346834962971636870341682219569368324396153456702106519669893696711847227603621791290911592241761305941133264962940829581442517222092941631635081611281860159486239020012071566088932989287938933614380850476199462094260964822793622599424036135714419162688662404188856320434907489999719968549846074275574183085
decrypt = mod_exp(k, d, n)
print("decryp: ", decrypt)