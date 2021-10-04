class Inchiriere(object):
    
    def __init__(self,client,film):
        self.__client=client 
        self.__film=film 
        
    def get_client(self):
        '''
        Functia returneaza clientul care a inchiriat filmul 
        Date de intrare:self-o inchiriere de tip Inchiriere 
        Return: un client de tip Client
        '''
        return self.__client 
    
    def get_film(self):
        '''
        Functia returneaza filml care a fost inchiriat de client 
        Date de intrare:self-o inchiriere de tip Inchiriere 
        Return: un film de tip Film
        '''
        return self.__film 
        
    def __eq__(self,other):
        '''
        Functia compara doua inchirierei
        Date de intrare: self-o inchiriere de tip Inchiriere
                         other-o inchiriere de tip Inchiriere
        Return :True daca cele doua inchirieri sunt identice,False in caz contrar
        '''
        return (self.__client.get_id_client()==other.__client.get_id_client()) and (self.__film.get_id_film()==other.__film.get_id_film())
    
    def __str__(self):
        '''
        Functia afiseaza o inchiriere
        Date de intrare:self-o inchiriere
        Return: un string ce reprezinta o inchiriere 
        '''
        return "Clientul: "+str(self.__client)+" a inchiriat:\nFilmul " + str(self.__film)+'\n'
    

