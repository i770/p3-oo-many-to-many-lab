class Author:
    instances = []  # Class variable to keep track of instances

    def __init__(self, name):
        self.name = name
        self.contracts_list = []  # To store contracts related to this author
        Author.instances.append(self)  # Add instance to the class variable

    def contracts(self):
        return self.contracts_list

    def books(self):
        return [contract.book for contract in self.contracts_list]

    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book):
            raise Exception("book must be an instance of Book")
        if not isinstance(royalties, int):
            raise Exception("royalties must be an integer")
        contract = Contract(self, book, date, royalties)
        self.contracts_list.append(contract)  # Ensure the contract is added to the author's contracts list
        book.contracts_list.append(contract)  # Ensure the contract is added to the book's contracts list
        return contract

    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts_list)


class Book:
    instances = []  # Class variable to keep track of instances

    def __init__(self, title):
        self.title = title
        self.contracts_list = []  # To store contracts related to this book
        Book.instances.append(self)  # Add instance to the class variable

    def contracts(self):
        return self.contracts_list

    def authors(self):
        return [contract.author for contract in self.contracts_list]  # Return authors from contracts


class Contract:
    instances = []  # Class variable to keep track of instances

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("author must be an instance of Author")
        if not isinstance(book, Book):
            raise Exception("book must be an instance of Book")
        if not isinstance(date, str):
            raise Exception("date must be a string")
        if not isinstance(royalties, int):
            raise Exception("royalties must be an integer")
        
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.instances.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.instances if contract.date == date]
