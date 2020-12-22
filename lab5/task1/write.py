import ZODB, ZODB.FileStorage, transaction
from storage_model import StorageModel

storage = ZODB.FileStorage.FileStorage('storages')
db = ZODB.DB(storage)
connection = db.open()
root = connection.root()

name = input('name: ')
price = input('price: ')
count = input('count: ')
date = input('date: ')
batch_number = input('batch_number: ')
first_name = input('first_name: ')
last_name = input('last_name: ')

if not 'storages' in root:
    root['storages'] = []

storages = root['storages']
storages.append(StorageModel(name, price, count, date, batch_number, first_name, last_name))
root['storages'] = storages

transaction.commit()