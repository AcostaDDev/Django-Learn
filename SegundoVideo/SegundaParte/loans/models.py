from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=255, verbose_name='Género')

    def __str__(self):
        return self.name
    
class Publisher(models.Model):
    name = models.CharField(max_length=255, verbose_name='Editorial')

    def __str__(self):
        return self.name

class Book(models.Model):

    class Meta:
        verbose_name = "Libro"
        verbose_name_plural = "Libros"

    # genre_choice = [
    #     (1, "Drama"),
    #     (2, "Acción"),
    #     (3, "Thriller"),
    #     (4, "Comedia"),
    #     (5, "Fantasía"),
    # ]

    title = models.CharField(max_length=255, verbose_name="Título")
    author = models.CharField(max_length=255, verbose_name="Autor")
    # genre = models.CharField(max_length=255, verbose_name="Género", blank=True, null=True)
    year = models.IntegerField(verbose_name="Año")
    # publisher = models.CharField(max_length=255, verbose_name="Editorial")
    # genre_list = models.IntegerField(choices=genre_choice, default=1, verbose_name="Lista de géneros", blank=True, null=True)
    genre = models.ForeignKey(Genre, verbose_name="Género", on_delete=models.DO_NOTHING)
    publisher = models.ForeignKey(Publisher, verbose_name="Editorial", on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.title} - {self.author}"
    

class User(models.Model):

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    first_name = models.CharField(max_length=255, verbose_name="Nombre")
    last_name = models.CharField(max_length=255, verbose_name="Apellidos")
    address = models.CharField(max_length=255, verbose_name="Dirección")
    phone = models.CharField(max_length=255, verbose_name="Teléfono")
    email = models.EmailField(verbose_name="Email")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Loan(models.Model):

    class Meta:
        verbose_name = "Préstamo"
        verbose_name_plural = "Préstamos"

    user_id = models.ForeignKey(User, on_delete=models.SET_DEFAULT, null=True, default=1, verbose_name="Usuario")
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name="Libro")
    loan_date = models.DateField(verbose_name="Fecha de préstamo")
    due_date = models.DateField(verbose_name="Fecha de devolución")

    def __str__(self):
        return f"{self.user_id} - {self.book_id}"
    
class Artist(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
# class Album(models.Model):
#     artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

# class Song(models.Model):
#     artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
#     album = models.ForeignKey(Album, on_delete=models.RESTRICT)

# class Author(models.Model):
#     first_name = models.CharField(max_length=255, verbose_name='Nombre')
#     last_name = models.CharField(max_length=255, verbose_name='Apellido')

