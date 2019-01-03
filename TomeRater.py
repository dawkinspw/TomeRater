class User(object):
    def __init__(self, name, email):
        self.name = str(name)
        self.email = str(email)
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = str(address)
        print("{}'s email has been updated to {}.".format(self.name, self.email))

    def __repr__(self):
        return("User:  {}\nEmail: {}\nBooks Read: {}".format(self.name, self.email, len(self.books)))

    def __eq__(self, other_user):
        if self.name == other_user.name and self.email == other_user.email:
            return True
        else:
            return False

    def read_book(self, book, rating = None):
        self.books[book] = rating

    def get_average_rating(self):
        summ = 0
        count = 0
        for i in self.books.values():
            if i != None:
                count += 1
                summ += i
        return summ / count

class Book(object):
    def __init__(self, title, isbn):
        self.title = str(title)
        self.isbn = int(isbn)
        self.ratings = []
    
    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_isbn):
        self.isbn = int(new_isbn)
        print("{}'s ISBN has been updated to {}.".format(self.title, self.isbn))

    def add_rating(self, rating):
        if rating >= 0 and rating <= 4:
            self.ratings.append(rating)
        else:
            print("Invalid Rating")

    def __eq__(self, other_book):
        if self.title == other_book.title and self.isbn == other_book.isbn:
            return True
        else:
            return False

    def get_average_rating(self):
        summ = 0
        count = 0
        for i in self.ratings:
            count += 1
            summ += i
        return summ / count

    def __hash__(self):
        return hash((self.title, self.isbn))

class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = str(author)

    def get_author(self):
        return self.author

    def __repr__(self):
        return("{} by {}".format(self.title, self.author))

class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = str(subject)
        self.level = str(level)

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return("{}, a {} manual on {}".format(self.title, self.level, self.subject))

class TomeRater():
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        return Book(title, isbn)

    def create_novel(self, title, author, isbn):
        return Fiction(title, author, isbn)

    def create_non_fiction(self, title, subject, level, isbn):
        return Non_Fiction(title, subject, level, isbn)

    def add_book_to_user(self, book, email, rating = None):
        if email in self.users.keys():
            self.users[email].read_book(book, rating)
            if rating != None:
                book.add_rating(rating)
            if book in self.books.keys():
                self.books[book] += 1
            else:
                self.books[book] = 1
        else:
            print("No user with email {}!".format(email))

    def add_user(self, name, email, user_books = None):
        my_user = User(name, email)
        self.users[email] = my_user
        if user_books != None:
            for i in user_books:
                self.add_book_to_user(i, email)

    def print_catalog(self):
        for i in self.books.keys():
            print(i)

    def print_users(self):
        for i in self.users.values():
            print(i)

    def most_read_book(self):
        largest_key = ""
        largest_value = 0
        for i in self.books.keys():
            if self.books[i] > largest_value:
                largest_key = i.title
                largest_value = self.books[i]
        return largest_key

    def highest_rated_book(self):
        best_book_title = ""
        best_average_value = 0        
        for i in self.books.keys():
            if i.get_average_rating() > best_average_value:
                best_book_title = i.title
                best_average_value = i.get_average_rating()
        return best_book_title

    def most_positive_user(self):
        high_avg = 0
        high_name = ""
        for i in self.users.values():
            avg = i.get_average_rating()
            if avg > high_avg:
                high_avg = avg
                high_name = i.name
        return high_name

    def __repr__(self):
        return("This is the TomeRater Project!")

    def __eq__(self, other_tomerater):
        if self.users == other_tomerater.users and self.books == other_tomerater.books:
            return True
        else:
            return False
