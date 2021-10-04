'''
Created on Nov 9, 2020

@author: BalaniciAndrei
'''
from exceptii.exceptii_entitati import ClientError, RepositoryError_Client,\
    FilmError, RepositoryError_Film,RepositoryError_Inchiriere

class Console:
     
    def __init__(self,service_client,service_film,service_inchiriere):
        self.__srv_client=service_client
        self.__srv_film=service_film 
        self.__srv_inchiriere=service_inchiriere
        self.__initializare()
        
    def __add_client(self):
        try:
            id_client=int(input("Da ti id ul  client ului: "))
            nume=input("Da ti numele client ului: ")
            cnp=input("Da ti cnp ul clientuui: ")
            self.__srv_client.adaugare(id_client,nume,cnp)
            print("Clientul a fost adaugat cu succes!")
        except ValueError:
            print("Id ul trebuie sa fie numeric!\n")
        except ClientError as ce:
            print(ce)
        except RepositoryError_Client as re:
            print(re)
    
    def __remove_client(self):
        try:
            id_client=int(input("Da ti id ul client ului de eliminat: "))
            #self.__srv_inchiriere.returnare_client_filme(id_client)
            self.__srv_client.remove(id_client)
            print("Clientul a fost sters cu succes!")
        except ValueError:
            print("Id ul trebuie sa fie numeric!\n")
        except RepositoryError_Client as re:
            print(re)
        except RepositoryError_Inchiriere as re:
            print(re)
            
    def __update_client(self):
        try:
            id_client=int(input("Da ti id ul  client ului de updatat: "))
            nume=input("Da ti numele nou al client ului: ")
            cnp=input("Da ti cnp ul nou clientului: ")
            self.__srv_client.update(id_client,nume,cnp)
            print("Clientul a fost updatat cu succes!\n")
        except ValueError:
            print("Id ul trebuie sa fie numeric!\n")
        except RepositoryError_Client as re:
            print(re)
        except ClientError as ce:
            print(ce)
    
    def __find_client(self):
        try:
            id_client=int(input("Da ti id ul client ului: "))
            rez_client=self.__srv_client.find(id_client)
            print("Clientul a fodt gasit: ",rez_client)
        except ValueError:
            print("Id ul trebuie sa fie numeric!\n")
        except RepositoryError_Client as re:
            print(re)
    
    def __add_film(self):
        try:
            id_film=int(input("Da ti id ul film ului: "))
            titlu=input("Da ti titlul filmului: ")
            descriere=input("Da ti descrierea filmului: ")
            gen=input("Da ti genul filmului: ")
            nrexemplare=int(input("Da ti numarul de exemplare ale filmului: "))
            self.__srv_film.adaugare(id_film,titlu,descriere,gen,nrexemplare)
            print("Filmul a fost adugat cu succes!\n")
        except ValueError:
            print("Id ul si nr de exemplare ale filmului trebuie sa fie numerice!\n")
        except FilmError as fe:
            print(fe)
        except RepositoryError_Film as re:
            print(re)
    
    def __remove_film(self):
        try:
            id_film=int(input("Da ti id ul filmului de eliminat: "))
            #self.__srv_inchiriere.returnare_filme_client(id_film)
            self.__srv_film.remove(id_film)
            print("Filmul a fost sters cu succes!\n")
        except ValueError:
            print("Id ul filmului trebuie sa fie numeric!\n")
        except RepositoryError_Film as re:
            print(re)
        except RepositoryError_Inchiriere as re:
            print(re)
            
    def __update_film(self):
        try:
            id_film=int(input("Da ti id ul film ului de updatat: "))
            titlu=input("Da ti titlul filmului (nou): ")
            descriere=input("Da ti descrierea filmului (nou): ")
            gen=input("Da ti genul filmului (nou): ")
            nrexemplare=int(input("Da ti numarul de exemplare ale filmului(nou): "))
            self.__srv_film.update(id_film,titlu,descriere,gen,nrexemplare)
            print("Filul a fot updatat cu succes!\n")
        except ValueError:
            print("Id ul si nr de exemplare trebuie sa fie numerice!\n")
        except FilmError as fe:
            print(fe)
        except RepositoryError_Film as re:
            print(re)
            
    def __find_film(self):
        try:
            id_film=int(input("Da ti id ul fimului: "))
            rez_film=self.__srv_film.find(id_film) 
            print("Filmul a fost gasit: ",rez_film)
        except ValueError:
            print("Id ul trebuie sa fie numeric!\n")
        except RepositoryError_Film as re:
            print(re)
    
    def __inchiriere(self):
        try:
            id_client=int(input("Da ti id ul clientului care inchiriaza: "))
            id_film=int(input("Da ti id ul filmului inchiriat: "))
            self.__srv_inchiriere.inchiriere(id_client,id_film)
            print("Inchirerea filmului s a incheiat cu succes!\n")
        except ValueError:
            print("Id_film si Id_client trebuie sa fie numerice!\n")
        except RepositoryError_Client as re:
            print(re)
        except RepositoryError_Film as re:
            print(re)
        except RepositoryError_Inchiriere as re:
            print(re)
    
    def __returnare(self):
        try:
            id_client=int(input("Da ti id ul clientului care returneaza: "))
            id_film=int(input("Da ti id ul filmului ce se returneaza: "))
            self.__srv_inchiriere.returnare(id_client,id_film)
            print("Returnarea filmului s a incheiat cu succes!\n")
        except ValueError:
            print("Id_film si Id_client trebuie sa fie numerice!\n")
        except RepositoryError_Client as re:
            print(re)
        except RepositoryError_Film as re:
            print(re)
        except RepositoryError_Inchiriere as re:
            print(re) 
    
    def __eliminare_filme_client(self):
        try:
            id_client=int(input("Da ti id ul clientului pentru care se vor returna toate filmele: "))
            self.__srv_inchiriere.returnare_client_filme(id_client)
            print("Clientul a returnat toate filmele cu succes!\n")
        except ValueError:
            print("Id_client trebuie sa fie numeric!\n")
        except RepositoryError_Client as re:
            print(re)
    
    def __eliminare_clienti_film(self):
        try:
            id_film=int(input("Da ti id ul filmului pentru care toti clientii il returneaza: "))
            self.__srv_inchiriere.returnare_filme_client(id_film)
            print("Filmul a fost returnat de toti clientii!\n")
        except ValueError:
            print("Id_client trebuie sa fie numeric!\n")
        except RepositoryError_Film as re:
            print(re)
            
            
    def __afisare_filme_inchiriate(self):
        try:
            id_client=int(input("Da ti id ul clientului ce inchiriaza: "))
            ans=self.__srv_inchiriere.nr_filme_inchiriate(id_client)
            print("Clientul este: ")
            self.__afisare_client(id_client)
            print("Clientul a inchiriat " + str(ans) + " filme!\n")
            lista=self.__srv_inchiriere.get_list_filme_inchiriate(id_client)
            self.__afisare_lista_general_filme(lista)
        except ValueError:
            print("Id client trebuie sa fie pozitiv!\n")
        except RepositoryError_Client as re:
            print(re)
    
    def __afisare_clienti_inchiriati(self):
        try:
            id_film=int(input("Da ti id ul filmului ce a fost inchiriat: "))
            ans=self.__srv_inchiriere.nr_clienti_inchiriaza(id_film)
            print("Filmul este: ")
            self.__afisare_film(id_film) 
            print("Filmul a fost inchiriat de " + str(ans)+" persoane!\n")
            lista=self.__srv_inchiriere.get_list_clienti_inchiriati(id_film)
            self.__afisare_lista_general_client(lista)
        except ValueError:
            print("Id client trebuie sa fie pozitiv!\n")
        except RepositoryError_Film as re:
            print(re)
    
    def __afisare_lista_general_client(self,lista):
        if(len(lista)==0): 
            print(lista) 
        else:
            for x in lista:
                print(x)     
    
    def __afisare_lista_general_filme(self,lista):
        if(len(lista)==0): 
            print(lista) 
        else:
            for x in lista:
                print(x)    
    
    def __afisare_client(self,id_client):
        rez_client=self.__srv_client.find(id_client)
        print(rez_client)
    
    def __afisare_film(self,id_film):
        rez_film=self.__srv_film.find(id_film)
        print(rez_film)
            
    def __afisare_all_film(self):
        lista=self.__srv_film.get_all_film() 
        print("Lista de filme este: \n")
        if(len(lista)==0): print(lista) 
        else:
            for x in lista:
                print(x) 
        
            
    def __afisare_all_client(self):
        lista=self.__srv_client.get_all_client()
        print("Lista de clienti este: \n")
        if(len(lista)==0): print(lista)
        else:
            for x in lista:
                print(x) 
    
    def __search_by_name_client(self):
        nume=input("Da ti numele dupa care se va cauta clientii: ")
        ans=self.__srv_client.search_nume(nume)
        print("Lista de clienti este: ")
        if(len(ans)==0):
            print(ans)
        else:
            for x in ans:
                print(x)
            
    def __search_by_name_film(self):
        nume=input("Da ti numele dupa care se va cauta filme: ")
        ans=self.__srv_film.search_nume(nume)
        print("Lista de filme este: ")
        if(len(ans)==0):
            print(ans)
        else:
            for x in ans:
                print(x)
            
    
    def __generare_client(self):
        try:
            n=int(input("Introduceti nr de clienti generati: "))
            self.__srv_client.generare_client(n)
            print("S a generat cu succes cele "+str(n)+" persoane!\n")
        except ValueError:
            print("Nr inrodus trebuie sa fie numeric!\n")
    
    def __generare_film(self):
        try:
            n=int(input("Introduceti nr de filme generate: "))
            self.__srv_film.generare_film(n)
            print("S a generat cu succes cele "+str(n)+" filme!\n")
        except ValueError:
            print("Nr inrodus trebuie sa fie numeric!\n")
    
    def __sortare_filme_desc(self):
        rez=self.__srv_inchiriere.sortare_nr_filme()
        for elem in rez:
            print("Filmul: "+str(elem.get_id_film())+" "+elem.get_titlu()+" a fost inchiriat de: "+str(elem.get_nr_clienti())+" clienti!")
    
    def __sortare_clienti_partial(self):
        rez=self.__srv_inchiriere.sortare_clienti_partial()
        for elem in rez:
            print("Clientul: "+elem.get_nume()+" a inchiriat: "+ str(elem.get_nr_filme())+" filme!")
    
    def __sortare_clienti_nume(self):
        rez=self.__srv_inchiriere.sortare_clienti_nume()
        for elem in rez:
            print("Clientul: "+elem.get_nume()+" a inchiriat filme!")
    
    def __sortare_clienti_filme(self):
        rez=self.__srv_inchiriere.sortare_clienti_nr_filme()
        for elem in rez:
            print("Clietul: "+elem.get_nume()+ " a inchiriat "+str(elem.get_nr_filme())+" filme!")        
     
    def __sortare_clienti_gen_film(self):
        gen=input("Da ti genul filmului: ")
        rez=self.__srv_inchiriere.sortare_filme_gen(gen)
        print("Lista de clienti este: ")
        if(len(rez)==0):
            print(rez)
        else:
            for client in rez:
                print(client) 
     
    def __sortare_db_cmp(self):
        lista=self.__srv_inchiriere.sortare_criteriu_dublu()
        for x in lista: 
            print(x.get_nr_filme(),x.get_nume())
                
    def __setitem__(self,key,value1,value2):
        self.__dict[key]=[value1,value2]
        
    def __initializare(self):
        self.__dict={}
        self.__setitem__(1, self.__add_client, "1-Adaugare client!\n")
        self.__setitem__(2,self.__remove_client, "2-Stergere client!\n")
        self.__setitem__(3, self.__find_client, "3-Cautare client!\n")
        self.__setitem__(4, self.__update_client, "4-Updatare client!\n")
        self.__setitem__(5, self.__add_film, "5-Adaugare film!\n")
        self.__setitem__(6, self.__remove_film, "6-Stergere film!\n")
        self.__setitem__(7,self.__find_film, "7-Cautare film!\n")
        self.__setitem__(8, self.__update_film, "8-Updatare film!\n")
        self.__setitem__(9,self.__afisare_all_client, "9-Afisare toti clientii!\n")
        self.__setitem__(10, self.__afisare_all_film, "10-Afisare toate filmele!\n")
        self.__setitem__(11,self.__inchiriere,"11-Inchiriere filme!\n")
        self.__setitem__(12,self.__returnare,"12-Returnare filme!\n")
        self.__setitem__(13,self.__afisare_filme_inchiriate ,"13-Afisare filme inchiriate pentru un client dat!\n")
        self.__setitem__(14,self.__afisare_clienti_inchiriati ,"14-Afisare clienti pentru un film inchiriat dat!\n" )
        self.__setitem__(15,self.__eliminare_filme_client ,"15-Se returneaza toate filmele inchiriate de un client!\n")
        self.__setitem__(16,self.__eliminare_clienti_film, "16-Se elibereaza un anumit film de toate inchirierile!\n")
        self.__setitem__(17, self.__search_by_name_client, "17-Cauta clienti dupa nume dat!\n")
        self.__setitem__(18, self.__search_by_name_film, "18-Cauta filme dupa un nume dat!\n")
        self.__setitem__(19,self.__generare_client,"19-Generare clienti!\n")
        self.__setitem__(20, self.__generare_film, "20-Generare film!\n")
        self.__setitem__(21,self.__sortare_filme_desc,"21-Afisare filmele in ordinea descrescatoare dupa nr de clienti care le au inchiriat\n ")
        self.__setitem__(22,self.__sortare_clienti_partial,"22-Afisare primii 30% clienti cu cele mai multe filme!\n")
        self.__setitem__(23,self.__sortare_clienti_nume, "23-Afiseaza clientii cu filme inchiriate ordonati dupa nume!\n")
        self.__setitem__(24,self.__sortare_clienti_filme,"24-Afiseaza clientii cu filme inchiriate ordonati dupa nr de filme!\n")
        self.__setitem__(25,self.__sortare_clienti_gen_film,"25-Afiseaza clientii care nu au inchiriat filme dintr un gen dat!\n")
        self.__setitem__(26,self.__sortare_db_cmp,"26-Sortare dupa nr de filme si numele clientului!\n")
        self.__setitem__(27, 0, "27-Iesire din aplicatie!\n")
    
    def __read_comanda(self):
        for key in self.__dict.keys():
            print(self.__dict[key][1])
        return int(input("Da ti numarul comenzii: ").strip())
    
    
    def run(self):
        while True:
            try:
                cmd=self.__read_comanda()
                if(cmd==27):
                    self.__srv_film.upload()
                    break 
                try:
                    f=self.__dict[cmd][0]
                    f()
                except KeyError:
                    print("Comanda invalida!\n")
            except ValueError:
                print("Comanda trebuie sa fie numerica!\n") 
                
            input("\nPress Enter")      



            