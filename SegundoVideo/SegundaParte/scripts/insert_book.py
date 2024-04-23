from loans.models import Book

book1 = Book(title="Eñ gran Gatsby", author="F. Scott Fitzgerald", genre="Ficción", year=1925, publisher="Scribner")
book1.save()

Book.objects.create(title="Matar a un suiseñor", author="Harper Lee", genre="Ficción", year=1960, publisher="J. B. Lippincott & Co.")

Book.objects.create(title="1984", author="George Orwell", genre="Ficción", year=1949, publisher="Secker & Warburg")

Book.objects.create(title="Pride and Prejudice", author="Jane Austen", genre="Ficción", year=1813, publisher="T. Egerton, Whitehall")

Book.objects.create(title="El guardián entre el centeno", author="J. D. Salinger", genre="Ficción", year=1951, publisher="Little, Brown and Company")