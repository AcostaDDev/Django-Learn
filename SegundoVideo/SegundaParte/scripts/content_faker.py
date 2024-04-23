from loans.models import User, Loan, Book

from faker import Faker

fake = Faker('es_ES')

for _ in range(10):
    User.objects.create(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        address=fake.address(),
        phone=fake.phone_number(),
        email=fake.email()
    )

users = User.objects.all()
books = Book.objects.all()

for _ in range(10):
    Loan.objects.create(
        user_id = fake.random_element(users),
        book_id = fake.random_element(books),
        loan_date = fake.date_between(start_date='-1y', end_date='today'),
        due_date = fake.date_between(start_date='today', end_date='+1y'),
    )