'''
Created on Nov 27, 2020

@author: BalaniciAndrei
'''
from infracstutura.repository_client import Repository_Client
from domain.entities_client import Client

class Repository_Client_File(Repository_Client):
    
    def __init__(self,file_name):
        Repository_Client.__init__(self)
        self.__file_name=file_name 
        
    def __loadfromfile(self):
        '''
        Functia incarca continutul fisierului in memorie
        '''
        self._elems=[]
        with open(self.__file_name) as f:
            for line in f:
                if line.strip()=="":
                    continue 
                atrb=line.split(';')
                client=Client(int(atrb[0]),atrb[1].strip(),atrb[2].strip())
                self._elems.append(client) 
                
    def __storetofile(self):
        '''
        Functia incarca tori clientii din memorie in fisier 
        '''
        with open(self.__file_name,"w") as f:
            for client in self._elems:
                linie=str(client.get_id_client())+";"+client.get_nume()+";"+client.get_cnp()
                f.write(linie)
                f.write("\n")
                
    def add(self,client):
        '''
        Functia adauga un client in repositry_clint si dupa salveaza si in fisier
        Date de intrare:client -un client de tip Client
        Return:-
        Functia ridica exceptii RepositoryError_Client daca clientul se afla deja in lista
        '''
        self.__loadfromfile()
        Repository_Client.add(self,client)
        self.__storetofile()
    
    def update(self,client):
        '''
           Functia face updat ul  unui client si salveaza si in fisier
           Date de intrare:self-un repository_client
                           client-un nou client de tip client
           return -
           Functia ridica exceptii de tip RepositoryError_Client daca clientul nu exista clientul
        ''' 
        self.__loadfromfile()
        Repository_Client.update(self, client)
        self.__storetofile() 
        
    def delete_client(self, client_id):
        '''Functia sterge clientul din repository_client si salveaza in fisier
           Date de intrare:self-un repository_client
                           cient_id-un int ce reprezinta id ul clientului
           return -
           Functia ridica exceptii RepositoryError_Client daca nu exista client ul
        '''  
        self.__loadfromfile()
        Repository_Client.delete_client(self, client_id)
        self.__storetofile()
    
    def get_all_client(self):
        self.__loadfromfile()
        return Repository_Client.get_all_client(self)
    
    def search(self,client_id):
        self.__loadfromfile() 
        client=Repository_Client.search(self, client_id)
        return client
