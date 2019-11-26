""" Le jeu : un tableau de 4 colonnes et len(L)//4 lignes possède len(L) boutons éteints. Le but du jeu est d'allumer tous les boutons sachant que les voisins du bouton appuyé et le bouton appuyé s'allument lorsque le bouton appuyé est appuyé. 
La réponse du jeu ; cliquer sur tous les boutons sur l'exterieur du tableau (pour un 3 lignes 4 colonnes)""" 

nombre_de_cases = 20   #ATTENTION nombre de cases possible : 8,12,16,20

import tkinter as tk

app = tk.Tk()
app.title("jeu des cases")
app.minsize(1270,800)
app.resizable(width=True, height=True)
app.geometry("800x645+0+0")
app.configure(bg = "light blue")
Frame = tk.Frame(app, bg='light blue')


Bouton_quit = tk.Button(app, text="C'EST GAGNE !!!", width=15,height=1, bg="red",font="GROBOLD.ttf 30", relief=tk.RAISED, cursor = 'hand2', command=app.destroy)
L = [i for i in range(nombre_de_cases)] 

x_gagné,y_gagné=800,500

coord_y='échelle'

if nombre_de_cases == 20:
    coord_y=10
    
elif nombre_de_cases == 16:
    coord_y=75
    
elif nombre_de_cases == 12:
    coord_y=125

elif nombre_de_cases == 8:
    coord_y=175

elif nombre_de_cases == 4:
    coord_y=180
    

else:
    print('dimensions erreur')
    app.destroy


nb=0
        
class GameButton(tk.Button):
    global B_recommencer
    
    def __init__(self, id):
        tk.Button.__init__(self, Frame)
        self.config(text=str(id), width=8, height=3, bg="white",font="GROBOLD.ttf 16",      
            relief=tk.RAISED, cursor = 'hand2', command=self.lancement)
        
        self.id = id
        self.state = 'eteint'
        
    def recommencer():
        global nb, M
        print(' ')
        print('nombre de coups:',nb)
        print('#################recommencer##################')
        print('')
        nb=0
        for i in Liste_boutons:
            i.configure(bg='white')
            i.state = 'eteint'
            M[Liste_boutons.index(i)]=0
        

    def changer(self,event):
        global Bouton_quit
        if Bouton_quit['bg']=='red':
            Bouton_quit.configure(bg='pink')
        elif Bouton_quit['bg']=='pink':
            Bouton_quit.configure(bg='red')
    
    
    def test(self,L):
        global nb, Bouton_quit
        if L==[1]*len(L):
            print('########gagné########')
            Bouton_quit.place(x=x_gagné, y=y_gagné)
            Bouton_quit.bind("<Enter>", self.changer)
            Bouton_quit.bind("<Leave>", self.changer)
            print('')
            print('nombre de coups:',nb)
            tk.Label(app, text='Nombre de coups : {}'.format(nb), fg='red', font='Arial 20 bold', bg='light blue').place(x=800,y=400)
            
        
    def lancement(self):
        global nb
        
        print('Cliqué {}'.format(self.id))
        nb += 1
        
        indice_temp = Liste_boutons.index(self)
        
        for i in range(len(L)//4):
            try :
                emplacement = Liste_boutons_prime[i].index(self)
                indice=i
            except:
                pass
        
            # on a donc self = Liste_boutons_prime[indice][emplacement]
            
        if self.state == 'eteint':
            self.config(bg='blue')
            self.state = 'allume'
            M[indice_temp]=1
        else:
            self.config(bg='white')
            self.state = 'eteint'
            M[indice_temp]=0
        
        if (indice_temp+1) in L:
            if Liste_boutons[indice_temp+1] in Liste_boutons_prime[indice]:
                if Liste_boutons[indice_temp+1].state == 'eteint':
                    Liste_boutons[indice_temp+1].config(bg='blue')
                    Liste_boutons[indice_temp+1].state = 'allume'
                    M[indice_temp+1]=1
                else:
                    Liste_boutons[indice_temp+1].config(bg='white')
                    Liste_boutons[indice_temp+1].state = 'eteint'
                    M[indice_temp+1]=0
                    
        if (indice_temp) in L:
            if Liste_boutons[indice_temp-1] in Liste_boutons_prime[indice]:
                if Liste_boutons[indice_temp-1].state == 'eteint':
                    Liste_boutons[indice_temp-1].config(bg='blue')
                    Liste_boutons[indice_temp-1].state = 'allume'
                    M[indice_temp-1]=1
                else:
                    Liste_boutons[indice_temp-1].config(bg='white')
                    Liste_boutons[indice_temp-1].state = 'eteint'
                    M[indice_temp-1]=0
        
        if indice_temp-4 in L:
            if Liste_boutons[indice_temp-4].state == 'eteint':
                Liste_boutons[indice_temp-4].config(bg='blue')
                Liste_boutons[indice_temp-4].state = 'allume'
                M[indice_temp-4]=1
            else:
                Liste_boutons[indice_temp-4].config(bg='white')
                Liste_boutons[indice_temp-4].state = 'eteint'
                M[indice_temp-4]=0
                
        if indice_temp+4 in L:
            if Liste_boutons[indice_temp+4].state == 'eteint':
                Liste_boutons[indice_temp+4].config(bg='blue')
                Liste_boutons[indice_temp+4].state = 'allume'
                M[indice_temp+4]=1
            else:
                Liste_boutons[indice_temp+4].config(bg='white')
                Liste_boutons[indice_temp+4].state = 'eteint'
                M[indice_temp+4]=0
        
        self.test(M)
        
    
    B_recommencer = tk.Button(app, text="recommencer", width=10,height=1, bg="light green",font="Arial 12 bold", relief=tk.RAISED, cursor = 'hand2', command=recommencer)
            

    
## Création des listes

    
# création de Lprime:
Lprime = [[]]*(len(L)//4)
for j in range(1,(len(L)//4)+1):
    for i in range(len(L)+1):
        if i>4*(j-1) and i<=4*j:
            Lprime[j-1] = Lprime[j-1] + [i]


# création de M
M = [0]*len(L)


#création de Liste_boutons
Liste_boutons = []
for i in L:
    button = GameButton(i+1)
    Liste_boutons.append(button)


#création de Liste_boutons_primek
Liste_boutons_prime = [[]]*(len(Lprime))
for j in range(1,len(Lprime)+1):
    for i in range(1,len(L)+1):
        if i>4*(j-1) and i<=4*j:
            Liste_boutons_prime[j-1] = Liste_boutons_prime[j-1] + [Liste_boutons[i-1]]


but = tk.Label(app, text="BUT DU JEU:", fg='blue', font='Arial 20 bold', bg='light blue')
regle = tk.Label(app, text="Allumer tous les boutons en cliquant dessus", fg='black', font='Arial 15 bold', bg='light blue')


## affichage


#affichage de la grille
for i in range(len(Lprime)):
    for j in range(len(L)//len(Lprime)):
        Liste_boutons_prime[i][j].grid(row=i,column=j, padx=20, pady=20)
        
B_recommencer.place(x=1150,y=10)

but.place(x=800,y=200)
regle.place(x=800,y=300)

    
Frame.place(x=100,y=coord_y)
app.mainloop()
