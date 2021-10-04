
class Client():
    ''' Abstraxtizeaza tipul client
        Domain: id_client-id ul prin care clientul este  identificat
                nume-numele clientului
                cnp-cnp-ul clientului
    '''
    def __init__(self,id_client,nume,cnp):
        self.__id_client=id_client
        self.__nume=nume 
        self.__cnp=cnp 
    
        
    def get_id_client(self):
        ''' Functia da id_ul clientului
            Date de intrare: self-un client
            Returneaza id ul(int) clientul
        '''
            
        return self.__id_client
    
    def get_nume(self):
        ''' Functia da id_ul clientului
            Date de intrare: self-un client
            Returneaza numele(string) clientul
        '''
        return self.__nume 
    
    def get_cnp(self):
        ''' Functia da id_ul clientului
            Date de intrare: self-un client
            Returneaza cnp ul(string) clientul
        '''
        return self.__cnp
    
    def set_nume(self,nume):
        ''' Functia seteaza mumele clientului
            Date de intrare:self-un client
                            nume-string
            Returneaza -
        '''
        self.__nume=nume 
    
    def set_cnp(self,cnp):
        ''' Functia seteaza cnp ul clientului
            Date de intrare:self-un client
                            cnp-un string
            Returneaza -
        '''
        self.__cnp=cnp
    
    def __eq__(self,other):
        ''' Functia retuneaza egalitatea a doua clienti fata de id ul lor
            Date de intrare:sefl-un client
                            other- un client
            Return:True-daca clienii au id urile egale 
                   False-daca clienti nu au id urile egale
        '''
        return self.get_id_client()==other.get_id_client()
    
    def __str__(self):
        '''Functia returneaza un string ce reprezinta un client
           Date de intrare:self-un client
           Return un string ce reprezinta un client
        '''
        return "Id:"+str(self.get_id_client())+"  Nume:"+self.get_nume()+"  Cnp:"+self.get_cnp()



