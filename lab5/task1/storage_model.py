from datetime import datetime


class StorageModel:
    def __init__(self, name, price, count, date, batch_number, first_name, last_name):
        self.name = name
        self.price = price
        self.count = count
        self.date = date
        self.batch_number = batch_number
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return '{}, {}, {}, {}, {}'\
            .format(self.name, self.price, self.count, self.date,
                self.batch_number, self.first_name, self.last_name) 