'''
Created on Nov 28, 2020

@author: BalaniciAndrei
'''
from infracstutura.repository_inchiriere import Repository_Inchiriere
from exceptii.exceptii_entitati import RepositoryError_Inchiriere
from domain.DTO_RaportClient import RaportClient
from domain.DTO_ReportFilm import RaportFilm

class Repository_Inchiriere_File(Repository_Inchiriere):
    def __init__(self,filename):
        self.__filename=filename 
    
    
    def __len__(self):
        '''
        Functia returneaza numarul de ichirieri
        Date de intrare:self-un repository de ichiriereif
        Return: un int ce reprezinta numarul de inchirierie
        '''
        cnt=0
        with open(self.__filename) as f:
            for linie in f:
                if(linie.strip()==""):
                    continue 
                cnt+=1 
        return cnt
    
    def add(self,inchiriere):
        '''
        Functia aduaga o inchiriere in lista de inchirieri 
        Date de intrare:self-un repository de inchirieri
                        inchiriere-o inchiriere de tip Inchiriere
        Return:-
        Ridica exceptii de tip RepositoryError_Inchiriere daca inchirierea a fost gasita
        '''
        gasit=False
        try:
            self.find(inchiriere)
            gasit=True
        except RepositoryError_Inchiriere:
            with open(self.__filename,"a") as f:
                if inchiriere.get_film().get_capacitate()<1:
                    raise RepositoryError_Inchiriere("Nu mai exista exemplare de acest tip!\n")
                f.write(str(inchiriere.get_client().get_id_client())+";"+str(inchiriere.get_film().get_id_film()))
                f.write("\n")
                inchiriere.get_film().take_capacitate_unit()
        
        if gasit==True:
            raise RepositoryError_Inchiriere("Clientul a inchiriat deja filmul!\n")
    
    def __storetofile(self,lista):
        '''
        Stocheaza lista de ichirieri in fisier
        '''
        with open(self.__filename,"w") as f:
            for elem in lista:
                linie=str(elem[0])+";"+str(elem[1])
                f.write(linie)
                f.write("\n")
                
    def remove2(self,inchiriere):
        '''
        Functia stereg o inchiriere in lista de inchirieri
        Date de intrare:self-un repository de inchirieri
                        inchiriere-o inchiriere de tip Inchiriere
        Return:-
        Ridica exceptii de tip RepositoryError_Inchiriere daca inchirierea nu a fost gasit
        ''' 
        self.find(inchiriere)
        rez=[]
        with open(self.__filename) as f:
            for linie in f:
                if linie.strip()=="":
                    continue
                atrb=linie.split(";")
                client_id=int(atrb[0])
                film_id=int(atrb[1])
                if(client_id==inchiriere.get_client().get_id_client() and film_id==inchiriere.get_film().get_id_film()):
                    inchiriere.get_film().get_capacitate_unit()
                    continue 
                rez.append([client_id,film_id])
                
        self.__storetofile(rez)
            
    def remove(self,inchiriere):
        self.find(inchiriere)
        g=open("inchir_aux.txt","w")
        with open(self.__filename) as f:
            for linie in f:
                if linie.strip()=="":
                    continue 
                atrb=linie.split(";")
                client_id=int(atrb[0])
                film_id=int(atrb[1])
                if(client_id==inchiriere.get_client().get_id_client() and film_id==inchiriere.get_film().get_id_film()):
                    inchiriere.get_film().get_capacitate_unit()
                    continue
                g.write(linie)
                #g.write("\n")
        g.close()
        g=open("inchir_aux.txt","r")
        with open(self.__filename,"w"): 
            f=open(self.__filename,"w")
            for linie in g:
                f.write(linie)
        g.close()
        f.close()
            
        
    def find(self,inchiriere):
        '''
        Functia gaseste o inchiriere in lista de inchirieri
        Date de intrare:self-un repository de inchirieri
                        inchiriere-o inchiriere de tip Inchiriere
        Return:o inchiriere de tip Inchiriere 
        Ridica exceptii de tip RepositoryError_Inchiriere daca inchirierea nu a fost gasit
        
        '''
        with open(self.__filename) as f:
            for line in f:
                if line.strip()=="":
                    continue
                atrb=line.split(";")
                client_id=int(atrb[0])
                film_id=int(atrb[1])
                if(client_id==inchiriere.get_client().get_id_client() and film_id==inchiriere.get_film().get_id_film()):
                    return inchiriere 
        raise RepositoryError_Inchiriere("Nu exista o astfel de inchiriere!\n") 
    
    def get_all(self):
        rez=[]
        with open(self.__filename) as f:
            for line in f:
                if line.strip()=="": 
                    continue
                atrb=line.split(";")
                client_id=int(atrb[0])
                film_id=int(atrb[1])
                rez.append([client_id,film_id])
        return rez
        
    def ClientiCuFilmeInchiriate(self):
        '''
        Functia contriueste o lista de obiecte de tip RaportClient
        Date de intrare:self-un service de inchirierir
        Return-o lista de obiecte RaportClient
        '''
        dictCF={}
        with open(self.__filename) as f:
            for linie in f:
                if linie.strip()=="":
                    continue
                atrb=linie.split(";")
                id_client=int(atrb[0])
                id_film=int(atrb[1])
                if id_client in dictCF.keys():
                    dictCF[id_client].inc()
                else:
                    dictCF[id_client]=RaportClient(id_client,1)
                dictCF[id_client].add_film(id_film)
        ans=list(dictCF.values())
        return ans
                
    def FilmeInchiriateDeClienti(self):
        '''
        Functia construieste o lista de obiecte de tip RaportFilm
        Date de intrare:self-un service de inchirierir
        Return-o lista de obiecte RaportFilm 
        '''
        dictCF={}
        with open(self.__filename) as f:
            for linie in f:
                if linie.strip()=="":
                    continue 
                atrb=linie.split(";")
                id_film=int(atrb[1])
                id_client=int(atrb[0])
                if id_film in dictCF.keys():
                    dictCF[id_film].inc()
                else:
                    dictCF[id_film]=RaportFilm(id_film,1)  
                dictCF[id_film].add_client(id_client)          
        ans=list(dictCF.values())
        return ans
    
    