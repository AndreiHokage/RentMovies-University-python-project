from domain.entities_film import Film
import string 
import random
from exceptii.exceptii_entitati import FilmError, RepositoryError_Film,\
    RepositoryError_Inchiriere

class ServiceFilm(object):
    
    def __init__(self,repository_film,repository_inchiriere,validator):
        self.__rep_film=repository_film
        self.__rep_inchiriere=repository_inchiriere
        self.__validator=validator 

    def upload(self):
        '''
        Functia incarca la sfarsitul executiei aplicatiei filmele in file 
        '''
        self.__rep_film.upload_to_file()
    
    def len_rep_film(self):
        '''
        Functia returneaza numarul de fimle pe care le are firma
        Date de intrare:self-servicefilm
        Return - un int ce reprezinta numarul de filme pe care le detine forima 
        '''
        return len(self.__rep_film)

    
    def adaugare(self, id_film, titlu, descriere, gen,nrexemplare):
        '''
        Functia adauga un film la firma de inchirieri
        Date de intrare:self-un servicefilm
                        id_film-un int ce reprezinta id ul filmului
                        titilu-un string ce reprez titilu filmului
                        descriere-un string ce reprez descrierea filmului
                        gen-un string ce reprezinta genul filmlui
        Return:-
        Functia arunca exceptii de tip FilmError daca nu trece de validare
        Functia arunca exceptii de tip RepositoryError_Film daca exista deja in repository  
        '''
        film=Film(id_film,titlu,descriere,gen,nrexemplare)
        self.__validator.validare_film(film)
        self.__rep_film.add(film)

    
    def find(self, id_film):
        '''
        Functia gasesgte un film ce i corespunde id ul id_film
        Date de intraer:self-un servocefilm
                        id_film-un int ce reprez id ul filmui
        Return: functia returneaza filmul ce i corespunde id ului dat
        Functia arunca exceptii de tip RepositoryError_Film daca filmul nu exista in firma
        '''
        return self.__rep_film.search(id_film)

    def search_nume(self,nume):
        '''
        Functia retuneaza o lista cu toate filmel cu numele nume
        Date de intrare:self-un service_film
                        nume-un string ce reprezinta un nume
        Return:ans-o ista cu filme
        '''
        ans=[]
        lista=self.__rep_film.get_all_film()
        for elem in lista:
            if(elem.get_titlu()==nume):
                ans.append(elem)
        return ans[:]
    
    def update(self, id_film, titlu, descriere, gen,nrexemplare):
        '''
        Functia updateaza un film la firma de inchirieri
        Date de intrare:self-un servicefilm
                        id_film-un int ce reprezinta id ul filmului
                        titilu-un string ce reprez titilu filmului
                        descriere-un string ce reprez descrierea filmului
                        gen-un string ce reprezinta genul filmlui
        Return:-
        Functia arunca exceptii de tip FilmError daca nu trece de validare
        Functia arunca exceptii de tip RepositoryError_Film daca nu exista in repository  
        '''
        film=Film(id_film,titlu,descriere,gen,nrexemplare)
        self.__validator.validare_film(film)
        self.__rep_film.update(film)

    
    def there_inchirieri_film(self,id_film):
        '''
        Functia verifica daca exista clienti ce au inchiriat filmul cu id ul id_film
        Date de intrare:self-un repository de inchirieri
                        id_film-un int ce reprezinta id ul filmului
        Return:1-daca se gaseste o inchiriere facuta de un client pt acel film,0 in caz contrar
        '''
        lista=self.__rep_inchiriere.FilmeInchiriateDeClienti()
        for elem in lista:
            if(elem.get_id_film()==id_film):
                return True;
        return False
    
    def remove(self, id_film):
        '''
        Functia sterge un film ce i corespunde id ul id_film
        Date de intraer:self-un servocefilm
                        id_film-un int ce reprez id ul filmui
        Return:-
        Functia arunca exceptii de tip RepositoryError_Film daca filmul nu exista in firma
        Functia arunca exceptii de tip RepositoryError_Inchiriere daca filmul a fost inchiriat de persoane
        '''
        if self.there_inchirieri_film(id_film) == True:
            raise RepositoryError_Inchiriere("Filmul nu poate fi sters deoarece exista clienti ce l-au inchiriat!\n")
        self.__rep_film.delete_film(id_film)
    
    
    def get_all_film(self):
        ''' 
           Functia da toate filmele de tip Film ale formei de inchiriat
           Date de intrare:un self-servicefilm
           Returneaza o lsta cu toate filmele 
        ''' 
        return self.__rep_film.get_all_film() 
    
    def generare_film(self,n):
        letters=string.ascii_lowercase 
        lg_id=self.len_rep_film()+n
        i=0
        while(i<n):
            try:
                lg_titlu=random.randint(6,10)
                lg_descriere=random.randint(4,6)
                lg_gen=random.randint(4,6)
                id_film=random.randint(1,lg_id)
                titlu=''.join(random.choice(letters) for j in range(0,lg_titlu))
                descriere=''.join(random.choice(letters) for j in range(0,lg_descriere))
                gen=''.join(random.choice(letters) for j in range(0,lg_gen))
                nrexemplare=random.randint(1,100)
                self.adaugare(id_film,titlu,descriere,gen,nrexemplare)
                i+=1
            except FilmError:
                continue
            except RepositoryError_Film:
                continue
               
    
    
    
    
    
        
    
        


