
from exceptii.exceptii_entitati import ClientError,FilmError

class Validare_Client():
   
    def __init__(self):
        self.__lista_cnp=[]
   
    def validare_client(self,client):       
        
        '''
        Functia valideaza clientul
        Date de intrare: self-un validator de tip Validari
                         clien-un obiect de tip film
        Functia arunca exceptii de tipul ClientError daca nu trece de validare                 
        '''
        erori=""
        if(client.get_id_client()<=0):
            erori+="Id_client trebuie sa fie pozitiv!\n"
        if(client.get_nume()==""):
            erori+="Numele trebuie sa fie nevid!\n"
        if(len(client.get_cnp())!=13):
            erori+="Cnp ul trebuie sa aiba 13 cifre!\n"
        
        s=client.get_cnp()
        ok=True
        for c in s:
            if not(c>='0' and c<='9'):
                ok=False
                erori+="Cnp ul trebuie sa contina numai cifre!\n"
                break
        if ok==True and (s in self.__lista_cnp):
            erori+="Cnp ul trebuie sa fie unic!\n"
        else:
            self.__lista_cnp.append(s)
            
        if(len(erori)>0):
            raise ClientError(erori)

class Validare_Film:
       
    def validare_film(self,film):
        '''
        Functia valideaza filmul
        Date de intrare: self-un validator de tip Validari
                         film-un obiect de tip film
        Functia arunca exceptii de tipul FilmError daca nu trece de validare                 
        '''
        erori=""
        if(film.get_id_film()<=0):
            erori+="Id_film trebuie sa fie pozitiv!\n"
        if(film.get_titlu()==""):
            erori+="String titlu vid!\n"
        if(film.get_descriere()==""):
            erori+="String descriere vid!\n"
        if(film.get_gen()==""):
            erori+="String gen vid!\n"
        if(film.get_capacitate()<0):
            erori+="Numarul de exemplare btrebuie sa fie strict pozitiv!\n"
        if(len(erori)>0):
            raise FilmError(erori)

