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
<hr>

### rand()

Η συνάρτηση `rand ()` χρησιμοποιείται για τη δημιουργία ενός τυχαίου αριθμού και επιστρέφει μια ακέραια τιμή που το εύρος της είναι από 0 έως 32767.

### srand (seed)

Η συνάρτηση `srand (seed)` χρησιμοποιείται για την αρχικοποίηση του παραγόμενου τυχαίου αριθμού με τη συνάρτηση rand (). Δεν επιστρέφει τίποτα.

### seed

Το `seed` από την άλλη είναι ένας αριθμός ή άλλη τιμή που δημιουργείται από λογισμικό χρησιμοποιώντας μία ή περισσότερες τιμές. Για παράδειγμα, η ώρα ή η ημερομηνία που έχουμε στην άσκηση είναι ένα παράδειγμα τιμών που βοηθούν στη δημιουργία μιας τυχαίας τιμής που χρησιμοποιείται από το ransomware.
<hr>

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

Πρώτα απο όλα πρέπει να βρούμε το “σωστό” [seed](https://github.com/p19tzam/crypto-2/blob/main/crypto-2/README.md#seed) δηλαδή πρέπει να βρούμε το epoch(την ημερομηνία και την ώρα που δημιούργησε το key το ransomware) και να το κάνουμε convert σε unix time.

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

Το σωστό [seed](https://github.com/p19tzam/crypto-2/blob/main/crypto-2/README.md#seed) είναι: `1606212503` δηλαδή είναι ο αριθμός που θα βάλουμε στην [srand()](https://github.com/p19tzam/crypto-2/blob/main/crypto-2/README.md#srand-seed) για να κάνουμε αρχικοποίηση την στιγμή που έγινε generate το key απο το ransomware.

<br>
<br>

### Ας ξεκινήσουμε με τον κώδικα <br>
Πρώτα απο όλα ο καθηγητής μας δίνει δύο πολύ σημαντικές πληροφορίες στην εκφώνηση.<br>
Το IV και τα magicbytes του PDF αρχείου σε hex πριν κρυπτογραφηθεί.<br><br>

IV                 = `61f6ef5c567fbcfb99961becdd0954e0` (16 bytes) <br>
Magic Bytes = `255044462d312e370a25e2e3cfd30a34` (16 bytes)
<br>

<b><u>p.s Αν η εξήγηση είναι απλή την γράφω σε python comments</u></b>

```python 
srand(1606212503) #Αρχικοποίηση την στιγμή που έγινε generate το key απο το ransomware
iv=bytes.fromhex('61f6ef5c567fbcfb99961becdd0954e0') #Αρχικοποίηση και μετατροπή του IV απο hex σε bytes 
magicb=b'255044462d312e370a25e2e3cfd30a34' #Αρχικοποίηση τα magic bytes σε μια μεταβλητή τύπου bytes
KEYSIZE=16 #Αρχικοποίηση το μήκος του key σε μια global μεταβλητή
```
<br>

```python
with open('important.enc.pdf','rb') as encrypted_pdf_file: #Ανοίγω το encrypted pdf αρχείο για ανάγνωση μόνο σε binary format.
	ciphertext=encrypted_pdf_file.read() #Διαβάζω τα binary περιεχόμενα του encrypted pdf αρχείου.
```

<br>


Όπως βλέπουμε στο παρακάτω κομμάτι κώδικα έχουμε ενα for loop που ξεκινάει απο τον αριθμό `1606212503` δηλαδή ξεκινάει απο το [seed](https://github.com/p19tzam/crypto-2/blob/main/crypto-2/README.md#seed) που αρχικοποιώ παραπάνω και σε κάθε loop το [seed](https://github.com/p19tzam/crypto-2/blob/main/crypto-2/README.md#seed) μας ανεβαίνει +1 κάθε φορά. Στην ουσία όταν αλλάζει το [seed](https://github.com/p19tzam/crypto-2/blob/main/crypto-2/README.md#seed) ταυτόχρονα είναι σαν να αλλάζει η ώρα αλλα σε μορφή epoch.
Και τέλος αυτού του κομματιού κανουμε νεα αρχικοποίηση κάθε φορα για την νεα στιγμή που έγινε generate το key απο το ransomware.<br>

Για να υλοποιήσω το start του for απο τον αριθμό του [seed](https://github.com/p19tzam/crypto-2/blob/main/crypto-2/README.md#seed) που θέλω χρισημοποίησα το itertools module και το .count() function.<br>

```python
import itertools

srand(1606212503)

for i in itertools.count(start=1606212503)
	srand(i)
```

<br>


Λοιπόν τώρα πρέπει να κάνουμε “grab” τα 16 πρώτα bytes απο τα magic bytes του κάθε key που θα δοκιμαστεί και να τα συγκρίνω με τα magic bytes που μας δόθηκε. <br>
Προτού γίνει αυτό πρώτα πρέπει να καλέσουμε την `generate_random_key(KEYSIZE)` για να γίνει το key generate. <br>
<br>
Δημιουργούμε την μεταβλητή `cipher` και καλούμε την συνάρτηση `.new()` που παίρνει ως ορίσματα το key(στην περίπτωση μας κάνουμε brute force attack), το mode του AES και το IV που μας έχει δοθεί. <br>

Επίσης θα χρειαστούμε την μεταβλητή `plaintext` που καλούμε την συνάρτηση `.decrypt()`
Που παιρνει ως όρισμα ciphertext που είναι το αρχείο που ανοίξαμε να διαβάσουμε έξω απο την loop για binary format read και το κανει decrypt.

```python
from Crypto.Cipher import AES

	tempkey=generate_random_key(KEYSIZE)

	cipher=AES.new(tempkey,AES.MODE_CBC,iv)

	plaintext=cipher.decrypt(ciphertext)
```

<br>

Λοιπόν πάμε στο τέλος του προγράμματος και στο κομμάτι που ελέγχουμε τα 16 πρώτα bytes απο το `plaintext` και βλέπουμε αν είναι ίδια με τα δικά μας magicbytes.<br>

If: αν τα πρώτα bytes(32 hexdata) απο το plaintext είναι ίσα με τα δικα μας magic bytes τότε εμφανίζεται το key και ανοίγει/δημιουργεί το αρχείο με όνομα `important.pdf` για write σε binary format. Και τέλος κάνει ενα break για να σταματησει η επίθεση brute force. <br>

<pre>
type(plaintext)=bytes πρέπει να το κάνουμε μετατροπή σε hex(γιατί τα magic bytes που μας δόθηκαν ειναι σε hex)
type(plaintext.hex())=hex μετατροπή σε hex απο bytes
type(plaintext.hex().encode())=b’hexdata’ μετατροπή απο hex σε bytes για να ολοκληρώσουμε την συνθήκη.
[0:32] = παίρνουμε τα πρώτα 32 hex data απο την plaintext μεταβλητή.
</pre>

```python
if plaintext.hex()[0:32].encode()==magicb: 
		os.system("clear")
		print("\n\n[!]=> Found key for decryption(bytes): ",tempkey)
		with open('important.pdf','wb') as decrypted_pdf_file:
			decrypted_pdf_file.write(plaintext)
		break

```
key for decryption <br>
FLAG{`b'-\xbe\xf8\x07G\xd6\xf1\xce~\x18%\xed\xc7j\xee\x9d'`}

[Source Code](https://github.com/p19tzam/crypto-2/blob/main/crypto-2/decrypt.py)
