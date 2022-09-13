class User:
    def _init_(self, name: str, id:int) -> None:
        self.name = name
        self.id = id

    def borrow_book(self, name_of_book:str):
        pass
    
    def return_book(self, name_of_book :str):
        pass
    
    def display_available_Books(self):
        pass

class Librarian:
    def _init_(self, name: str, list_books: list) -> None:
        self.name = name
        self.list_book = list_books
    
    def upload_list_of_books(self, name_of_book: str):
        self.list_book.append(name_of_book)
    
    def modify_list(self, name_of_book: str):
        self.list_book.remove(name_of_book)
