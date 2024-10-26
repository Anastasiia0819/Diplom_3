import faker


def get_random_data_user():
    fake = faker.Faker('en_US')
    email = fake.email()
    password = fake.password()
    name = fake.first_name()
    return email, password, name

