from domain.inchiriere import Inchiriere
from domain.DTO_RaportClient import RaportClient
from math import ceil
from domain.DTO_ReportFilm import RaportFilm
from http import client
from exceptii.exceptii_entitati import RepositoryError_Inchiriere
from Metode_de_sortare import Sortari

class ServiceInchirieri(object):
    
    
    def __init__(self,rep_client,rep_film,rep_inchir):
        self.__rep_client=rep_client
        self.__rep_film=rep_film
        self.__rep_inchir=rep_inchir
    
    def inchiriere(self,id_client,id_film):
        '''
        Functia realizeaza inchirerea filmului cu id ul id_film de catre clientul cu id_client
        Date de intrare: self-un serviceinchirieri
                         id_client-un int ce specifica id ul clientului
                         id_film- un int ce specifica id ul filmului
        Functia arunca exceptii de tip: RepositoryError_Film daca id_film nu se gaseste in lista
                                        RepositoryError_Client daca id_clent nu se gaseste in lista
                                        RepositoryError_Inchiriere daca inchirieera nu este prezent in lista de inchirieri
        '''
        client=self.__rep_client.search(id_client)
        film=self.__rep_film.search(id_film)
        inchirierede=Inchiriere(client,film)
        self.__rep_inchir.add(inchirierede)
        self.__rep_film.upload_to_file()
        
    def returnare(self,id_client,id_film):
        '''
        Functia realizeaza returnarea filmului cu id ul id_film de catre clientul cu id_client
        Date de intrare: self-un serviceinchirieri
                         id_client-un int ce specifica id ul clientului
                         id_film- un int ce specifica id ul filmului
        Functia arunca exceptii de tip: RepositoryError_Client daca id_clent nu se gaseste in lista
                                        RepositoryError_Film daca id_film nu se gaseste in lista
                                        RepositoryError_Inchiriere daca inchirieera nu este prezent in lista de inchirieri
        '''
        client=self.__rep_client.search(id_client)
        film=self.__rep_film.search(id_film) 
        inchiriere=Inchiriere(client,film)
        self.__rep_inchir.remove(inchiriere)
        self.__rep_film.upload_to_file()
     
    def returnare_client_filme(self,id_client):
        '''
        Functia sterge toate filmele pe care clientul cu id_client le a inchiriat
        Date de intrare:self-serviceinchirieri
                        id_client-un int ce reprez id ul clientul care sterge toate filmele inchiriate
        Return:-
        Functia arunca exceptii de tip RpositoryError_Client daca id ul nu corespunde
        '''
        client=self.__rep_client.search(id_client)
        lista=self.__rep_film.get_all_film()
        for elem in lista:
            try:
                rent=Inchiriere(client,elem)
                self.__rep_inchir.find(rent)
                self.__rep_inchir.remove(rent)
            except RepositoryError_Inchiriere:
                pass 
        self.__rep_film.upload_to_file()     
            
    def returnare_filme_client(self,id_film): 
        '''
        Functia sterge toti clientii pentru care filmul cu id id_film este inchiriat inchiriat
        Date de intrare:self-serviceinchirieri
                        id_client-un int ce reprez id ul clientul care sterge toate filmele inchiriate
        Return:-
        Functia arunca exceptii de tip RpositoryError_Film daca id ul nu corespunde
        '''
        film=self.__rep_film.search(id_film)
        lista=self.__rep_client.get_all_client()
        for elem in lista:
            try:
                rent=Inchiriere(elem,film)
                self.__rep_inchir.find(rent)
                self.__rep_inchir.remove(rent)
            except RepositoryError_Inchiriere:
                pass      
        self.__rep_film.upload_to_file()
        
    def find_film(self,id_client,id_film):
        '''
        Functia gaseste filmul cu id_film ce afost inchiriat de clientul cu id_client
        Date de intrare: self-un serviceinchirieri
                         id_client-un int ce specifica id ul clientului
                         id_film- un int ce specifica id ul filmului
        Return:un film de tip Film 
        Areunca exceptii de tip:RepositoryError_Film daca id_film nu se gaseste in lista
                                RepositoryError_Client daca id_clent nu se gaseste in lista
                                RepositoryError_Inchiriere daca inchirieera nu este prezent in lista de inchirieri     
        '''
        client=self.__rep_client.search(id_client)
        film=self.__rep_film.search(id_film)
        inchiriere=Inchiriere(client,film)
        return self.__rep_inchir.find(inchiriere).get_film()
    
    def nr_filme_inchiriate(self,id_client):
        '''
        Functia returneaza numarul de filme inchiriate de clientul client
        Date de intrare:self-un serviceinchirieri
                        id_client- un int ce reprez   id_client
        Return -un int ce reprez nr de filme inchiriate
        Metoda arunca exceptii:RepositoryError_Client daca id_clent nu se gaseste in lista
        '''
        cnt=0
        client=self.__rep_client.search(id_client)
        lista=self.__rep_film.get_all_film()
        for elem in lista:
            try:
                self.__rep_inchir.find(Inchiriere(client,elem))
                cnt+=1
            except RepositoryError_Inchiriere:
                pass
        return cnt
    
    def nr_clienti_inchiriaza(self,id_film):
        '''
        Functia returneaza numarul de clienti ce au inchiriat fulmul film
        Date de intrare:self-un serviceinchirieri
                        id_film- un int ce reprez id ul filmului 
        Return -un int ce reprez nr de clienti ce au inchiriat acel film
        Arunca RepositoryError_Film daca id_film nu se gaseste in lista
        '''
        cnt=0
        film=self.__rep_film.search(id_film)
        lista=self.__rep_client.get_all_client()
        for elem in lista:
            try:
                self.__rep_inchir.find(Inchiriere(elem,film))
                cnt+=1
            except RepositoryError_Inchiriere:
                pass
        return cnt
        
    def get_list_filme_inchiriate(self,id_client):
        '''Functia returneaza lista tuturor filmelor inchiriate de cientul cu id id_client
           Date de intrare:self-un serviceinchirieri
                           id_client-un int ce reprez id_client
           Return-o lista de filme inchiriate
           Metoda arunca exceptii:RepositoryError_Client daca id_clent nu se gaseste in lista
        '''
        ans=[]
        client=self.__rep_client.search(id_client)
        lista=self.__rep_inchir.ClientiCuFilmeInchiriate()
        for elem in lista:
            if(elem.get_id_client()==id_client):
                lista_id=elem.get_lista_filme()
                for id_film in lista_id:
                    film=self.__rep_film.search(id_film)
                    ans.append(film)
                break
        return ans
    
    def get_list_clienti_inchiriati(self,id_film):
        '''Functia returneaza lista tuturor clienilor ce au inchiriat filmul cu id id_film
           Date de intrare:self-un serviceinchirieri
                           id_film-un int ce reprez id_film
           Return-o lista de clienti ce au inchiriat filmul
           Metoda arunca exceptii:RepositoryError_Film daca id_film nu se gaseste in lista
        '''
        ans=[]
        film=self.__rep_film.search(id_film)
        lista=self.__rep_inchir.FilmeInchiriateDeClienti()
        for elem in lista:
            if(elem.get_id_film()==id_film):
                lista_id=elem.get_lista_client()
                for id_client in lista_id:
                    client=self.__rep_client.search(id_client)
                    ans.append(client)
                break
            
        return ans
    
    def set_name_movies(self,lista):
        '''
        Functia seteaza numee tuturor filmelor care au participat la inchiriere
        Date de intrare:lista-list de obiecte DTO_RaportFilm
        Date de iesire:-
        '''
        for elem in lista:
            film=self.__rep_film.search(elem.get_id_film())
            elem.set_titlu(film.get_titlu())
            elem.add_nr_clienti(film.get_nr_returnari())
    
    def set_names_clienti(self,lista):
        '''
        Functia seteaza numee tuturor clientilor care au participat la inchiriere
        Date de intrare:lista-list de obiecte DTO_RaportClient
        Date de iesire:-
        '''
        for elem in lista:
            elem.set_nume(self.__rep_client.search(elem.get_id_client()).get_nume())
    
    def sortare_nr_filme(self):
        '''
        Functia retuneaza o lista de obiecte RaportFilme ordonat dupa numarul de clienti
        Date de intrare:self-un service de inchirierir
        Rreturn: o lista de obiecte RaportFilme
        '''
        rez=self.__rep_inchir.FilmeInchiriateDeClienti()
        self.set_name_movies(rez)
        rez=Sortari.CombSort(rez, key=lambda x:x.get_nr_clienti(), reverse=True)
        #rez=sorted(rez, key=lambda x:x.get_nr_clienti(), reverse=True)
        return rez
       
    def sortare_clienti_nume(self):
        '''
        Functia retuneaza o lista de obiecte ReportClient ordonati crescator dupa nume
        Date de intrare:self-un service de inchirierir
        Return:o lista de obiecte ReportClient ordonati crescator dupa nume
        '''
        rez=self.__rep_inchir.ClientiCuFilmeInchiriate()
        self.set_names_clienti(rez)
        rez=Sortari.InsertionSort(rez, key=lambda x:x.get_nume())
        #rez=sorted(rez, key=lambda x:x.get_nume()) 
        return rez

    
    def sortare_clienti_nr_filme(self):
        '''
        Functia retuneaza o lista de obiecte ReportClient ordonati crescator dupa nr de filme
        Date de intrare:self-un service de inchirierir
        Return:o lista de obiecte ReportClient ordonati crescator dupa nr de filme
        '''
        rez=self.__rep_inchir.ClientiCuFilmeInchiriate()
        self.set_names_clienti(rez)
        rez=Sortari.InsertionSort(rez, key=lambda x:x.get_nr_filme())
        #rez=sorted(rez,key=lambda x:x.get_nr_filme())
        return rez

    
    def sortare_clienti_partial(self):
        '''
        Functia retuneaza o lista de 30% de obiecte din totalul clientilor ReportClient 
                                                 ordonati descrescator dupa nr de filme
        Date de intrare:self-un service de inchirierir
        Return:o lista de obiecte ReportClient ordonati descrescator dupa nr de filme
        '''
        rez=self.__rep_inchir.ClientiCuFilmeInchiriate()
        self.set_names_clienti(rez)
        rez=Sortari.CombSort(rez, key=lambda x:x.get_nr_filme(), reverse=True)
        #rez=sorted(rez, key=lambda x:x.get_nr_filme(), reverse=True)
        nr_clienti=ceil(len(rez)*3/10)
        rez=rez[:nr_clienti]
        return rez
            
    
    def sortare_filme_gen(self,gen):
        ans=[]
        viz={}
        lista_clienti=self.__rep_client.get_all_client()
        lista_dto=self.__rep_inchir.ClientiCuFilmeInchiriate()
        for elem in lista_dto:
            ok=0
            id_client=elem.get_id_client()
            viz[id_client]=1
            lista_filme=elem.get_lista_filme()
            for id_film in lista_filme:
                gen_film=self.__rep_film.search(id_film).get_gen()
                if gen==gen_film:
                    ok=1
                    break
            if ok==0:
                ans.append(self.__rep_client.search(id_client))
        for client in lista_clienti:
            id_client=client.get_id_client()
            if id_client not in viz.keys():
                ans.append(client)
        return ans
    
    def __cmp(self,x,y): 
        if x.get_nr_filme()<y.get_nr_filme():
            return True
        elif x.get_nr_filme()==y.get_nr_filme():
            return (x.get_nume()<y.get_nume())
        else:
            return False 
            
    
    def sortare_criteriu_dublu(self):
        '''
        Functia sorteaza dupa dupa nr de filme a tuturor clientilor care au inchiriat si in caz de egalitate dupa nume
        Date de intrare:-
        Date de iesire:lista-o lista de obiecte DTO_RaportClient ordonate dupa criteriile specificate
        '''
        lista=self.__rep_inchir.ClientiCuFilmeInchiriate()
        self.set_names_clienti(lista)
        lista=Sortari.InsertionSort(lista,cmp=self.__cmp)
        return lista
        
