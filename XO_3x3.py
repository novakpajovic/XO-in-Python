from math import inf as infinity
import platform
import time
from os import system


class XO:
    igrac1 = -1
    igrac2 = +1
    tabla = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]
    mode = -1
    igrac1name = "Igrac 1"
    igrac2name = "Racunar"

    def __init__(self,mode): 
        self.mode = mode  
        if mode == 2:
            self.igrac2name = "Igrac 2" 

    def zapocniIgru(self):
        i1_izbor = 'X'  
        i2_izbor = 'O'  

        clean()
        print("----- {}(X) i {}(O) igraju! -----\n\n3".format(self.igrac1name,self.igrac2name))
        time.sleep(1)
        clean()

        print("----- {}(X) i {}(O) igraju! -----\n\n2".format(self.igrac1name,self.igrac2name))
        time.sleep(1)
        clean()

        print("----- {}(X) i {}(O) igraju! -----\n\n1".format(self.igrac1name,self.igrac2name))
        time.sleep(1)
        clean()

        
        while len(self.slobodne_celije()) > 0 and not self.kraj_igre():
            self.igrac1_naPotezu(i2_izbor, i1_izbor)
            if self.mode == 1:
                self.racunar_naPotezu(i2_izbor, i1_izbor)
            else:
                self.igrac2_naPotezu(i2_izbor, i1_izbor)    

        if self.pobeda(self.igrac1):
            clean()
            self.tabela(i2_izbor, i1_izbor)
            print(self.igrac1name+' JE POBEDIO!')
        elif self.pobeda(self.igrac2):
            clean()
            print(f'{self.igrac2name} turn [{i2_izbor}]')
            self.tabela(i2_izbor, i1_izbor)
            print(self.igrac2name+' JE POBEDIO!')
        else:
            clean()
            self.tabela(i2_izbor, i1_izbor)
            print('NERESENO!')

    def procena(self):


        if self.pobeda(self.igrac2):
            rezultat = +1
        elif self.pobeda(self.igrac1):
            rezultat = -1
        else:
            rezultat = 0

        return rezultat

    def pobeda(self, igrac):

        stanje = self.tabla

        stanja_pobede = [
            [stanje[0][0], stanje[0][1], stanje[0][2]],
            [stanje[1][0], stanje[1][1], stanje[1][2]],
            [stanje[2][0], stanje[2][1], stanje[2][2]],
            [stanje[0][0], stanje[1][0], stanje[2][0]],
            [stanje[0][1], stanje[1][1], stanje[2][1]],
            [stanje[0][2], stanje[1][2], stanje[2][2]],
            [stanje[0][0], stanje[1][1], stanje[2][2]],
            [stanje[2][0], stanje[1][1], stanje[0][2]],
        ]
        if [igrac, igrac, igrac] in stanja_pobede:
            return True
        else:
            return False

    def kraj_igre(self):
        
        
        return self.pobeda(self.igrac1) or self.pobeda(self.igrac2)

    def slobodne_celije(self):
        
        
        stanje = self.tabla

        cells = []

        for x, red in enumerate(stanje):
            for y, cell in enumerate(red):
                if cell == 0:
                    cells.append([x, y])

        return cells

    def odgovarajuci_potez(self, x, y):
        
        
        if [x, y] in self.slobodne_celije():
            return True
        else:
            return False

    def postavi_znak(self,x, y, igrac):
        
        
        if self.odgovarajuci_potez(x, y):
            self.tabla[x][y] = igrac
            return True
        else:
            return False

    def minimax(self, dubina, igrac):
        

        stanje = self.tabla

        if igrac == self.igrac2:
            best = [-1, -1, -infinity]
        else:
            best = [-1, -1, +infinity]

        if dubina == 0 or self.kraj_igre():
            rezultat = self.procena()
            return [-1, -1, rezultat]

        for cell in self.slobodne_celije():
            x, y = cell[0], cell[1]
            stanje[x][y] = igrac
            rezultat = self.minimax(dubina - 1, -igrac)
            stanje[x][y] = 0
            rezultat[0], rezultat[1] = x, y

            if igrac == self.igrac2:
                if rezultat[2] > best[2]:
                    best = rezultat  
            else:
                if rezultat[2] < best[2]:
                    best = rezultat  

        return best

    def tabela(self, i2_izbor, i1_izbor):        

        stanje = self.tabla

        chars = {
            -1: i1_izbor,
            +1: i2_izbor,
            0: ' '
        }
        hor_linija = '---------------'

        print('\n' + hor_linija)
        for red in stanje:
            for cell in red:
                symbol = chars[cell]
                print(f'| {symbol} |', end='')
            print('\n' + hor_linija)

    def racunar_naPotezu(self,i2_izbor, i1_izbor):
        
        
        dubina = len(self.slobodne_celije())
        if dubina == 0 or self.kraj_igre():
            return

        clean()
        print(f'{self.igrac2name} je na potezu [{i2_izbor}]')
        self.tabela(i2_izbor, i1_izbor)

        if dubina == 9:
            x = izbor([0, 1, 2])
            y = izbor([0, 1, 2])
        else:
            potez = self.minimax(dubina, self.igrac2)
            x, y = potez[0], potez[1]

        self.postavi_znak(x, y, self.igrac2)
        time.sleep(1)

    def igrac1_naPotezu(self,i2_izbor, i1_izbor):
        
        
        dubina = len(self.slobodne_celije())
        if dubina == 0 or self.kraj_igre():
            return

        potez = -1
        potezi = {
            1: [0, 0], 2: [0, 1], 3: [0, 2],
            4: [1, 0], 5: [1, 1], 6: [1, 2],
            7: [2, 0], 8: [2, 1], 9: [2, 2],
        }

        clean()
        print(f'{self.igrac1name} je na potezu [{i1_izbor}]')
        self.tabela(i2_izbor, i1_izbor)

        while potez < 1 or potez > 9:
            try:
                potez = int(input('Koristiti tastaturu za unos (1..9): '))
                koord = potezi[potez]
                can_potez = self.postavi_znak(koord[0], koord[1], self.igrac1)

                if not can_potez:
                    print('Polje je zauzeto')
                    potez = -1
            except (EOFError, KeytablaInterrupt):
                print('Greska!')
                exit()
            except (KeyError, ValueError):
                print('Pogresan unos brojeva')

    def igrac2_naPotezu(self,i2_izbor, i1_izbor):

        dubina = len(self.slobodne_celije())
        if dubina == 0 or self.kraj_igre():
            return

        potez = -1
        potezi = {
            1: [0, 0], 2: [0, 1], 3: [0, 2],
            4: [1, 0], 5: [1, 1], 6: [1, 2],
            7: [2, 0], 8: [2, 1], 9: [2, 2],
        }

        clean()
        print(f'{self.igrac2name} je na potezu [{i2_izbor}]')
        self.tabela(i2_izbor, i1_izbor)

        while potez < 1 or potez > 9:
            try:
                potez = int(input('Koristiti tastaturu za unos (1..9): '))
                koord = potezi[potez]
                can_potez = self.postavi_znak(koord[0], koord[1], self.igrac2)

                if not can_potez:
                    print('Polje je zauzeto')
                    potez = -1
            except (EOFError, KeytablaInterrupt):
                print('Greska!')
                exit()
            except (KeyError, ValueError):
                print('Pogresan unos brojeva')



def clean():
    os_name = platform.system().lower()
    if 'windows' in os_name:
        system('cls')
    else:
        system('clear')


def main():
    
    while True:
        mode = input("Da li zelite da igrate protiv racunara ili drugog igraca?\n(Pritisnite 1 da igrate protiv racunara ili 2 protiv drugog igraca) : ")
        if mode == "1" or mode == "2":
            mode = int(mode)
            break

    game = XO(mode)
    game.zapocniIgru()

    exit()


if __name__ == '__main__':
    main()
