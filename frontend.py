import backend as ba

from datetime import date
from datetime import datetime

def Greeting():
    print('Witaj w kalkulatorze!')
    print('Kalkulator nie zachowuje kolejności wykonywania działań!')
    print('Tzn. jesli podasz 3+4*5, to kalkulator w wyniku da 40, a nie 23!')


def podaj_wartosc():
    Greeting()
    now = datetime.now()
    dt_string = now.strftime("%H-%M-%S")
    wynik=0
    a=input('Podaj pierwszy argument:')
    wynik=int(a)
    historia=a
    while(True):
        wartosc=input('Podaj znak operacji:')
        if wartosc=='+':
            historia+=wartosc
            arg=input('Podaj liczbe:')
            arg=float(arg)
            wynik=ba.suma(wynik,arg)
            historia+=str(arg)
        elif wartosc == '-':
            arg=input('Podaj liczbę:')
            historia+=wartosc
            arg=int(arg)
            wynik=ba.roznica(wynik,arg)
            historia+=str(arg)
        elif wartosc == '*':
            arg=input('Podaj liczbę:')
            arg=float(arg)
            wynik=ba.mnozenie(wynik,arg)
            historia+=str(arg)
        elif wartosc=='/':
            arg=input('Podaj liczbę:')
            arg=float(arg)
            historia+=wartosc
            historia+=str(arg)
            if(arg==0):
                #Zero
                print('Nie dziel przez 0')
                wynik='Niedozwolone dzielenie przez 0!'
            wynik=ba.dzielenie(wynik,arg)
        elif wartosc=="=":
            scierzka='WW'
            break
        else:
            print('Niedozwolony argument!')
            wynik='Uzytkownik podał niewłaściwy argument'
            scierzka='WW'
    scierzka+='_'+str(date.today())+'_'+dt_string+'.txt'

    with open(scierzka,'a') as file:
        file.write(historia+'='+str(wynik)+'\n')


            
            
                    


    