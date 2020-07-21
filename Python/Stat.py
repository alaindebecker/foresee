import pandas

class ReadError(Exception) :
    '''  Exception raised for errors while reading files '''
    pass
    
class Stat(pandas.DataFrame) :


    def read_csv(file, **kwargs) :
        ''' Same as pandas.read_csv except encoding default is 'ANSI'. '''
        if 'encoding' not in kwargs :
            kwargs['encoding'] = 'ANSI'
        try :
            return Stat(pandas.read_csv(file, **kwargs))

        except UnicodeDecodeError as err:
            raise ReadError(f"Cannot read file {file} probaly due to use of encoding '{err.args[0]}'.")
        except LookupError as err:
            raise ReadError(f"Cannot read file {file}: {err.args[0]}.")


    def read_excel(file, **kwargs) :
        ''' Same as pandas.read_excel except default is to read all sheets in one dict. '''
        if 'sheet' not in kwargs :
            kwargs['sheet'] = None
        kwargs['sheet_name'] = kwargs['sheet']
        del kwargs['sheet']
        return pandas.read_excel(file, **kwargs)


    def sort(self, *by) :
        ''' Order a table by the specifed columns list.

            If the column name is prededed by a minus sign ('-'), 
            then the column is sorted by descending values.
            otherwise it is sorted by ascending values.
            
            The sort is stable, so that the realive order with equals 
            values is maintained.
            
        '''  
        #TODO: sort on computed column
        df = self
        for c in reversed(by) :
            if c.startswith('-') :
                df = df.sort_values(c[1:], ascending=False, kind='mergesort', ignore_index=True)
            else :
                df = df.sort_values(c, ascending=True, kind='mergesort', ignore_index=True)
        return Stat(df)


        
        
''' Read from Excel, all sheets in one dict '''
'''
db = Stat.read_excel('C:/Uhelpers/aldebeck/Desktop/projets/Sampledata/ClassicModels.xlsx')
Customers = db['Customers']
Employees = db['Employees']
Offices   = db['Offices']
OrderDetails = db['OrderDetails']
Orders    = db['Orders']
Payments  = db['Payments']
Products  = db['Products']
'''

''' Read from Excel, sheet by sheet '''
'''
Customers = Stat.read_excel('C:/Users/aldebeck/Desktop/projets/Sampledata/ClassicModels.xlsx', sheet='Customers')
Employees = Stat.read_excel('C:/Users/aldebeck/Desktop/projets/Sampledata/ClassicModels.xlsx', sheet='Employees')
Offices   = Stat.read_excel('C:/Users/aldebeck/Desktop/projets/Sampledata/ClassicModels.xlsx', sheet='Offices')
OrderDetails = Stat.read_excel('C:/Users/aldebeck/Desktop/projets/Sampledata/ClassicModels.xlsx', sheet='OrderDetails')
Orders    = Stat.read_excel('C:/Users/aldebeck/Desktop/projets/Sampledata/ClassicModels.xlsx', sheet='Orders')
Payments  = Stat.read_excel('C:/Users/aldebeck/Desktop/projets/Sampledata/ClassicModels.xlsx', sheet='Payments')
Products  = Stat.read_excel('C:/Users/aldebeck/Desktop/projets/Sampledata/ClassicModels.xlsx', sheet='Products')
'''

''' Read from csv '''
Customers = Stat.read_csv('C:/Users/aldebeck/Desktop/projets/Sampledata/Customers.csv')
Employees = Stat.read_csv('C:/Users/aldebeck/Desktop/projets/Sampledata/Employees.csv')
Offices   = Stat.read_csv('C:/Users/aldebeck/Desktop/projets/Sampledata/Offices.csv')
OrderDetails = Stat.read_csv('C:/Users/aldebeck/Desktop/projets/Sampledata/OrderDetails.csv', sep='\t')
Orders    = Stat.read_csv('C:/Users/aldebeck/Desktop/projets/Sampledata/Orders.csv')
Payments  = Stat.read_csv('C:/Users/aldebeck/Desktop/projets/Sampledata/Payments.csv')
Products  = Stat.read_csv('C:/Users/aldebeck/Desktop/projets/Sampledata/Products.csv')





''' Prepare a list of offices sorted by country, state, city '''
x = 'country'
df = Offices.sort(x,'-state','city')
print(df)

''' How many employees are in the company '''
