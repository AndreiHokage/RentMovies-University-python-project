
from domain.entities_client import Client
from domain.entities_film import Film
from exceptii.exceptii_entitati import ClientError,RepositoryError_Client,FilmError,RepositoryError_Film,\
     RepositoryError_Inchiriere
from validari.validari_firma import Validare_Client, Validare_Film
from infracstutura.repository_client import Repository_Client
from infracstutura.repository_film import Repository_Film
from service.service_client import ServiceClient
from service.service_film import ServiceFilm
from service.service_inchirieri import ServiceInchirieri
from domain.inchiriere import Inchiriere
from infracstutura.repository_inchiriere import Repository_Inchiriere
from infracstutura.repository_client_file import Repository_Client_File
from infracstutura.repository_film_file import Repository_Film_File
from infracstutura.repository_inchiriere_file import Repository_Inchiriere_File


import unittest
from Metode_de_sortare import Sortari
from domain.DTO_RaportClient import RaportClient
    
class Test_domain_entities_client(unittest.TestCase):

    def setUp(self):
        id_client=12
        nume="Fanica"
        cnp="1000123456789"
        self.__client=Client(id_client,nume,cnp)
        self.__client1=Client(12,"Andrei",cnp)

    def tearDown(self):
        unittest.TestCase.tearDown(self)
        

    def test_domain_entities_client_test(self):
        self.assertEqual(12,self.__client1.get_id_client(),"Id ul clientului este 12")
        #assert self.__client.get_id_client()==12
        self.assertEqual("Fanica",self.__client.get_nume(),"Numele trebuie sa fie Fanica")
        #assert client.get_nume()=="Fanica"
        
        #assert client.get_cnp()=="1000123456789"
        self.assertEqual("1000123456789", self.__client.get_cnp(), "Cnpul trebe sa fie 1000123456789")
        #assert client1==client
        self.assertEqual(self.__client, self.__client1, "Clientii trebe sa fie egali")
        #assert str(client)=="Id:12  Nume:Fanica  Cnp:1000123456789"
        self.assertEqual("Id:12  Nume:Fanica  Cnp:1000123456789", str(self.__client), "Se verifica mesajul")


class Test_validare_client(unittest.TestCase):

    def setUp(self):
        self.__validator=Validare_Client()

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def test_validare_client(self):
    
        client=Client(-12,"","2331")
        self.assertRaisesRegex(ClientError,"Id_client trebuie sa fie pozitiv!\nNumele trebuie sa fie nevid!\nCnp ul trebuie sa aiba 13 cifre!\n",self.__validator.validare_client,client)
        
        client1=Client(12,"","1000123456789")  
        self.assertRaisesRegex(ClientError,"Numele trebuie sa fie nevid!\n",self.__validator.validare_client,client1)
 
        #client2=Client(12,"Andrei","1000123456989")
        #self.assertRaises(,self.__validator.validare_client,client2)
    
        client2=Client(12,"Andrei","100hfg1j345678")
        self.assertRaisesRegex(ClientError,"Cnp ul trebuie sa aiba 13 cifre!\nCnp ul trebuie sa contina numai cifre!\n",self.__validator.validare_client,client2)


class Test_repository_client(unittest.TestCase):

    def setUp(self):
        with open("client_test.txt","w"):
                pass
        self.__stoc_clienti=Repository_Client_File("client_test.txt")

    def tearDown(self):
        with open("client_test.txt","w"):
                pass

    def test_repository_client(self):
        
        self.assertEqual(0, len(self.__stoc_clienti), "Se calculeaza nr de clienti")
        
        client=Client(12,"Andrei","1000123456789")   
        self.__stoc_clienti.add(client)
        self.assertEqual(1, len(self.__stoc_clienti), "Se calculeaza nr de clienit")
        
        
        client_result=self.__stoc_clienti.search(client.get_id_client())
        self.assertEqual(12,client_result.get_id_client() )
        self.assertEqual("Andrei",client_result.get_nume() )
        self.assertEqual("1000123456789",client_result.get_cnp() )
        
        client=Client(10,"Fanica","1000123456788")
        self.assertRaisesRegex(RepositoryError_Client,"Clientul nu se afla in lista de clienti!\n",self.__stoc_clienti.search,client.get_id_client())
        
        client=Client(12,"Fanica","1000123456788")
        self.assertRaisesRegex(RepositoryError_Client,"Clientul se afla deja in lista de clienti!\n",self.__stoc_clienti.add,client)
            
        client=Client(13,"Fanica","1000123456788")
        self.__stoc_clienti.add(client)
        self.assertEqual(2,len(self.__stoc_clienti))
        
        client=Client(14,"YuhikoNagato","1111111111111")
        self.assertRaisesRegex(RepositoryError_Client,"Clientul nu se afla in lista de clienti!\n",self.__stoc_clienti.update,client)
        
        self.__stoc_clienti.add(client)
        self.assertEqual(3,len(self.__stoc_clienti))
        
        client1=Client(14,"Yuhiko","1111111111111")
        self.__stoc_clienti.update(client1)
        client_result=self.__stoc_clienti.search(client1.get_id_client())
        self.assertEqual(3,len(self.__stoc_clienti))
        self.assertEqual("Yuhiko",client_result.get_nume())
        self.assertEqual("1111111111111",client_result.get_cnp())
    
        
        client=Client(11,"Igor","2222222222222")
        self.assertRaisesRegex(RepositoryError_Client,"Clientul nu se afla in lista de clienti!\n",self.__stoc_clienti.delete_client,client.get_id_client())
        
        self.__stoc_clienti.add(client)
        self.assertEqual(4,len(self.__stoc_clienti))
        self.__stoc_clienti.delete_client(client.get_id_client())
        self.assertEqual(3,len(self.__stoc_clienti))
        self.assertRaisesRegex(RepositoryError_Client,"Clientul nu se afla in lista de clienti!\n",self.__stoc_clienti.delete_client,client.get_id_client() )
 
    def test_add_client_black_box(self):
        self.assertEqual(0,len(self.__stoc_clienti))
        client=Client(21,"Andrei","6020706226789")
        self.__stoc_clienti.add(client)
        self.assertEqual(1,len(self.__stoc_clienti))
        client=Client(22,"Andrei","6070706226789")
        self.__stoc_clienti.add(client)
        self.assertEqual(2,len(self.__stoc_clienti))
        client=Client(21,"Andrei","1237062267892")
        self.assertRaisesRegex(RepositoryError_Client,"Clientul se afla deja in lista de clienti!\n",self.__stoc_clienti.add,client)

class Test_domain_entities_film(unittest.TestCase):

    def setUp(self):
        self.__id_film=10
        self.__titlu="Naruto"
        self.__descriere="batai"
        self.__gen="familie"
        self.__capacitate=2
        self.__film=Film(self.__id_film,self.__titlu,self.__descriere,self.__gen,self.__capacitate)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def test_entities_film(self):
        
        self.assertEqual(10, self.__film.get_id_film())
        self.assertEqual("Naruto", self.__film.get_titlu(),)
        self.assertEqual("batai",self.__film.get_descriere())
        self.assertEqual("familie",self.__film.get_gen())
        self.assertEqual(2,self.__film.get_capacitate(), )
        film1=Film(10,"Nagato","shoturi","crima",40)
        self.assertEqual(film1, self.__film)
        self.assertEqual(str(self.__film), "Id_film: 10  Titlu: Naruto  Descriere: batai  Gen: familie  Exemplare: 2")


class Test_validare_film(unittest.TestCase):

    def setUp(self):
        self.__validator=Validare_Film()

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def test_validare_film(self):
        film=Film(-10,"","","",0)
        self.assertRaisesRegex(FilmError,"Id_film trebuie sa fie pozitiv!\nString titlu vid!\nString descriere vid!\nString gen vid!\n" ,self.__validator.validare_film,film)
        
        film=Film(100,"","karate","",-50)
        self.assertRaisesRegex(FilmError,"String titlu vid!\nString gen vid!\nNumarul de exemplare btrebuie sa fie strict pozitiv!\n",self.__validator.validare_film,film)
        
        film=Film(10,"Nagato","shoturi","crima",2)
        try:
            self.__validator.validare_film(film)
            self.assertTrue(True)
        except FilmError:
            self.assertTrue(False)



class Test_repository_film(unittest.TestCase):

    def setUp(self):
        with open("filmtest.txt","w"):
            pass
        self.__stoc_filme=Repository_Film_File("filmtest.txt")

    def tearDown(self):
        with open("filmtest.txt","w"):
            pass

    def test_repository_film(self):
        self.assertEqual(0,len(self.__stoc_filme))         
        
        film=Film(10,"naruto","batai","familie",50)
        self.__stoc_filme.add(film)
        self.assertEqual(1,len(self.__stoc_filme)) 
        
        film1=Film(10,"yagoto","batai","crime",60)
        self.assertRaisesRegex(RepositoryError_Film,"Film existent",self.__stoc_filme.add,film1)
        
        film_rez=self.__stoc_filme.search(film.get_id_film())
        self.assertEqual(10, film_rez.get_id_film())
        self.assertEqual("batai", film_rez.get_descriere())
        self.assertEqual("familie", film_rez.get_gen())
        self.assertEqual(50, film_rez.get_capacitate())
        
        film=Film(12,"minato","hokage","horror",70)
        self.assertRaisesRegex(RepositoryError_Film,"Film inexistent",self.__stoc_filme.search,film.get_id_film())
        
        self.__stoc_filme.add(film)
        self.assertEqual(2,len(self.__stoc_filme)) 
        film_rez=self.__stoc_filme.search(film.get_id_film())
        self.assertEqual(12, film_rez.get_id_film())
        self.assertEqual("hokage", film_rez.get_descriere())
        self.assertEqual("horror", film_rez.get_gen())
        self.assertEqual(70, film_rez.get_capacitate())
        self.assertEqual("minato",film_rez.get_titlu())
        
        film=Film(13,"tobirama","war","comedie",80)
        self.assertRaisesRegex(RepositoryError_Film,"Film inexistent",self.__stoc_filme.update,film)
            
        self.__stoc_filme.add(film)
        film=Film(13,"hasirama","peace","drama",90)
        self.__stoc_filme.update(film)
        film_rez=self.__stoc_filme.search(film.get_id_film())
        self.assertEqual(13, film_rez.get_id_film())
        self.assertEqual("peace", film_rez.get_descriere())
        self.assertEqual("drama", film_rez.get_gen())
        self.assertEqual(90, film_rez.get_capacitate())
        self.assertEqual("hasirama",film_rez.get_titlu())
        
        film=Film(14,"boruto","hasiramas cell","drama",100)
        self.assertRaisesRegex(RepositoryError_Film,"Film inexistent",self.__stoc_filme.delete_film,film.get_id_film())
      
        
        self.__stoc_filme.add(film)
        self.assertEqual(4,len(self.__stoc_filme))
        self.__stoc_filme.delete_film(film.get_id_film())
        self.assertEqual(3,len(self.__stoc_filme))
        
        self.assertRaisesRegex(RepositoryError_Film,"Film inexistent",self.__stoc_filme.delete_film,film.get_id_film())     


class Test_service_client(unittest.TestCase):

    def setUp(self):
        with open("client_test.txt","w"):
            pass
        self.__rep_client=Repository_Client_File("client_test.txt")
        self.__rep_inchirieri=Repository_Inchiriere()
        self.__validator=Validare_Client()
        self.__service=ServiceClient(self.__rep_client,self.__rep_inchirieri,self.__validator)

    def tearDown(self):
        with open("client_test.txt","w"):
            pass

    def test_service_client(self):
        self.__service.adaugare(12,"hazuma","1111111111111")
        self.assertEqual(1, self.__service.len_rep_client())
        
        rez_client=self.__service.find(12)
        self.assertEqual("1111111111111",rez_client.get_cnp())
        self.assertEqual("hazuma",rez_client.get_nume() )
        self.assertRaisesRegex(RepositoryError_Client,"Clientul se afla deja in lista de clienti!\n" ,self.__service.adaugare,12,"jiraya","2222222222222")
        
        self.__service.update(12,"jiraya","1234567891234")
        rez_client=self.__service.find(12)
        self.assertEqual("1234567891234",rez_client.get_cnp())
        self.assertEqual("jiraya",rez_client.get_nume() )
        self.assertEqual(1, self.__service.len_rep_client())
        
        lista=self.__service.get_all_client()
        self.assertEqual(1,len(lista))
        self.assertRaisesRegex(RepositoryError_Client,"Clientul nu se afla in lista de clienti!\n",self.__service.update,13,"sasuke","1010101010111")
        
        self.__service.remove(12)
        self.assertEqual(0, self.__service.len_rep_client())
        self.__service.adaugare(12,"sakura","9999999999999")
        self.assertRaisesRegex(RepositoryError_Client,"Clientul nu se afla in lista de clienti!\n",self.__service.remove,13) 
            


class Test_service_film(unittest.TestCase):

    def setUp(self):
        with open("filmtest.txt","w"):
            pass
        self.__rep_film=Repository_Film_File("filmtest.txt")
        self.__validator=Validare_Film()
        self.__rep_inchirieri=Repository_Inchiriere()
        self.__service_film=ServiceFilm(self.__rep_film,self.__rep_inchirieri,self.__validator)

    def tearDown(self):
        with open("filmtest.txt","w"):
            pass

    def test_service_film(self):
        self.assertEqual(0,self.__service_film.len_rep_film())
                
        self.__service_film.adaugare(12,"Oblivion","sakura","familie",43)
        rez_film=self.__service_film.find(12)
        self.assertEqual("Oblivion",rez_film.get_titlu())
        self.assertEqual("sakura",rez_film.get_descriere())
        self.assertEqual(43,rez_film.get_capacitate())
        self.assertEqual("familie",rez_film.get_gen())
        self.assertEqual(1,self.__service_film.len_rep_film())
        
        self.__service_film.adaugare(11,"Kaguya","sakura","crima",3)
        self.assertEqual(2,self.__service_film.len_rep_film()) 
        
        self.assertRaisesRegex(RepositoryError_Film,"Film existent",self.__service_film.adaugare,12,"Oblivion","sakura","familie",45)
        self.assertRaisesRegex(RepositoryError_Film,"Film inexistent",self.__service_film.find,13)
            
        self.__service_film.update(12,"Naruto","sasuke","familie",50)
        rez_film=self.__service_film.find(12)
        self.assertEqual("Naruto",rez_film.get_titlu())
        self.assertEqual("sasuke",rez_film.get_descriere())
        self.assertEqual(50,rez_film.get_capacitate())
        self.assertEqual("familie",rez_film.get_gen())
        self.assertEqual(2,self.__service_film.len_rep_film())
        
        lista=self.__service_film.get_all_film()
        self.assertEqual(2, len(lista))
        self.assertRaisesRegex(RepositoryError_Film,"Film inexistent",self.__service_film.update,9,"DS","dsf","d",45)
            
        self.__service_film.remove(12)
        self.assertEqual(1,self.__service_film.len_rep_film())
        self.assertRaisesRegex(RepositoryError_Film,"Film inexistent",self.__service_film.find,12)   


class Test_creeaza_inchiriere(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_creeaza_inchiriere(self):
        client1=Client(1,"Andrei","2223334567897")
        film2=Film(2,"Konoha","hj","familie",4)
        inchir=Inchiriere(client1,film2)
        self.assertEqual(client1,inchir.get_client() )
        self.assertEqual(film2,inchir.get_film() )
        inchir2=Inchiriere(client1,film2)
        self.assertEqual(inchir,inchir2)


class Test_rep_inchir(unittest.TestCase):

    def setUp(self):
        with open("inchiriere_test.txt","w"):
            pass
        self.__client1=Client(1,"Andrei","2223334567897")
        self.__client2=Client(2,"Cristian","2313213423421")
        self.__client3=Client(3,"Fantoma","9856409870876")
        self.__film1=Film(1,"Oblivion","fsf","crima",3)
        self.__film2=Film(2,"Konoha","hj","familie",4)
        self.__film3=Film(3,"Bakugan","DGv","comedie",1) 
        
        self.__rep_inchir=Repository_Inchiriere_File("inchiriere_test.txt")

    def tearDown(self):
        with open("inchiriere_test.txt","w"):
            pass

    def test_repository_inchir(self):
        self.assertEqual(0, len(self.__rep_inchir))
        inchir1=Inchiriere(self.__client1,self.__film1)
        inchir2=Inchiriere(self.__client1,self.__film2)
        self.__rep_inchir.add(inchir1)
        self.__rep_inchir.add(inchir2)
        self.assertEqual(2, len(self.__rep_inchir))
        
        rez_inchir=self.__rep_inchir.find(inchir1)
        self.assertEqual(inchir1.get_client(), rez_inchir.get_client())
        self.assertEqual(inchir1.get_film(), rez_inchir.get_film())
        self.assertRaisesRegex(RepositoryError_Inchiriere,"Nu exista o astfel de inchiriere!\n",self.__rep_inchir.find,Inchiriere(self.__client3,self.__film3))
        self.assertRaisesRegex(RepositoryError_Inchiriere,"Clientul a inchiriat deja filmul!\n",self.__rep_inchir.add,inchir1)
            
        inchir2=Inchiriere(self.__client1,self.__film3)
        self.__rep_inchir.add(inchir2)
        self.assertEqual(0,inchir2.get_film().get_capacitate())
        self.assertRaisesRegex(RepositoryError_Inchiriere,"Nu mai exista exemplare de acest tip!\n",self.__rep_inchir.add,Inchiriere(self.__client2,self.__film3))

        self.assertEqual(3, len(self.__rep_inchir))     
        self.__rep_inchir.remove(inchir2)
        self.assertEqual(2, len(self.__rep_inchir)) 
        self.assertEqual(1, inchir2.get_film().get_capacitate())
        self.assertRaisesRegex(RepositoryError_Inchiriere,"Nu exista o astfel de inchiriere!\n",self.__rep_inchir.remove,Inchiriere(self.__client1,self.__film3))


class Test_service_inchirieri(unittest.TestCase):

    def setUp(self):
        with open("client_test.txt","w"):
            pass 
        with open("filmtest.txt","w"):
            pass
        with open("inchiriere_test.txt","w"):
            pass
        self.__client1=Client(1,"Andrei","2223334567897")
        self.__client2=Client(2,"Cristian","2313213423421")
        self.__client3=Client(3,"Fantoma","9856409870876")
        self.__film1=Film(1,"Oblivion","fsf","crima",3)
        self.__film2=Film(2,"Konoha","hj","familie",4)
        self.__film3=Film(3,"Bakugan","DGv","comedie",2)
        self.__valid=Validare_Film()
        self.__rep_client=Repository_Client_File("client_test.txt")
        self.__rep_client.add(self.__client1)
        self.__rep_client.add(self.__client2)
        self.__rep_client.add(self.__client3)
        
        self.__rep_film=Repository_Film_File("filmtest.txt")
        self.__rep_film.add(self.__film1)
        self.__rep_film.add(self.__film2)
        self.__rep_film.add(self.__film3)
        
        self.__rep_inchir=Repository_Inchiriere_File("inchiriere_test.txt")
        self.__srv_client=ServiceClient(self.__rep_client,self.__rep_inchir,self.__valid)
        self.__srv_film=ServiceFilm(self.__rep_film,self.__rep_inchir,self.__valid)
        self.__serv_inchirieri=ServiceInchirieri(self.__rep_client,self.__rep_film,self.__rep_inchir)

    def tearDown(self):
        with open("client_test.txt","w"):
            pass 
        with open("filmtest.txt","w"):
            pass
        with open("inchiriere_test.txt","w"):
            pass

    def test_service_inchirieri(self):
        self.__serv_inchirieri.inchiriere(1,3)
        film=self.__rep_film.search(3)
        self.assertEqual(1,film.get_capacitate())
        self.assertEqual(1,self.__serv_inchirieri.nr_filme_inchiriate(1))
        self.assertRaisesRegex(RepositoryError_Inchiriere,"Clientul a inchiriat deja filmul!\n",self.__serv_inchirieri.inchiriere,1,3)
        self.__serv_inchirieri.inchiriere(2,3)
        self.__serv_inchirieri.inchiriere(3,1)
        
        rez_film=self.__serv_inchirieri.find_film(2, 3)
        self.assertEqual(rez_film,self.__film3)
        self.assertRaisesRegex(RepositoryError_Inchiriere,"Nu exista o astfel de inchiriere!\n",self.__serv_inchirieri.find_film,3,2)
            
        rez_film=self.__serv_inchirieri.find_film(3, 1)
        self.assertEqual(rez_film,self.__film1)
        self.assertRaisesRegex(RepositoryError_Film,"Film inexistent",self.__serv_inchirieri.inchiriere,3,4) 
        
        self.__serv_inchirieri.inchiriere(3,2)
        self.__serv_inchirieri.inchiriere(2,2)  
        
        self.assertEqual(1,self.__serv_inchirieri.nr_filme_inchiriate(1))
        self.assertEqual(2,self.__serv_inchirieri.nr_filme_inchiriate(2))
        self.assertEqual(2,self.__serv_inchirieri.nr_clienti_inchiriaza(3))
        self.assertEqual(2,self.__serv_inchirieri.nr_clienti_inchiriaza(2))
        self.assertEqual(1,self.__serv_inchirieri.nr_clienti_inchiriaza(1))

        self.__serv_inchirieri.returnare(1,3)
        self.__serv_inchirieri.returnare(2,3)
        self.assertEqual(2,self.__film3.get_capacitate())
        self.assertEqual(0,self.__serv_inchirieri.nr_clienti_inchiriaza(3))
        self.assertEqual(1,self.__serv_inchirieri.nr_clienti_inchiriaza(1))
        self.assertEqual(2,self.__serv_inchirieri.nr_clienti_inchiriaza(2))
        self.assertRaisesRegex(RepositoryError_Client,"Clientul nu se afla in lista de clienti!\n",self.__serv_inchirieri.nr_filme_inchiriate,7)
        self.assertRaisesRegex(RepositoryError_Inchiriere,"Nu exista o astfel de inchiriere!\n",self.__serv_inchirieri.returnare,2,1)
        film=self.__rep_film.search(1)
        self.assertEqual(2,film.get_capacitate())
        
            
        self.__serv_inchirieri.returnare(3,1)
        self.assertEqual(3,self.__film1.get_capacitate())
        
        self.__serv_inchirieri.returnare_client_filme(1)
        self.__serv_inchirieri.returnare_client_filme(2)
        self.__serv_inchirieri.returnare_client_filme(3)
        
        self.assertEqual(3,self.__film1.get_capacitate())
        self.assertEqual(4,self.__film2.get_capacitate())
        self.assertEqual(2,self.__film3.get_capacitate())

        
        self.__serv_inchirieri.inchiriere(1, 1)
        self.__serv_inchirieri.inchiriere(2,1)
        self.__serv_inchirieri.inchiriere(3,1)
        film=self.__rep_film.search(1)
        self.assertEqual(0,film.get_capacitate())
        
        self.__serv_inchirieri.inchiriere(1,2)
        self.__serv_inchirieri.inchiriere(2,2)
        film=self.__rep_film.search(2)
        self.assertEqual(2,film.get_capacitate())
        
        self.__serv_inchirieri.returnare_filme_client(1)
        film=self.__rep_film.search(1)
        self.assertEqual(3,film.get_capacitate())
      
        self.__serv_inchirieri.returnare_client_filme(2)
        film=self.__rep_film.search(2)
        self.assertEqual(3,film.get_capacitate())
               
    def test_raport_general(self):
        self.__serv_inchirieri.inchiriere(1,1)
        self.__serv_inchirieri.inchiriere(1,3)
        rez=self.__rep_inchir.ClientiCuFilmeInchiriate()
        self.__serv_inchirieri.set_names_clienti(rez)
        self.assertEqual(1, len(rez))
        self.assertEqual("Andrei", rez[0].get_nume())
        self.assertEqual(2, rez[0].get_nr_filme())
        
        self.__serv_inchirieri.inchiriere(2,1)
        self.__serv_inchirieri.inchiriere(2,3)
        self.__serv_inchirieri.inchiriere(2,2)
        rez=self.__rep_inchir.ClientiCuFilmeInchiriate()
        self.__serv_inchirieri.set_names_clienti(rez)
        self.assertEqual(2, len(rez))
        self.assertEqual("Andrei", rez[0].get_nume())
        self.assertEqual(2, rez[0].get_nr_filme())
        self.assertEqual("Cristian", rez[1].get_nume())
        self.assertEqual(3, rez[1].get_nr_filme())   
    
    def test_sortare_nume(self):
        self.__serv_inchirieri.inchiriere(1,1)
        rez=self.__serv_inchirieri.sortare_clienti_nume()
        self.assertEqual(1, len(rez))
        self.assertEqual("Andrei", rez[0].get_nume())
        self.__serv_inchirieri.inchiriere(2,2)
        rez=self.__serv_inchirieri.sortare_clienti_nume()
        self.assertEqual(2, len(rez))
        self.assertEqual("Andrei",rez[0].get_nume())
        self.assertEqual("Cristian",rez[1].get_nume())
        self.__serv_inchirieri.inchiriere(3,1)
        rez=self.__serv_inchirieri.sortare_clienti_nume()
        self.assertEqual(3, len(rez))
        self.assertEqual("Cristian", rez[1].get_nume())
        self.assertEqual("Fantoma", rez[2].get_nume())
        self.assertEqual("Andrei", rez[0].get_nume())
    
    def test_search_nume_film(self):
        ans=self.__srv_film.search_nume("Konoha")
        self.assertEqual([self.__film2],ans)

        ans=self.__srv_film.search_nume("Oblivion")
        self.assertEqual([self.__film1],ans)
        ans=self.__srv_film.search_nume("Konojjha")
        self.assertEqual([],ans)  
    
    def test_sortare_nr_filme(self):
        self.assertEqual(0,len(self.__rep_inchir))
        self.__serv_inchirieri.inchiriere(1, 1)
        self.__serv_inchirieri.inchiriere(2, 2)
        rez=self.__serv_inchirieri.sortare_clienti_nr_filme()
        self.assertEqual(2,len(rez))
        self.assertEqual("Andrei", rez[0].get_nume())
        self.assertEqual("Cristian", rez[1].get_nume())
        self.__serv_inchirieri.inchiriere(1, 2)
        self.__serv_inchirieri.inchiriere(1, 3)
        self.__serv_inchirieri.inchiriere(2, 1)
        self.__serv_inchirieri.inchiriere(3, 1)
        rez=self.__serv_inchirieri.sortare_clienti_nr_filme()
        self.assertEqual(3,len(rez))
        self.assertEqual("Fantoma", rez[0].get_nume())
        self.assertEqual("Cristian", rez[1].get_nume())
        self.assertEqual("Andrei", rez[2].get_nume())
        rez=self.__serv_inchirieri.sortare_clienti_partial()
        self.assertEqual(1,len(rez))
        self.assertEqual("Andrei", rez[0].get_nume())
        self.assertEqual(3, rez[0].get_nr_filme())
        rez=self.__serv_inchirieri.sortare_nr_filme()
        self.assertEqual(3,len(rez))
        self.assertEqual("Oblivion",rez[0].get_titlu() )
        self.assertEqual("Konoha",rez[1].get_titlu() )
        self.assertEqual("Bakugan",rez[2].get_titlu() )
        self.assertEqual(3, rez[0].get_nr_clienti())
        self.assertEqual(2, rez[1].get_nr_clienti())
        self.__serv_inchirieri.returnare(1, 1)
        rez=self.__serv_inchirieri.sortare_nr_filme()
        self.assertEqual(3,len(rez))
        self.assertEqual("Konoha",rez[1].get_titlu() )
       # self.assertEqual(3, rez[1].get_nr_clienti())
        self.__serv_inchirieri.inchiriere(1, 1)
        rez=self.__serv_inchirieri.sortare_nr_filme()
        self.assertEqual(3,len(rez))
        self.assertEqual("Oblivion",rez[0].get_titlu() )
       # self.assertEqual(4, rez[0].get_nr_clienti())
    
    def test_sortare_gen_nume_client(self):
        self.__serv_inchirieri.inchiriere(1, 1)
        self.__serv_inchirieri.inchiriere(1, 2)
        rez=self.__serv_inchirieri.sortare_filme_gen("crima")
        self.assertEqual(rez,[self.__client2,self.__client3] )
        self.__serv_inchirieri.inchiriere(2, 1)
        rez=self.__serv_inchirieri.sortare_filme_gen("crima")
        self.assertEqual(rez,[self.__client3])
        rez=self.__serv_inchirieri.sortare_filme_gen("familie")
        self.assertEqual(rez,[self.__client2,self.__client3])
        rez=self.__serv_inchirieri.sortare_filme_gen("comedie")
        self.assertEqual(rez,[self.__client1,self.__client2,self.__client3])
        rez=self.__serv_inchirieri.sortare_filme_gen("dsgsgcomedie")
        self.assertEqual(rez,[self.__client1,self.__client2,self.__client3])
    
    def test_search_nume_client(self):
        ans=self.__srv_client.search_nume("Andrei")
        self.assertEqual([self.__client1],ans)
        ans=self.__srv_client.search_nume("Cristian")
        self.assertEqual([self.__client2],ans)


class Test_Metode_Sortare(unittest.TestCase):

    def setUp(self):
        self.__lista=[Client(1,"Andrei","5010207226734"),Client(4,"Iustin","5010207226734"),\
                      Client(3,"Zarzane","5010207226734"),Client(2,"Igor","5010207226734")]
        self.__number_list=[4,5,2,6,3,1,8]

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def test_Insertie(self):
        self.__lista=Sortari.InsertionSort(self.__lista,key=lambda x:x.get_nume(),reverse=False) 
        self.assertEqual(self.__lista[0].get_nume(),"Andrei")
        self.assertEqual(self.__lista[2].get_nume(),"Iustin")
        self.assertEqual(self.__lista[1].get_nume(),"Igor")
        self.assertEqual(self.__lista[3].get_nume(),"Zarzane")
        self.__lista=Sortari.InsertionSort(self.__lista,key=lambda x:x.get_id_client(),cmp=lambda x,y:x>y)
        self.assertEqual(4,self.__lista[0].get_id_client())
        self.assertEqual(3,self.__lista[1].get_id_client())
        self.assertEqual(2,self.__lista[2].get_id_client())
        self.assertEqual(1,self.__lista[3].get_id_client())
         
    def test_Comb_sort(self):
        self.__lista=Sortari.CombSort(self.__lista,key=lambda x:x.get_nume(),reverse=False) 
        self.assertEqual(self.__lista[0].get_nume(),"Andrei")
        self.assertEqual(self.__lista[2].get_nume(),"Iustin")
        self.assertEqual(self.__lista[1].get_nume(),"Igor")
        self.assertEqual(self.__lista[3].get_nume(),"Zarzane")
        self.__lista=Sortari.CombSort(self.__lista,key=lambda x:x.get_id_client(),reverse=True)
        self.assertEqual(4,self.__lista[0].get_id_client())
        self.assertEqual(3,self.__lista[1].get_id_client())
        self.assertEqual(2,self.__lista[2].get_id_client())
        self.assertEqual(1,self.__lista[3].get_id_client())
        self.__number_list=Sortari.CombSort(self.__number_list)
        self.assertEqual([1,2,3,4,5,6,8],self.__number_list)
        self.__number_list=Sortari.CombSort(self.__number_list,reverse=True)
        self.assertEqual([8,6,5,4,3,2,1],self.__number_list)
        
    

        

if __name__ == '__main__':
    unittest.main()
