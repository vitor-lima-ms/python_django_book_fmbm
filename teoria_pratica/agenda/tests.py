from class_contact import Contact
from class_contact_repository import ContactRepository
from class_contact_register import ContactRegister
from pprint import pprint

# """Testing Contact and ContactRepository class"""
# vitor = Contact(1, 'Vitor', '998371486')
# geraldo = Contact(2, 'Geraldo', '999560316')

# repository = ContactRepository()

# """Testing include method"""
# repository.repo_include(vitor)
# repository.repo_include(geraldo)

# """Testing change method"""
# repository.repo_change(vitor)
# print()
# repository.repo_change(vitor)
# print()

# """Testing remove_by_id method"""
# repository.remove_by_id()

# """Testing query_index_by_name method"""
# repository.query_index_by_name()

# """Testing exist_by_phone method"""
# test_contact = Contact(3, 'Test name', 'Test phone')
# repository.exist_by_phone(test_contact)

"""Testing ContactRegister class"""
vitor = Contact(1, 'Vitor', '998371486')
geraldo = Contact(2, 'Geraldo', '999560316')

contact_manager = ContactRegister()

"""Testing include method"""
contact_manager.include(vitor)
contact_manager.include(geraldo)

"""Testing change method"""
# contact_manager.change(vitor)
# print(vitor.name)
# contact_manager.change(geraldo)
# print(geraldo.tel)

"""Testing remove method"""
# contact_manager.remove(vitor)
# contact_manager.remove(geraldo)

"""Testing consult method"""
contact_manager.consult('Gera')