from class_contact import Contact
from class_contact_repository import ContactRepository

class ContactRegister(ContactRepository):
    def __init__(self):
        super().__init__()

    def include(self, contact: Contact) -> None:
        super().repo_include(contact)
    
    def change(self, contact: Contact) -> None:
        super().repo_change(contact)
    
    def remove(self, contact: Contact) -> None:
        super().remove_by_id(contact.id)
    
    def consult(self, name: str) -> None:
        super().query_contact_by_name(name)
