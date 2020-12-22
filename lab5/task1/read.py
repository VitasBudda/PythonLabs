import ZODB, ZODB.FileStorage, transaction
from storage_model import StorageModel


storage = ZODB.FileStorage.FileStorage('storages')
db = ZODB.DB(storage)
connection = db.open()
root = connection.root()

date = input('date: ')

goods = list(filter(lambda s: s.date == date, root['storages']))

if len(goods) == 0 :
    print("No goods for this date")
    exit()

most_expensive = max(goods, key=lambda g: int(g.price))
all_price = sum(int(good.price) for good in goods)

print("Name of most expensive: ", most_expensive.name)
print("Sum of prices: ", all_price)

