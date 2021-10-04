'''
Created on Dec 16, 2020

@author: BalaniciAndrei
'''
import math

class Sortari: 
    
    @staticmethod
    def InsertionSort(lista,key=lambda x:x,reverse=False,cmp=lambda x,y:x<y):
        '''
        Functia sorteaza elementele unei liste dupa funcrtia key stabilind ordinea prin reveerse
        '''
        for i in range(1,len(lista)):
            idx=i-1 
            val=lista[i] 
            while idx>=0 and cmp(key(val),key(lista[idx])):
                lista[idx+1]=lista[idx] 
                idx=idx-1 
            lista[idx+1]=val 
        if reverse==True:
            lista.reverse()
        return lista
    
    @staticmethod
    def CombSort(lista,key=lambda x:x,reverse=False,cmp=lambda x,y:x>y):
        '''
        Functia sorteaza elementele unei liste dupa funcrtia key stabilind ordinea prin reveerse
        '''
        lenght=len(lista)
        factor_shrink=1.3  #factor de impartire
        gap=lenght 
        issorted=False    #variabila ce identifica daca lista este sau nu sortata
        while issorted==False:
            gap=math.floor(gap/factor_shrink)  #reduce lungimea sariturii
            if(gap<=1) :
                gap=1
                issorted=True
            stop=lenght-gap
            for i in range(0,stop):
                if cmp(key(lista[i]),key(lista[i+gap])):
                    lista[i],lista[i+gap]=lista[i+gap],lista[i]  #se interschimba elementele care nu sunt in ordine 
                    issorted=False  #se marcheaza faptul ca lista nu este sortata
        if reverse==True:
            lista.reverse()
        return lista
    
