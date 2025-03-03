class Contact:
    def __init__(self, id: int, name: str, tel:str) -> None:
        self.__id = id
        self.__name = name
        self.__tel = tel
    
    def __str__(self) -> str:
        return f'id: {self.__id}\nNome: {self.__name}\nTelefone: {self.__tel}'
    
    @property
    def id(self) -> int:
        return self.__id
    
    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, new_value) -> str:
        self.__name = new_value
    
    @property
    def tel(self) -> str:
        return self.__tel

    @tel.setter
    def tel(self, new_value) -> str:
        self.__tel = new_value

if __name__ == '__main__':
    test_contact = Contact(1, 'Vitor', '998371486')
    print(test_contact.__dict__.values())