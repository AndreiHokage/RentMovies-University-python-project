'''
Created on Nov 7, 2020

@author: BalaniciAndrei
'''

#from testing.tests import Tests
from infracstutura.repository_film import Repository_Film
from infracstutura.repository_client import Repository_Client
from service.service_film import ServiceFilm
from service.service_client import ServiceClient
from ui.console import Console
from service.service_inchirieri import ServiceInchirieri
from infracstutura.repository_inchiriere import Repository_Inchiriere
from validari.validari_firma import Validare_Client, Validare_Film
from infracstutura.repository_client_file import Repository_Client_File
from infracstutura.repository_film_file import Repository_Film_File
from infracstutura.repository_inchiriere_file import Repository_Inchiriere_File



#test=Test()
#test.run_all_test()

valid_client=Validare_Client()   
valid_film=Validare_Film()            
rep_film=Repository_Film_File("film.txt")                                
rep_client=Repository_Client_File("client.txt")                             
rep_inchir=Repository_Inchiriere_File("inchiriere.txt")                                            
service_film=ServiceFilm(rep_film,rep_inchir,valid_film)                                 
service_client=ServiceClient(rep_client,rep_inchir,valid_client)                 
service_inchiriere=ServiceInchirieri(rep_client,rep_film,rep_inchir)                             
console=Console(service_client,service_film,service_inchiriere)                                              
console.run()
