from loans.models import Book, Genre, Publisher

Genre.objects.create(name='Realismo mágico')
Genre.objects.create(name='Distopía')
Genre.objects.create(name='Novela')
Genre.objects.create(name='Romance')
Genre.objects.create(name='Ficción')
Genre.objects.create(name='Novela de caballería')
Genre.objects.create(name='Realismo')
Genre.objects.create(name='Fantasía')

Publisher.objects.create(name='Editorial Sudamericana')
Publisher.objects.create(name='Secker & Warburg')
Publisher.objects.create(name='J. B. Lippincott & Co.')
Publisher.objects.create(name='T. Egerton, Whitehall')
Publisher.objects.create(name='Charles Scribner\'s Sons')
Publisher.objects.create(name='Juan de la Cuesta')
Publisher.objects.create(name='Little, Brown and Company')
Publisher.objects.create(name='Bloomsbury Publishing')
Publisher.objects.create(name='George Allen & Unwin')
Publisher.objects.create(name='Cassell & Co.')

Book.objects.create(title='Cien años de soledad', author='Gabriel García Márquez',genre_id=1, year=1967, publisher_id=1)
Book.objects.create(title='1984', author='George Orwell', genre_id=2, year=1949, publisher_id=2)
Book.objects.create(title='To Kill a Mockingbird', author='Harper Lee', genre_id=3, year=1960, publisher_id=3)
Book.objects.create(title='Pride and Prejudice', author='Jane Austen', genre_id=4, year=1813, publisher_id=4)
Book.objects.create(title='The Great Gatsby', author='F. Scott Fitzgerald', genre_id=5, year=1925, publisher_id=5)
Book.objects.create(title='Don Quijote', author='Miguel de Cervantes Saavedra', genre_id=6, year=1605, publisher_id=6)
Book.objects.create(title='The Catcher in the Rye', author='J.D. Salinger', genre_id=7, year=1951, publisher_id=7)
Book.objects.create(title='Harry Potter and the Philosopher\'s Stone', author='J.K. Rowling', genre_id=8, year=1997, publisher_id=8)
Book.objects.create(title='The Hobbit', author='J.R.R. Tolkien', genre_id=8, year=1937, publisher_id=9)
Book.objects.create(title='The Lord of the Rings', author='J.R.R. Tolkien', genre_id=8, year=1954, publisher_id=9)


""" 
1. Título: "La isla del tesoro" 
   Autor: Robert Louis Stevenson 
   Género: Aventura 
   Año: 1883 
   Editorial: Cassell & Co. 
 
2. Título: "Las minas del rey Salomón" 
   Autor: H. Rider Haggard 
   Género: Aventura 
   Año: 1885 
   Editorial: Cassell & Co. 
 
3. Título: "La vuelta al mundo en 80 días" 
   Autor: Jules Verne 
   Género: Aventura 
   Año: 1873 
   Editorial: Pierre-Jules Hetzel 
 
4. Título: "Moby-Dick" 
   Autor: Herman Melville 
   Género: Aventura 
   Año: 1851 
   Editorial: Harper & Brothers 
 
5. Título: "La llamada de la selva" 
   Autor: Jack London 
   Género: Aventura 
   Año: 1903 
   Editorial: Macmillan Publishers 
 
6. Título: "Robinson Crusoe" 
   Autor: Daniel Defoe 
   Género: Aventura 
   Año: 1719 
   Editorial: W. Taylor 
 
7. Título: "El libro de la selva" 
   Autor: Rudyard Kipling 
   Género: Aventura 
   Año: 1894 
   Editorial: Macmillan Publishers 
 
8. Título: "Las aventuras de Tom Sawyer" 
   Autor: Mark Twain 
   Género: Aventura 
   Año: 1876 
   Editorial: American Publishing Company 
 
9. Título: "La odisea" 
   Autor: Homero 
   Género: Aventura 
   Año: Siglo VIII a.C. 
   Editorial: Varios 
 
10. Título: "El principito" 
   Autor: Antoine de Saint-Exupéry 
   Género: Aventura 
   Año: 1943 
   Editorial: Reynal & Hitchcock
 """