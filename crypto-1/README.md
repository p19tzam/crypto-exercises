### Crypto excercise 1 <br>

# Functions

Η `menuChoiceCheck(choice)` παίρνει ως όρισμα την μεταβλητή choice και ελέγχει αν η τιμή της μεταβλητής δεν είναι 0,1 η 2 και αν είναι θα μπεί μέσα στην loopa και θα ξανα ζητήσει input απο τον χρήστη.

```python
def menuChoiceCheck(choice):
    while(choice!="0" and choice!="1" and choice!="2"):
        print "Select right cipher..!\n"
        choice=raw_input("Choice:>> ")
    return choice
```


```python
def menu():
    print "\nPlease select cipher \n0:Affine\n1:Vigerene\n2:Substitution"
```

<br>

# Main program


