### Crypto excercise 1 <br>

# Functions

Η `menuChoiceCheck(choice)` παίρνει ως όρισμα την μεταβλητή choice και ελέγχει αν η τιμή της μεταβλητής δεν είναι 0,1 η 2 και αν δεν είναι θα μπεί μέσα στην loopa και θα ξανα ζητήσει input απο τον χρήστη.

```python
def menuChoiceCheck(choice):
    while(choice!="0" and choice!="1" and choice!="2"):
        print "Select right cipher..!\n"
        choice=raw_input("Choice:>> ")
    return choice
```

Η `menu()` εμφανίζει απλά ενα μήνυμα με το menu όταν γίνεται κλήση της συνάρτησης για να επιλεξει ο χρήστης τον αλγόριθμο που θέλει να κάνει encrypt και decrypt . 

```python
def menu():
    print "\nPlease select cipher \n0:Affine\n1:Vigerene\n2:Substitution"
```

<br>

<hr>

### affineCipher.py

```python
from affineCipher import * # Στο main πρόγραμμα.

def encryptAFF(myKey, myMessage): # Κάνει encrypt με ορίσματα το μήνυμα και το key που έχει γίνει generate.
    translated = encryptMessage(myKey, myMessage)
    return translated

def decryptAFF(myMessage, myKey): # Κάνει decrypt με ορίσματα το μήνυμα και το key που έχει γίνει generate.
    translated = decryptMessage(myKey, myMessage)
    return translated

def getRandomKeyaAFF(): # Κάνει generate ενα random key για τον affine
    while True:
        keyA = random.randint(2, len(SYMBOLS))
        keyB = random.randint(2, len(SYMBOLS))
        if gcd(keyA, len(SYMBOLS)) == 1:
            return keyA * len(SYMBOLS) + keyB

```

<hr>






# Main program

```python
os.system("clear") # Καθαρίζει το terminal όταν ξεκινάει το πρόγραμμα.
menu() # Κλήση συνάρτησης menu() για να εμφανίσει το menu για επιλογή.
choice=raw_input("Choice:>> ") # Ζητάει απο τον χρήστη το input σε string
choice=menuChoiceCheck(choice) # και εδώ γίνεται κλήση της συνάρτησης menuChoiceCheck(choice)
os.system("clear") # και ξανα καθαρίζει το terminal
``` 

<br>

Μετά απο όλα αυτά ξεκινάω μια if,elif,else που η κάθε μια αντικατοπτρίζει τις επιλογές του χρήστη πχ αν το `choice==”0”` τοτε έχουμε τον affine για encrypt και decrypt αν `choice==”1”` τοτε έχουμε τον vigerene για encrypt και decrypt και στο `else` έχουμε τον substitution επίσης για encrypt και decrypt..  <br>

Έχουμε και τις εξής πληροφορίες.. <br>
Οτι ο `affine` και ο `substitution` έχουν δυναμικο κλειδι δηλαδή κάθε φορά που χρησιμοποιούμε το πρόγραμμα θα γίνει generate ενα random key απο τις συναρτήσεις που έχουμε στους encrypt και decrypt αλγορίθμους που μας έδωσε ο καθηγητής ενώ ο `vigerene` έχει στατικό κλειδί.



