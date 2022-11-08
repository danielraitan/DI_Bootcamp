from faker import Faker
fake = Faker()

fake.name()
fake.address()

for _ in range(3):
    fake_list = fake.name(), fake.address()
    print(fake_list)
   

  






