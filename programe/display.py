import string


def fixed_len(text,f_len):
    '''
    >>> fixed_len("abc",6)
    'abc   '
    '''
    text=str(text)
    actual_len=0
    for char in text:
        if char in string.printable:
            actual_len+=1
        else:
            actual_len+=2

    diff_len=f_len-actual_len
    return text+" "*diff_len

def make_row(id_,name,phone):
    '''
    >>> make_row(1,"小王","13588934489")
    '|1  |小王      |13588934489         |'
    '''
    
    return '|%s|%s|%s|'%(fixed_len(id_,3),
                         fixed_len(name,10),
                         fixed_len(phone,20))

def print_table(data):
    '''
    >>> print_table([[1,'校长','13876457794']])
    -------------------------------------
    |ID |姓名      |电话号码            |
    -------------------------------------
    |1  |校长      |13876457794         |
    -------------------------------------
    '''



    divid_line='-'*37
    print(divid_line)
    print(make_row('ID','姓名','电话号码'))
    print(divid_line)
    for row in data:
        print(make_row(row[0],row[1],row[2]))
        print(divid_line)






if __name__=="__main__":
    import doctest
    doctest.testmod(verbose=True)
