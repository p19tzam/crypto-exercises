### Crypto excercise 2 <br>

# Functions

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

<br><br>
### rand()

Η συνάρτηση `rand ()` χρησιμοποιείται για τη δημιουργία ενός τυχαίου αριθμού και επιστρέφει μια ακέραια τιμή που το εύρος της είναι από 0 έως 32767.

### srand (seed)

Η συνάρτηση `srand (seed)` χρησιμοποιείται για την αρχικοποίηση του παραγόμενου τυχαίου αριθμού με τη συνάρτηση rand (). Δεν επιστρέφει τίποτα.

### seed

Το `seed` από την άλλη είναι ένας αριθμός ή άλλη τιμή που δημιουργείται από λογισμικό χρησιμοποιώντας μία ή περισσότερες τιμές. Για παράδειγμα, η ώρα ή η ημερομηνία που έχουμε στην άσκηση είναι ένα παράδειγμα τιμών που βοηθούν στη δημιουργία μιας τυχαίας τιμής που χρησιμοποιείται από το ransomware.


<br>
<br>

Η `generate_random_key(KEYSIZE)` παιρνει ως όρισμα το KEYSIZE δηλαδή το μήκος του key που θέλουμε να κάνουμε generate και φτιάχνει ενα key KEYSIZE bytes. 

```python
def generate_random_key(KEYSIZE): 
	key = b' '
	for i in range(KEYSIZE):
 		key += bytes([rand()%256])
	return key
```


<br>
Αμέσως μετά ορίζω την μεταβλητή  ` key = b' ' ` δηλαδή μια κενή μεταβλητή που έχει type() bytes που στην πορεία θα γίνει generate το key και θα προστεθεί μέσα σε αυτή την μεταβλητή.

```python
key = b' '
```


<br>

Μετά απο τον ορισμό της μεταβλητής key έχουμε την for loop που loopαρει για KEYSIZE φορές(δηλαδή όσο είναι το KEYSIZE τόσα bytes θα είναι το key μας) Στην δικια μας περίπτωση  θα loopαρει για 16 φορές και το generated key μας θα είναι 16bytes.

Με το που μπει το script μας μέσα στην for θα κάνει κάθε 1 byte που κάνει generate απο την <b>rand()%256</b>(όπως στο C script) πρόσθεση στα ήδη καταχωρημένα bytes που είτε είχε κάνει generate είτε η μεταβλητη key είναι κενή.

Αυτό γίνεται για KEYSIZE φορές δηλαδή κάθε φορά κάνει generate 1byte τα προσθέτει με τα ήδη καταχωρημένα bytes και στο exit της loop κάνουμε `return` το key μας για να χρησιμοποιηθεί στο πρόγραμμα μας.


επίσης με την function `bytes()` επιστρέφουμε bytes που είναι αμετάβλητα δηλαδή δεν μπορούν να τροποποιηθούν. *Αν δεν είχαμε την `bytes()` ο τυχαίος αριθμός που θα γινόταν generate απο την `rand()` δεν θα μπορούσε να προστεθεί στην μεταβλητή γιατί η μεταβλητή είναι type bytes και ο αριθμός είναι int.



```python
for i in range(KEYSIZE):
	key += bytes([rand()%256])
return key
```


<br>
<br>

# Main program

Προτού ξεκινήσουμε με την αποκρυπτογράφηση του pdf αρχείου πρώτα θα εξηγήσω το σκεπτικό και τα βήματα που ακολούθησα για να κάνω την αποκρυπτογράφηση.

<br>

Πρώτα απο όλα πρέπει να βρούμε το “σωστό” [seed](https://github.com/p19tzam/crypto-2/blob/main/README.md#seed) δηλαδή πρέπει να βρούμε το epoch(την ημερομηνία και την ώρα που δημιούργησε το key το ransomware) και να το κάνουμε convert σε unix time.

<br>

Ο καθηγητής μας δίνει σε μια εικονα στην εκφώνηση date time seconds που είναι:
`Tue, Nov 24 2020 17:08:23` <br>
Και μας λέει ότι ο χρόνος epoch είναι για UTC(2 ώρες πίσω διαφορά με την ώρα στην αθήνα).
Επομένως το σωστό date time seconds είναι: `Tue, Nov 24 2020 10:08:23` <br>
Εξήγηση
<pre>
        17:00 - 2 ώρες το UTC = 15:00
        15:00 - 5 ώρες κρυπτογράφηση = 10:00
</pre>
Αρα η ώρα που το key δημιουργήθηκε είναι `10:08:23`. <br>

Τώρα θα πρέπει να μετατρέψουμε αυτο το date: `Tue, Nov 24 2020 17:08:23` σε epoch. <br>
Αυτό μπορούμε να το κάνουμε είτε με script είτε online. <br>

Το σωστό [seed](https://github.com/p19tzam/crypto-2/blob/main/README.md#seed) είναι: `1606212503` δηλαδή είναι ο αριθμός που θα βάλουμε στην [srand()](https://github.com/p19tzam/crypto-2/blob/main/README.md#srand-seed) για να κάνουμε αρχικοποίηση την στιγμή που έγινε generate το key απο το ransomware.

