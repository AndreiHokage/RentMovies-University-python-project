class ClientError(Exception):
    pass


class RepositoryError_Client(Exception):
    pass


class FilmError(Exception):
    pass


class RepositoryError_Film(Exception):
    pass


class Inchiriere_clientfilm_Error(Exception):
    pass

class NoThereExemplar(Exception):
    pass

class Inchiriere_filmclient_Error(Exception):
    pass

class RepositoryError_Inchiriere(Exception):
    pass