class Publication:
    def __init__(self,name):
        self.name=name

class Book(Publication):
    def __init__(self,name,author,pages):
        self.author=author
        self.pages=pages
        super().__init__(name)

    def print_information(self):
        print(f"Name: {self.name}, Author: {self.author}, Pages: {self.pages}")

class Magazine(Publication):
    def __init__(self,name,chief):
        self.name=name
        self.chief=chief
        super().__init__(name)
    def print_information(self):
        print(f"Name: {self.name}, Chief: {self.chief}")


publications = []
publications.append(Magazine("Donald Duck","Aki Hyyppä"))
publications.append(Book("Compartnment No. 6","Rosa Liksom", "192"))

for p in publications:
    p.print_information()