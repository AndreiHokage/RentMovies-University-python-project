'''
Created on Nov 20, 2020

@author: BalaniciAndrei
'''

class RaportClient:
    
    def __init__(self,id_client,nr_filme):
        self.__id_client=id_client 
        self.__nume=None 
        self.__nr_filme=nr_filme
        self.__lista_filme=[]
    
    def add_film(self,id_film):
        '''
        Functia adauga id ul filmului la lista de filme pentru un client
        Date de intrare:id_film-un int ce reprez id ul filmului
        Date de iesire:-
        '''
        self.__lista_filme.append(id_film)
        
    def get_lista_filme(self):
        '''
        Functia returneaza lista de filme pentru un client
        Date de intrare:-
        Date de iesire:o lista de filme
        '''    
        return self.__lista_filme
        
    def inc(self):
        '''
        Functia incrementeaza nr de filme inchiriate
        '''
        self.__nr_filme+=1
        
    def get_id_client(self):
        '''
        Functia returneaza id ul clientului
        '''
        return self.__id_client 
    
    def get_nume(self):
        '''
        Functia returneaza numele clientului
        Return:un string,nume 
        '''
        return self.__nume 
    
    def get_nr_filme(self):
        '''
        Functia returneaza nr de filme inchiriate de client
        Return;un int,nr de filme
        '''
        return  self.__nr_filme
    
    def set_nume(self,nume):
        '''
        Functia seteaza numele clientului
        date de intrare:nume- un string,ce rerezinya numele clientului
        '''
        self.__nume=nume
        