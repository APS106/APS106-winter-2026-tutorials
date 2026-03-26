import csv

# Practice Problem: OOP + CSV
class SensorReader:
    def __init__(self, filename):
        """
        Initializes the SensorReader with a given CSV filename.
        """
        self.filename = filename
        self.data = []  # will store the CSV data after read_data() is called

    def read_data(self):
        """
        Reads the CSV file and stores all rows in self.data.
        """
        # TODO: open the file using csv.reader and store rows in self.data
        pass

    def __str__(self):
        """
        Returns a string with basic information:
        - The filename
        - How many rows of data have been loaded
        """
        # TODO: return a string like "SensorReader reading from <filename>: <N> rows loaded."
        pass

    def save_filtered_data(self, output_file, threshold):
        """
        Saves only the rows where 'voltage' (assumed to be in column index 1)
        is above the specified threshold.

        Writes the filtered data to the specified output file.
        """
        # TODO: write only rows where voltage > threshold to output_file
        pass


# Practice Problem: OOP + File I/O
class Book:
    def __init__(self, title, author, year, is_checked_out=False):
        # TODO: store the attributes
        pass

    def check_out(self):
        # TODO: set is_checked_out to True
        pass

    def return_book(self):
        # TODO: set is_checked_out to False
        pass

    def __str__(self):
        # TODO: return a string like "[Available] Title by Author (Year)"
        # or "[Checked Out] Title by Author (Year)"
        pass

class Library:
    def __init__(self):
        self.books = []  # will hold a list of Book objects

    def load_books_from_csv(self, filename):
        """
        Reads a CSV where each row contains: title,author,year,is_checked_out
        """
        # TODO: read the CSV file and create Book objects, appending to self.books
        pass

    def save_books_to_csv(self, filename):
        """
        Writes the same format to CSV, including the current status.
        For each book, we write: title,author,year,is_checked_out
        """
        # TODO: write each book's data to a CSV file
        pass

    def find_book_by_title(self, title):
        """
        Returns the Book object if a matching title is found, otherwise None.
        """
        # TODO: loop through self.books and return the matching book
        pass

    def check_out_book(self, title):
        """
        If found and available, mark the book as checked out.
        If not found, or already checked out, handle gracefully.
        """
        # TODO: find the book by title and check it out
        pass
