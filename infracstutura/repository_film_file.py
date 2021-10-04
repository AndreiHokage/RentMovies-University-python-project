'''
Created on Nov 28, 2020

@author: BalaniciAndrei
'''
from infracstutura.repository_film import Repository_Film
from domain.entities_film import Film

class Repository_Film_File(Repository_Film):
    
    def __init__(self,filename):
        Repository_Film.__init__(self)
        self.__file_name=filename 
        self.__loadfromfile()
        
    def __loadfromfile(self):
        '''
        Functia incarca in memorie toatre filele din fisier
        '''
        self._elems=[]
        with open(self.__file_name) as f:
            for line in f:
                if line.strip()=="":
                    continue
                atrb=line.split(";")
                film=Film(int(atrb[0]),atrb[1],atrb[2],atrb[3],int(atrb[4]))
                self._elems.append(film) 
                
    def __storetofile(self):
        '''
        Functia incarca in fisier filmelle din repository_film
        '''
        with open(self.__file_name,"w") as f:
            for film in self._elems:
                linie=str(film.get_id_film())+";"+film.get_titlu()+";"+film.get_descriere()+";"
                linie=linie+film.get_gen()+";"+str(film.get_capacitate())
                f.write(linie)
                f.write("\n")
                
    def upload_to_file(self):
        '''
        Functia incarca tot continutul filmelor din memorie in fisier dupa modificarile suferite la inchirieri
        '''
        self.__storetofile()
                
    def add(self,film):
        '''
        Functia aduga un film in repository:
        Date de intrare:self-un repository de film
                        film -un fil de tip Film
        Return:-
        Functia ridica exceptii de tip RepositoryError_Film daca filmul exista deja
        '''
       # self.__loadfromfile()
        Repository_Film.add(self, film)
        self.__storetofile()
        
    def update(self,film):
        '''
        Functia updateaza un film cu id ul film_id 
        Date de intrare:self-repository de film
                        film- un film de tip Film
        Return:- 
        Functia ridica exceptii de tip RepositorhError_film daca id ul este inexistent
        '''
        #self.__loadfromfile()
        Repository_Film.update(self, film)
        self.__storetofile()
    
    def delete_film(self,film_id):
        '''
        Functia sterge un film cu id ul film_id 
        Date de intrare:self-repository de film
                        film- un film de tip Film
        Return:- 
        Functia ridica exceptii de tip RepositorhError_film daca id ul este inexistent
        ''' 
        #self.__loadfromfile()
        Repository_Film.delete_film(self, film_id)
        self.__storetofile()    
        
    def search(self, film_id):
        #self.__loadfromfile()
        return Repository_Film.search(self, film_id)    
        
    def get_all_film(self):
        #self.__loadfromfile()
        return Repository_Film.get_all_film(self)
        