import random
from datetime import date

from credit.models import Client, Account, Credit

client1 = Client.objects.create(name='Бердиев Нурсултан', birth_year=date(1994, 1, 10), work_place='Codify/Mentor')
client2 = Client.objects.create(name='Алымбеков Мырза', birth_year=date(1997, 3, 15), work_place='Codify/Student')


def id_generator():
    import random
    a = random.randrange(1000_000_000_000_000, 10000_000_000_000_000)
    b = str(a)
    return b


account1 = client1.accounts.create(number=id_generator(), account_type=1)
account2 = client1.accounts.create(number=id_generator(), account_type=2)

account3 = client2.accounts.create(number=id_generator(), account_type=1)
account4 = client2.accounts.create(number=id_generator(), account_type=2)

credit1 = account1.credits.create(sum=100000)
credit2 = account2.credits.create(sum=200000)
credit3 = account3.credits.create(sum=300000)
credit4 = account4.credits.create(sum=400000)



