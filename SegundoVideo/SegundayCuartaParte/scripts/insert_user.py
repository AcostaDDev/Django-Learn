from loans.models import User

user1 = User.objects.create(
    first_name="John",
    last_name="Doe",
    address="123 Main St",
    phone="555-1234",
    email="john@example.com"
)

user2 = User.objects.create(
    first_name="Jane",
    last_name="Smith",
    address="456 Elm St",
    phone="555-5678",
    email="jane@example.com"
)

user3 = User.objects.create(
    first_name="Mike",
    last_name="Johnson",
    address="789 Oak St",
    phone="555-9012",
    email="mike@example.com"
)