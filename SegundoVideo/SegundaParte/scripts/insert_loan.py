from loans.models import Loan, User, Book

loan1 = Loan.objects.create(
    user_id=User.objects.get(id=1),
    book_id=Book.objects.get(id=1),
    loan_date="2022-01-01",
    due_date="2022-01-15"
)

loan2 = Loan.objects.create(
    user_id=User.objects.get(id=2),
    book_id=Book.objects.get(id=2),
    loan_date="2022-02-02",
    due_date="2022-02-15"
)

loan3 = Loan.objects.create(
    user_id=User.objects.get(id=3),
    book_id=Book.objects.get(id=3),
    loan_date="2022-03-03",
    due_date="2022-03-15"
)