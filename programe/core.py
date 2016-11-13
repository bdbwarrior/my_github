import csv

class AddressBook():
    '''DATA:
    [
     [1,'小王'，‘13899654782’]，
     【2，‘小罗’，‘18818765200’】
     ]
    '''
    def __init__(self):
        self._DATA=[]
        self.filepath='addressbook.csv'


    def load_data(self):
        with open(self.filepath,'r') as f:
            for line in csv.reader(f):
                line[0]=int(line[0])
                self._DATA.append(line)

    def save_data(self):
        with open(self.filepath,'w') as f:
            writer=csv.writer(f)
            for line in self._DATA:
                writer.writerow(line)

    def add_record(self,name,phone):
        last_id=self._DATA[-1] if len(self._DATA)>0 else 0
        new_id=last_id[0]+1
        new_row=[new_id,name,phone]
        self._DATA.append(new_row)


    def delete_record(self,row_id):
        for line in self._DATA:
            if line[0]==row_id:
                self._DATA.remove(line)

    def query_record(self,name):
        resultset=[]
        for line in self._DATA:
            if name in line[1]:
                resultset.append(line)
        return resultset




