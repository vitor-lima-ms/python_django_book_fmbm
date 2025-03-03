from class_contact import Contact
from pprint import pprint
from time import sleep

class ContactRepository:
    def __init__(self) -> None:
        self.__repository: list[Contact] = list()
        self.__id_list: list[int] = list()
    
    def __repr__(self):
        return f'Contatos cadastrados {self.__repository}'
    
    @property
    def repository(self) -> list[Contact]:
        return self.__repository
    
    @property
    def id_list(self) -> list[Contact]:
        return self.__id_list

    def repo_include(self, contact: Contact) -> None:
        if len(self.__repository) == 0:
            self.__repository.append(contact.__dict__)
            print(f'{contact.name} cadastrado com sucesso.')
            self.__id_list.append(contact.id)
            pprint(self.__repository)
        else:
            flag = False
            for register in self.__repository:
                    if contact.id == register['_Contact__id']:
                        print(f'Contato {contact.name} não cadastrado. O id informado já está sendo utilizado.')
                        print(f'Consulte a lista de ids já cadastrados {self.__id_list}')
                        flag = True
                        return

            if not flag:        
                self.__repository.append(contact.__dict__)
                self.__id_list.append(contact.id)
                print(f'{contact.name} cadastrado com sucesso.')
                pprint(self.__repository)

    def repo_change(self, contact: Contact) -> None:
        attr_to_change = input('Qual atributo deseja alterar [Nome]/[Telefone]? ')

        if attr_to_change == 'Nome':
            contact.name = input('Digite o novo nome: ')
            print(f'Nome do contato alterado para {contact.name}')       
        elif attr_to_change == 'Telefone':
            contact.tel = input('Digite o novo telefone: ')
            print(f'Telefone do contato alterado para {contact.tel}')
    
    def remove_by_id(self, id: int) -> None:
        flag = False
        for register in self.__repository:
            if id == register['_Contact__id']:
                print(f'Deletanto o contato {register['_Contact__name']}...')
                sleep(2)
                self.__id_list.remove(register['_Contact__id'])
                self.__repository.remove(register)
                pprint(self.__repository)
                flag = True
                return
        
        if not flag:
            print('Não foi encontrado nenhum contato com o id informado.')
    
    def query_index_by_name(self, name: str) -> None:
        flag = False
        for register in self.__repository:
            if name == register['_Contact__name']:
                print(f'O id do contato {name} é {register["_Contact__id"]}.')
                flag = True
                return
        
        if not flag:
            print(f'Contato {name} não encontrado.')
    
    def query_contact_by_name(self, name: str) -> None:
        flag = False
        for register in self.__repository:
            if name == register['_Contact__name']:
                print(f'Informações do contato\nNome: {register["_Contact__name"]}.\nTelefone: {register["_Contact__tel"]}.')
                flag = True
                return
        
        if not flag:
            print(f'Contato {name} não encontrado.')
    
    def exist_by_phone(self, contact: Contact) -> None:
        flag = False
        for register in self.__repository:
            if contact.tel == register['_Contact__tel']:
                print(f'Telefone {contact.tel} pertence ao contato {register['_Contact__name']}.')
                flag = True
                return
        
        if not flag:
            print(f'Telefone {contact.tel} não encontrado.')
   