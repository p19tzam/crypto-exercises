# Crypto excercise 2


Η `srand(seed)` και η `rand()` είναι python implementations της `srand()` και `rand()` απο την C.
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

Η `generate_random_key(KEYSIZE)` παιρνει ως όρισμα το KEYSIZE δηλαδή το μήκος του key που θέλουμε να κάνουμε generate και φτιάχνει ενα key KEYSIZE bytes. 

```python
def generate_random_key(KEYSIZE): 
	key = b' '
	for i in range(KEYSIZE):
 		key += bytes([rand()%256])
	return key
```


<br>
Αμέσως μετά ορίζω την μεταβλητή `key = b' '` δηλαδή μια κενή μεταβλητή που έχει type() bytes που στην πορεία θα γίνει generate το key και θα προστεθεί μέσα σε αυτή την μεταβλητή.

```python
key += bytes([rand()%256])
```


<br>

Μετά απο τον ορισμό της μεταβλητής key έχουμε την for loop που loopαρει για KEYSIZE φορές(δηλαδή όσο είναι το KEYSIZE τόσα bytes θα είναι το key μας) Στην δικια μας περίπτωση  θα loopαρει για 16 φορές και το generated key μας θα είναι 16bytes.


