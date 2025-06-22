from faker import Faker

fake = Faker("ru_RU")

data = {
    "name": fake.name(),
    "address": fake.address(),
    "age": fake.random_int(min=18, max=100),
    "email": fake.email()
}

print(data)