from exceptii.exceptii_entitati import RepositoryError_Inchiriere
from domain.DTO_RaportClient import RaportClient
from domain.DTO_ReportFilm import RaportFilm

class Repository_Inchiriere(object):
    
    def __init__(self):
        self.__elem=[]
    
    def __adaugare(self,inchiriere):
        '''
        Functia adauga la lista inchirierea
        Date de intrare:self-un repository de inchirieri
                        inchiriere-o inchiriere de tip Inchiriere
        Return:-
        '''
        self.__elem.append(inchiriere)
    
    def get_all(self):
        return self.__elem[:]
    
    def __get_element(self, i):
        '''
        Fucntia returneaza inchirierea de pe pozitia i
        Date de intrare:self-un repository de inchirieei
                        i-index
        Return :o inchiriere de top Inchiriere
        '''
        return self.__elem[i]
    
    
    def __stergere(self, i):
        '''
        Fucntia sterge inchirierea de pe pozitia i
        Date de intrare:self-un repository de inchirieei
                        i-index
        Return :-
        '''
        del self.__elem[i]
    
    
    def __len__(self):
        '''
        Functia returneaza numarul de ichirieri
        Date de intrare:self-un repository de ichiriereif
        Return: un int ce reprezinta numarul de inchirierie
        '''
        return len(self.__elem)
    
    def add(self, inchiriere):
        '''
        Functia aduaga o inchiriere in lista de inchirieri 
        Date de intrare:self-un repository de inchirieri
                        inchiriere-o inchiriere de tip Inchiriere
        Return:-
        Ridica exceptii de tip RepositoryError_Inchiriere daca inchirierea a fost gasita
        '''
        if inchiriere in self.__elem:
            raise RepositoryError_Inchiriere("Clientul a inchiriat deja filmul!\n")
        
        if inchiriere.get_film().get_capacitate()<1:
            raise RepositoryError_Inchiriere("Nu mai exista exemplare de acest tip!\n")
        
        self.__adaugare(inchiriere)
        inchiriere.get_film().take_capacitate_unit() 

    
    def find(self, inchiriere):
        '''
        Functia gaseste o inchiriere in lista de inchirieri
        Date de intrare:self-un repository de inchirieri
                        inchiriere-o inchiriere de tip Inchiriere
        Return:o inchiriere de tip Inchiriere 
        Ridica exceptii de tip RepositoryError_Inchiriere daca inchirierea nu a fost gasit
        
        '''
        if inchiriere not in self.__elem:
            raise RepositoryError_Inchiriere("Nu exista o astfel de inchiriere!\n")
        
        for elem in self.__elem:
            if(elem==inchiriere):
                return inchiriere
            
    
    
    def remove(self, inchiriere):
        '''
        Functia stereg o inchiriere in lista de inchirieri
        Date de intrare:self-un repository de inchirieri
                        inchiriere-o inchiriere de tip Inchiriere
        Return:-
        Ridica exceptii de tip RepositoryError_Inchiriere daca inchirierea nu a fost gasit
        '''
        if inchiriere not in self.__elem:
            raise RepositoryError_Inchiriere("Nu exista o astfel de inchiriere!\n")
        
        for i in range(len(self.__elem)):
            elem=self.__get_element(i)
            if(elem==inchiriere):
                self.__stergere(i)
                inchiriere.get_film().get_capacitate_unit()
                return
                
    
    def ClientiCuFilmeInchiriate(self):
        '''
        Functia contriueste o lista de obiecte de tip RaportClient
        Date de intrare:self-un service de inchirierir
        Return-o lista de obiecte RaportClient
        '''
        dictCF={}
        for elem in self.__elem:
            client=elem.get_client()
            id_client=client.get_id_client()
            if id_client in dictCF.keys():
                dictCF[id_client].inc()
            else:
                dictCF[id_client]=RaportClient(id_client,1)
            dictCF[id_client].add_film(elem.get_film().get_id_film())
        
        ans=list(dictCF.values())
        return ans

    def FilmeInchiriateDeClienti(self):
        '''
        Functia construieste o lista de obiecte de tip RaportFilm
        Date de intrare:self-un service de inchirierir
        Return-o lista de obiecte RaportFilm 
        '''
        dictCF={}
        for elem in self.__elem:
            film=elem.get_film()
            id_film=film.get_id_film()
            id_client=elem.get_client().get_id_client()
            if id_film in dictCF.keys():
                dictCF[id_film].inc() 
            else:
                dictCF[id_film]=RaportFilm(id_film,1)
            dictCF[id_film].add_client(id_client)  
        ans=list(dictCF.values())
        return ans
    
    
    



