
class Film(object):
    
    def __init__(self,id_film,titlu,descriere,gen,capacitate):
        self.__id_film=id_film
        self.__titlu=titlu 
        self.__descriere=descriere 
        self.__gen=gen 
        self.__capacitate=capacitate
        self.__nr_returnari=0
    
    def get_id_film(self):
        ''' Metoda returneaza id ul unui film
            Date de intrare: self-un film
            Return un intreg ce repreinta id ul filmuluiu
        '''
        return self.__id_film 
    
    def get_nr_returnari(self):
        '''
        Metoda returneaza nr de returnari ale unui film
        Date de intrare: self-un film
        Return un intreg ce repreinta nr de returnari filmuluiu
        '''
        return self.__nr_returnari
    
    def get_titlu(self):
        '''Metoda returneaza titlu unui film
           Date de intrare: self-un film
           Return un string ce reprezinta numele filmului
        '''
        return self.__titlu
    
    def get_descriere(self):
        '''Metoda returneaza descrierea unui film
           Date de intrare: self-un film
           Return un string ce reprezinta descrierea filmului
        '''
        return self.__descriere 
    
    def get_capacitate(self):
        '''
        Metoda returneaza nr de filme de un tip pe care le detne firma
        Date de intrare:self-un film de tip Film
        Return:un int ce reprezinta nr de exemplare
        '''
        return self.__capacitate
    
    def get_gen(self):
        '''Metoda returneaza genul unui film
           Date de intrare: self-un film
           Return un string ce reprezinta genul filmului
        '''
        return self.__gen 
    
    def set_titlu(self,titlu):
        '''Functia seteaza titlul unui film
           Date de inrare:self-un film
                          titlu-un string
           Return -
        '''
        self.__titlu=titlu 
        
    def set_descriere(self,descriere):
        '''Functia seteaza descrierea unui film
           Date de inrare:self-un film
                          descriere-un string
           Return -
        '''
        self.__descriere=descriere 
        
    def set_gen(self,gen):
        '''Functia seteaza genul unui film
           Date de inrare:self-un film
                          genul-un string
           Return -
        '''
        self.__gen=gen 
     
    def set_capacitate(self,capacitate):
        '''
        Metoda seteaza nr de exemplare pentru un film
        Date de intrare:self-un film
        Return :-
        ''' 
        self.__capacitate=capacitate
    
    def take_capacitate_unit(self):
        self.__capacitate-=1 
        
    def get_capacitate_unit(self):
        self.__nr_returnari+=1
        self.__capacitate+=1
        
    def __eq__(self,another):
        ''' Functia retuneaza egalitatea a doua filme fata de id ul lor
            Date de intrare:sefl-un film
                            other- un film
            Return:True-daca filmele au id urile egale 
                   False-daca filmele nu au id urile egale
        '''
        return self.get_id_film()==another.get_id_film()
    
    def __str__(self):
        '''Functia returneaza un string ce reprezinta un film
           Date de intrare:self-un film
           Return un string ce reprezinta un film
        '''
        return "Id_film: "+ str(self.get_id_film()) + "  Titlu: "+ self.get_titlu()+"  Descriere: "+ \
    self.get_descriere()+  "  Gen: " + self.get_gen() + "  Exemplare: "+ str(self.get_capacitate())

