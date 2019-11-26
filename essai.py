"""trouve les solutions du jeu des cases en fonction du nombre des cases (attendre 30 secondes pour 20 cases)"""


L = [i for i in range(1,16 + 1)] #L doit etre un multiple de 4 Puis imaginer une matrice à 4 colonnes

Lprime = [[]]*(len(L)//4)

for j in range(1,(len(L)//4)+1):
    for i in L:
        if i>4*(j-1) and i<=4*j:
            Lprime[j-1] = Lprime[j-1] + [i]

M = [0]*len(L)

M_stocké=M

ligne_de_appuyé=[]

def essayer(V):
    global M, Lprime, L, M_stocké,ligne_de_appuyé
    
    solu=[]
    
    for b in V:
        for j in b:
            appuyé=int(j)
    
            # analyse du bouton appuyé :
            for i in range(len(Lprime)):
                if appuyé in Lprime[i]:
                    ligne_de_appuyé = Lprime[i]
            
            # réponse de l'ordi :
            if appuyé in L:
                if M[appuyé -1] == 0:
                    M[appuyé -1] = 1
                else:
                    M[appuyé -1] = 0
            
            if appuyé-4 in L:
                if M[appuyé-4 -1] == 0:
                    M[appuyé-4 -1] = 1
                else:
                    M[appuyé-4 -1] = 0
                    
            if appuyé+4 in L:
                if M[appuyé+4 - 1] == 0:
                    M[appuyé+4 - 1] = 1
                else:
                    M[appuyé+4 - 1] = 0
                    
            if appuyé-1 in ligne_de_appuyé:
                if M[appuyé-1 -1] == 0:
                    M[appuyé-1 -1] = 1
                else:
                    M[appuyé-1 -1] = 0
            
            if appuyé+1 in ligne_de_appuyé:
                if M[appuyé+1 -1] == 0:
                    M[appuyé+1 -1] = 1
                else:
                    M[appuyé+1 -1] = 0
        
        if M==[1]*len(L):
            solu.append(b)
            
        M=[0]*len(L)
    
    min=solu[0]
    for i in solu:
        if len(i)<len(min):
            min=i
    
    print("########### meilleure combinaison : ############")
    print(min)

def TriInsertion(L):
    for i in range(len(L)):
        j=i-1   #indice de l'élément à insérer
        a=L[i]    #Valeur à insérer
        while L[j]>a and j>=0:
            L[L.index(a)]=L[j]
            L[j]=a
            j=j-1
    return L
    

def liste(L):
    total=[]
        
    petit=[]
    
    for i in range(len(L)):     #1
        petit=[]
        print('i:',i)
        petit.append(L[i])
        petit_bis=[L[i]]
        total.append(petit_bis)
        
        for j in range(i+1,len(L)):     #2
            petit.append(L[j])
            petit_bis=[L[i],L[j]]
            total.append(petit_bis)
            
            for k in range(j+1,len(L)):     #3
                petit.append(L[k])
                petit_bis=[L[i],L[j],L[k]]
                total.append(petit_bis)
                
                for l in range(k+1, len(L)):     #4
                    petit.append(L[l])
                    petit_bis=[L[i],L[j],L[k],L[l]]
                    total.append(petit_bis)
                    
                    for m in range(l+1, len(L)): #5
                        petit.append(L[m])
                        petit_bis=[L[i],L[j],L[k],L[l],L[m]]
                        total.append(petit_bis)
                        
                        for n in range(m+1, len(L)):     #6
                            petit.append(L[n])
                            petit_bis=[L[i],L[j],L[k],L[l],L[m],L[n]]
                            total.append(petit_bis)
                                
                            for o in range(n+1, len(L)):     #7
                                petit.append(L[o])
                                petit_bis=[L[i],L[j],L[k],L[l],L[m],L[n],L[o]]
                                total.append(petit_bis)
                                
                                for p in range(o+1, len(L)):     #8
                                    petit.append(L[p])
                                    petit_bis=[L[i],L[j],L[k],L[l],L[m],L[n],L[o],L[p]]
                                    total.append(petit_bis)
                                    
                                    for q in range(p+1, len(L)):     #9
                                        petit.append(L[q])
                                        petit_bis=[L[i],L[j],L[k],L[l],L[m],L[n],L[o],L[p],L[q]]
                                        total.append(petit_bis)
                                        
                                        for r in range(q+1, len(L)):     #10
                                            petit.append(L[r])
                                            petit_bis=[L[i],L[j],L[k],L[l],L[m],L[n],L[o],L[p],L[q],L[r]]
                                            total.append(petit_bis)
                                            
                                            for s in range(r+1, len(L)):     #11
                                                petit.append(L[s])
                                                petit_bis=[L[i],L[j],L[k],L[l],L[m],L[n],L[o],L[p],L[q],L[r],L[s]]
                                                total.append(petit_bis)
                                                
                                                for t in range(s+1, len(L)):     #12
                                                    petit.append(L[t])
                                                    petit_bis=[L[i],L[j],L[k],L[l],L[m],L[n],L[o],L[p],L[q],L[r],L[s],L[t]]
                                                    total.append(petit_bis)
                                                    
                                                    for u in range(t+1, len(L)):     #13
                                                        petit.append(L[u])
                                                        petit_bis=[L[i],L[j],L[k],L[l],L[m],L[n],L[o],L[p],L[q],L[r],L[s],L[t],L[u]]
                                                        total.append(petit_bis)
                                                    
                                                        for v in range(u+1, len(L)):     #14
                                                            petit.append(L[v])
                                                            petit_bis=[L[i],L[j],L[k],L[l],L[m],L[n],L[o],L[p],L[q],L[r],L[s],L[t],L[u],L[v]]
                                                            total.append(petit_bis)
                                                            
                                                            for w in range(v+1, len(L)):     #15
                                                                petit.append(L[w])
                                                                petit_bis=[L[i],L[j],L[k],L[l],L[m],L[n],L[o],L[p],L[q],L[r],L[s],L[t],L[u],L[v],L[w]]
                                                                total.append(petit_bis)
                                                                
                                                                for x in range(w+1, len(L)):     #16
                                                                    petit.append(L[x])
                                                                    petit_bis=[L[i],L[j],L[k],L[l],L[m],L[n],L[o],L[p],L[q],L[r],L[s],L[t],L[u],L[v],L[w],L[x]]
                                                                    total.append(petit_bis)
                                                                    
                                                                    for y in range(x+1, len(L)):     #17
                                                                        petit.append(L[y])
                                                                        petit_bis=[L[i],L[j],L[k],L[l],L[m],L[n],L[o],L[p],L[q],L[r],L[s],L[t],L[u],L[v],L[w],L[x],L[y]]
                                                                        total.append(petit_bis)
                                                                    
                                                                        for z in range(y+1, len(L)):     #18
                                                                            petit.append(L[y])
                                                                            petit_bis=[L[i],L[j],L[k],L[l],L[m],L[n],L[o],L[p],L[q],L[r],L[s],L[t],L[u],L[v],L[w],L[x],L[y],L[z]]
                                                                            total.append(petit_bis)
                                                                            
                                                                            for a in range(z+1, len(L)):     #19
                                                                                petit.append(L[a])
                                                                                petit_bis=[L[i],L[j],L[k],L[l],L[m],L[n],L[o],L[p],L[q],L[r],L[s],L[t],L[u],L[v],L[w],L[x],L[y],L[z],L[a]]
                                                                                total.append(petit_bis)
                                                                            
                                                                            
                                                                            petit=[L[i],L[j],L[k],L[l],L[m],L[n],L[o],L[p],L[q],L[r],L[s],L[t],L[u],L[v],L[w],L[x],L[y],L[z]]
                                                                        petit=[L[i],L[j],L[k],L[l],L[m],L[n],L[o],L[p],L[q],L[r],L[s],L[t],L[u],L[v],L[w],L[x],L[y]]
                                                                    petit=[L[i],L[j],L[k],L[l],L[m],L[n],L[o],L[p],L[q],L[r],L[s],L[t],L[u],L[v],L[w],L[x]]
                                                                petit=[L[i],L[j],L[k],L[l],L[m],L[n],L[o],L[p],L[q],L[r],L[s],L[t],L[u],L[v],L[w]]
                                                            petit=[L[i],L[j],L[k],L[l],L[m],L[n],L[o],L[p],L[q],L[r],L[s],L[t],L[u],L[v]]
                                                        petit=[L[i],L[j],L[k],L[l],L[m],L[n],L[o],L[p],L[q],L[r],L[s],L[t],L[u]]
                                                    petit=[L[i],L[j],L[k],L[l],L[m],L[n],L[o],L[p],L[q],L[r],L[s],L[t]]
                                                petit=[L[i],L[j],L[k],L[l],L[m],L[n],L[o],L[p],L[q],L[r],L[s]]
                                            petit=[L[i],L[j],L[k],L[l],L[m],L[n],L[o],L[p],L[q],L[r]]
                                        petit=[L[i],L[j],L[k],L[l],L[m],L[n],L[o],L[p],L[q]]
                                    petit=[L[i],L[j],L[k],L[l],L[m],L[n],L[o],L[p]]
                                petit=[L[i],L[j],L[k],L[l],L[m],L[n],L[o]]
                            petit=[L[i],L[j],L[k],L[l],L[m],L[n]]
                        petit=[L[i],L[j],L[k],L[l],L[m]]
                    petit=[L[i],L[j],L[k],L[l]]
                petit=[L[i],L[j],L[k]]
            petit=[L[i],L[j]]
        petit=[L[i]]
    
    essayer(total)
    
liste(L)
            
                        