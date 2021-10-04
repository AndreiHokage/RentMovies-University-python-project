'''
Created on Nov 20, 2020

@author: BalaniciAndrei
'''
class RaportFilm:
    
    def __init__(self,id_film,nr_clienti):
        self.__id_film = id_film
        self.__titlu = None
        self.__nr_clienti = nr_clienti
        self.__lista_client=[]
    
    def add_client(self,id_client):
        '''
        Functia adauga clienti 
        Date de intrare:id_clien-int ce repreznta id ul uni client
        '''
        self.__lista_client.append(id_client)
    
    def get_lista_client(self):
        '''
        Functia returneaza o lista cu id ul clientilor care au inchiriat acel film
        '''
        return self.__lista_client
    
    def inc(self):
        '''
        Functia incrementeaza numarul de clienti care au inchiriat acest film
        '''
        self.__nr_clienti+=1
    
    def get_id_film(self):
        '''
        Functia retuneaza un int ce repre id filmu lui
        '''
        return self.__id_film 
    
    def get_titlu(self):
        '''
        Functia returneaza un string,numele filmului
        '''
        return self.__titlu
    
    def get_nr_clienti(self):
        '''
        Functia returneaza un int,ce reprezinta numarul de clienti care l-au inchiriat
        '''
        return self.__nr_clienti
    
    def add_nr_clienti(self,x):
        self.__nr_clienti+=x
        
    def set_titlu(self,titlu):
        '''
        Functia seteazza titlul unui film
        Date de intrare:titlu-un string ce reprezinta titlu unui film
        Return:-
        '''
        self.__titlu=titlu