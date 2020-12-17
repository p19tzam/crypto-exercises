
# Crypto excercise 2


Η ```python 
srand()
``` και η `rand()` είναι python implementations της `srand()` και `rand()` απο την C.
Διαφορετικά αυτό το πράγμα δεν μπορεί να δουλέψει γιατί δεν χρησιμοποιούν τις ίδιες random η C με την python. Επομένως οτι seed να βάλουμε στην python στην αντίστοιχη random δεν θα δουλέψει.



```python
from ctypes import c_int, c_uint

def srand(seed):
    srand.r = [0 for _ in range(34)]
    srand.r[0] = c_int(seed).value
    for i in range(1, 31):
        srand.r[i] = (16807 * srand.r[i - 1]) % 2147483647
    for i in range(31, 34):
        srand.r[i] = srand.r[i - 31]
    srand.k = 0
    for _ in range(34, 344):
        rand()


def rand():
    srand.r[srand.k] = srand.r[(srand.k - 31) % 34] + srand.r[(srand.k - 3) % 34]
    r = c_uint(srand.r[srand.k]).value >> 1
    srand.k = (srand.k + 1) % 34
    return r
```

dsadsaasdsadsd

```python
def generate_random_key(KEYSIZE): 
	key = b''
	for i in range(KEYSIZE):
 		key += bytes([rand()%256])
	return key
```
