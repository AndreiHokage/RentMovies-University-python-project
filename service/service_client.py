from domain.entities_client import Client
import string
import random
from exceptii.exceptii_entitati import ClientError, RepositoryError_Client,\
    RepositoryError_Inchiriere

class ServiceClient(object):
    
    def __init__(self,repository_client,repository_inchiriere,validator):
        self.__rep_client=repository_client
        self.__rep_inchiriere=repository_inchiriere
        self.__validator=validator
        
    def adaugare(self,id_client,nume,cnp):
        '''Functia adauga un client in  
           Date de intrare:self-un service_client
                           nume-numele clientului de tip string
                           cnp -un string de 13 cifre ce reprezinta cnp ul clientului
                           id_client-un int ce reprezinta id ul clietuli
           Return:-
           Ridica exceptii de tip ClientError daca validarea nu reuseste
           Ridica exceptii de tip repositoryyError_Client daca  exista un astfel de client cu id ul id_client
        ''' 
        client=Client(id_client,nume,cnp) 
        self.__validator.validare_client(client)
        self.__rep_client.add(client)
      
        
    def find(self,id_client):
        '''Functia  returneaza un client de tip Client cu id ul id_client
           Date de intrare:self-un service client 
                           id_client-un int ce reprezinta id ul clientuli
           Return-un client de tip Client cu id ul ega cu id_client
           Functia ridica exceptii de tip repositoryyError_Client daca nu exista un astfel de client
        '''
        return self.__rep_client.search(id_client)
        
    def search_nume(self,nume):
        '''
        Functia returneaza o lista de clienti cu numele nume
        Date de intrare:self-un service client
                        nume-un string ce reprezinta un nume
        Return:o lista de clienti
        '''
        ans=[]
        lista=self.__rep_client.get_all_client()
        for elem in lista:
            if elem.get_nume()==nume:
                ans.append(elem)
        return ans[:]
    
    def update(self,id_client,nume,cnp):
        '''
        Functia updateaza un client  
        Datre de intrare:self-un service_client
                        nume-numele clientului de tip string
                        cnp -un string de 13 cifre ce reprezinta cnp ul clientului
                        id_client-un int ce reprezinta id ul clietuli
        Return :-
        Ridica exceptii de tip repositoryyError_Client daca nu exista un astfel de client
        Ridica exceptii de tip ClientError daca validarea nu reuseste
        '''
        client=Client(id_client,nume,cnp)
        self.__validator.validare_client(client)
        self.__rep_client.update(client)
    
    def there_inchirieri_client(self,id_client):
        '''
        Functia verifica daca exista filme inchiriate de clientul cu id ul id_client
        Date de intrare:self-un repository de inchirieri
                        id_client-un int ce reprezinta id ul clintului
        Return:1-daca se gaseste o inchiriere facuta de acel client,0 in caz contrar
        '''
        lista=self.__rep_inchiriere.ClientiCuFilmeInchiriate()
        for elem in lista:
            if(elem.get_id_client()==id_client):
                return True;
        return False
    
    def remove(self,id_client):
        '''Functia  updateaza un client de tip Client cu id ul id_client
           Date de intrare:self-un service client 
                           id_client-un int ce reprezinta id ul clientuli
           Return-
           Functia ridica exceptii de tip repositoryyError_Client daca nu exista un astfel de client
           Functia arunca exceptii de tip RepositoryError_Inchiriere daca clientul are inchirieri
        '''
        if self.there_inchirieri_client(id_client) == True:
            raise RepositoryError_Inchiriere("Clientul nu se poate elimina deoarece are inchirieri facute!\n")
        self.__rep_client.delete_client(id_client)
    
        
    def len_rep_client(self):
        '''
        Functia retuneaza lungimea listei de concurenti
        Date de intrare:self-un serviceclient
        Reurneaz un int ce reprezinta lg listei de clienti
        '''
        return len(self.__rep_client)
    
    def get_all_client(self):
        '''
        Functia da toti clientii prezenti in firma de inchirirat
        Date de intrare: self-un ServiceClient
        Retuneaza  lista tuturor clientilor prezenti 
        '''
        return self.__rep_client.get_all_client()
    
    def generare_client(self,n):
        letters=string.ascii_lowercase
        digit=string.digits
        lg_id=self.len_rep_client()+n
        i=0
        while(i<n):
            lg_nume=random.randint(6,10)
            nume=''.join(random.choice(letters) for j in range(0,lg_nume))
            cnp=''.join(random.choice(digit) for j in range(0,13))
            id_client=random.randint(1,lg_id)
            try:
                self.adaugare(id_client, nume, cnp)
                i+=1
            except ClientError:
                continue
            except RepositoryError_Client:
                continue
            
    