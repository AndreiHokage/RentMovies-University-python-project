
from exceptii.exceptii_entitati import RepositoryError_Film

class Repository_Film(object):
    
    def __init__(self):
        self._elems=[]
        
    def __len__(self):
        '''
        Functia retuneaza lungimea listei de filme
        Date de intrare:self-un reposiroty de film
        Retunreaza:- un int ce reprezinta nr de filme din repositor_film
        '''
        return len(self._elems)
    
    def __adaugare(self,film):
        '''
        Functia adauga un nou film la lista de filme 
        Date de intrare:self-un repository_fim
                        film-un film de tip Film
        Return:-
        '''
        self._elems.append(film)
    
    def __stergere(self,idx):
        '''
        Functia sterge un film din lista de filme
        Date de intrare:self-un repository_film
                        idx-nr de ordine a filmului
        Retrn:-
        '''
        del self._elems[idx]
    
    def __get_film_from_list(self,idx):
        '''
        Funcria retuneaza un film cu nr de ordine specificat din repository
        Date de intrare:self-repositpry_film
                        idx-un numar de tip ind ce repreind indel
        Return -returneaza un film de tip Film
        '''
        return self._elems[idx] 

    def get_all_film(self):
        ''' 
           Functia da toate filmele de tip Film ale formei de inchiriat
           Date de intrare:self-repositoy_film
           Returneaza o lsta cu toate filmele 
        ''' 
        return self._elems   #atentie se va retuna cu adresa de memorie originala
    
    def add(self,film):
        '''
        Functia aduga un film in repository:
        Date de intrare:self-un repository de film
                        film -un fil de tip Film
        Return:-
        Functia ridica exceptii de tip RepositoryError_Film daca filmul exista deja
        '''
        if film in self._elems:
            raise RepositoryError_Film("Film existent")
        self.__adaugare(film)
    
    def search(self,film_id):
        '''
        Functia returneaza un film cu id ul film_id 
        Date de intrare:self-repository de film
                        film_id-un int ce reprezinta id ul uni film
        Return: un film De tip Dilm cu id ul id_film 
        Functia ridica exceptii de tip RepositorhError_film daca id ul este inexistent
        '''
        '''gasit=False
        for film in self._elems:
            if(film.get_id_film()==film_id):
                gasit=True
                break
                
        if gasit==False:
            raise RepositoryError_Film("Film inexistent")
        
        for elem in self._elems:
            if(elem.get_id_film()==film_id):
                return elem # se retuneaza atat valoare cat si adrsa de memorie spre atribuire'''
        
        return self.__search_recursiv(self._elems[:], film_id)
        
    def __search_recursiv(self,lista,id_film):
        if lista==[]:
            raise RepositoryError_Film("Film inexistent") 
        if lista[0].get_id_film()==id_film:
            return  lista[0] 
        return self.__search_recursiv(lista[1:], id_film)
    
    def update(self,film):
        '''
        Functia updateaza un film cu id ul film_id 
        Date de intrare:self-repository de film
                        film- un film de tip Film
        Return:- 
        Functia ridica exceptii de tip RepositorhError_film daca id ul este inexistent
        '''
        if film not in self._elems:
            raise RepositoryError_Film("Film inexistent")
        
        #atentie la updatare ca sa nu schimbi adresa locatie de memorie a elem din self.__elems
        for elem in self._elems:
            if(elem==film):
                elem.set_titlu(film.get_titlu())
                elem.set_descriere(film.get_descriere())
                elem.set_gen(film.get_gen())
                elem.set_capacitate(film.get_capacitate())
                return # si nu am modificat adresa loc de memorie 
    
    
    
    def delete_film(self,film_id):
        '''
        Functia sterge un film cu id ul film_id 
        Date de intrare:self-repository de film
                        film- un film de tip Film
        Return:- 
        Functia ridica exceptii de tip RepositorhError_film daca id ul este inexistent
        '''
        gasit=False
        for film in self._elems:
            if(film.get_id_film()==film_id):
                gasit=True
                
        if gasit==False:
            raise RepositoryError_Film("Film inexistent")
        
        for i in range(len(self)):
            elem=self.__get_film_from_list(i)
            if(elem.get_id_film()==film_id):
                self.__stergere(i)
                return
              
            

