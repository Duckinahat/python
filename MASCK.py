# Mono Alphabetic Substitution Cipher using Keywords (MASCK)
# V 1.2
# by Nicola Leonardi
# written for Python 3

#definitions
def main():
        print('Create or decode monoalphabetic substitution ciphers with a keyword. \nSelect mode:')
        mode = input('Decipher, Encipher or Custom decipher? ')
        if mode != '' :
                mode = mode[0]
        if mode in 'dD1':
                temp = Dinp()
                ct = temp[0]
                key = temp[1]
                pt = decipher(ct,key)
                print('Plaintext: ' + pt)

        elif mode in 'eE2':
                temp = Einp()
                pt = temp[0]
                key = temp[1]
                ct = encipher(pt,key)
                print('Ciphertext: ' + ct)

        elif mode in 'cC3':
                print('\n' * 40)
                print('Enter a ciphertext, then give a capital letter and a lowercase letter to replace it with.  Attempts can be reversed by switching the order.  Enter yes when finished.')
                ct = Cinp()
                codebreak(ct)

        else:
                print('Invalid input')
                main()

def Dinp():
        ct = input('enter ciphertext here: ')
        CT = ct.upper()
        key = input('enter keyword here: ')
        KEY = key.upper()
        return(CT,KEY)

def Einp():
        pt = input('enter plaintext here: ')
        PT = pt.upper()
        key = input('enter keyword here: ')
        KEY = key.upper()
        return(PT,KEY)

def Cinp():
        ct = input('enter ciphertext here: ')
        CT = ct.upper()
        return(CT)

def decipher(ct,key):
        alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        keyp = ''
        for c in key:
                if c not in keyp:
                        keyp = keyp + key[key.find(c)]
        calpha = ''
        ralpha = alpha
        for c in keyp:
                calpha = calpha + c 
                cind = ralpha.find(c)
                ralpha = ralpha.replace(c,'')
                ralpha = (ralpha[cind:] + ralpha[:cind])
        calpha = calpha + ralpha	
        cipher = str.maketrans(calpha, alpha)
        PT = ct.translate(cipher)
        pt = PT.lower()
        return(pt)

def encipher(pt,key):
        alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        keyp = ''
        for c in key:
                if c not in keyp:
                        keyp = keyp + key[key.find(c)]
        calpha = ''
        ralpha = alpha
        for c in keyp:
                calpha = calpha + c 
                cind = ralpha.find(c)
                ralpha = ralpha.replace(c,'')
                ralpha = (ralpha[cind:] + ralpha[:cind])
        calpha = calpha + ralpha	
        cipher = str.maketrans(alpha, calpha)
        CT = pt.translate(cipher)
        ct = CT.lower()
        return(ct)

def codebreak(ct):
        print(ct + '\n')
        alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        calpha = alpha
        switch = ''
        while switch != 'yes':
                print(alpha)
                print(calpha)
                print()
                switch = input()
                if switch != '':
                        calpha = calpha.replace(switch[0],switch[-1])
                cipher = str.maketrans(alpha, calpha)
                pt = ct.translate(cipher)
                print('\n' + pt + '\n')
                
        return(pt)

#run program
main()
