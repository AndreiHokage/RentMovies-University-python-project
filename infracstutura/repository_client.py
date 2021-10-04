
from exceptii.exceptii_entitati import RepositoryError_Client

class Repository_Client():
    
    def __init__(self):
        self._elems=[]

    def __len__(self):
        '''
        Functia retuneaza lungimea listei de concurenti
        Date de intrare:self-un repository de tip Client
        Reurneaz un int ce reprezinta lg listei de clienti
        '''
        return len(self._elems)
    
    
    def __adauga(self,client):
        '''
        Functia adauga un client in ista de clienti
        Date de intrare;client-un client de tip Client
                        self-un reposirory_client
        Return :-
        '''
        self._elems.append(client)
    
    def __stergere(self,idx):
        '''Functia sterge un client din lista
           Date de intrare:self-un repository_client
                           idx-nr de ordine al clientul e e tip int
           Return -
        '''
        del self._elems[idx]
    
    def __get_client_from_repository(self,idx):
        '''Functia retuneaza un clint din repository
           Date de intrare:self-repository_client
                           idx-nr de indexare a clientului adaugat de tip int
           Retuneaza un client de tip client
        '''
        return self._elems[idx]
    
    def get_all_client(self):
        '''
        Functia da toti clientii prezenti in firma de inchirirat
        Date de intrare: self-un rpository_client
        Retuneaza  lista tuturor clientilor prezenti 
        '''
        return self._elems
    
    def add(self,client):
        ''' 
            Functia adauga un client in Repository_Client 
            Date de iintrare:self-un repositoy_client
                             client-un client de tip Client
            Return -
            Functia ridica exceptii RepositoryError_Client daca clientul se afla deja in lista
        '''
        if client in self._elems:
            raise RepositoryError_Client("Clientul se afla deja in lista de clienti!\n")
        self.__adauga(client)
        
    def search(self,client_id):
        '''
        Functia cauta un client dupa client_id
        Date de intrare: self-un repository client
                         clint_id-un int ce reprezinta id ul clientului
        Returneaza: un client de tip client
        Functia ridica exceptii RepositorError_Client daca clientul nu se afla in lista
        '''
        '''gasit=False
        for client in self._elems:
            if(client.get_id_client()==client_id):
                gasit=True
                
        if gasit==False:
            raise RepositoryError_Client("Clientul nu se afla in lista de clienti!\n")
        
        for elem in self._elems:
            if(elem.get_id_client()==client_id):
                return elem # ma intereseaza si adresa de memorie originala'''
        
        return self.__search_recursiv(self._elems[:], client_id)
    
    
    def __search_recursiv(self,lista,client_id):
        if lista==[]:
            raise RepositoryError_Client("Clientul nu se afla in lista de clienti!\n")
        
        if lista[0].get_id_client()==client_id:
            return lista[0] 
         
        return self.__search_recursiv(lista[1:],client_id)
    
    def update(self,client):
        '''Functia face updat ul  unui client 
           Date de intrare:self-un repository_client
                           client-un nou client de tip client
           return -
           Functia ridica exceptii de tip RepositoryError_Client daca clientul nu exista clientul
        '''
        if client not in self._elems:
            raise RepositoryError_Client("Clientul nu se afla in lista de clienti!\n")
        for elem in self._elems:
            if(elem==client):
                elem.set_cnp(client.get_cnp())
                elem.set_nume(client.get_nume())
                return 
            
    def delete_client(self,client_id):
        '''Functia sterge clientul din repository_client
           Date de intrare:self-un repository_client
                           cient_id-un int ce reprezinta id ul clientului
           return -
           Functia ridica exceptii RepositoryError_Client daca nu exista client ul
        '''
        gasit=False
        for client in self._elems:
            if(client.get_id_client()==client_id):
                gasit=True
                
        if gasit==False:
            raise RepositoryError_Client("Clientul nu se afla in lista de clienti!\n")
        
        for i in range(len(self)):
            elem=self.__get_client_from_repository(i)
            if(elem.get_id_client()==client_id):
                self.__stergere(i)
                return 
            