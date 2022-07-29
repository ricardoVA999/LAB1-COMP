from prettytable import PrettyTable

class TablaSimbolos():
    def __init__(self):
        self.my_table = PrettyTable()
        self.symbols = []
        self.off = 0

    def Add(self, tipo, id, size, off, isParameter):
        self.symbols.append({
            'Tipo': tipo,
            'Id': id,
            'Size': size,
            'Offset': off,
            'IsParameter': isParameter
        })

        self.off += size

    def LookUp(self, variable):
        symbols_copy = self.symbols.copy()
        symbols_copy.reverse()
        for symbol in symbols_copy:
            if symbol['Id'] == variable:
                return symbol

        return 0
    
    def GetSize(self):
        return sum(symbol['Size'] for symbol in self.symbols)

    def ToTable(self):
        self.my_table.field_names = ['Tipo', 'ID', 'Size', 'Offset', 'IsParameter']
        for i in self.symbols:
            self.my_table.add_row(list(i.values()))

        print("My symbols table:")
        print(self.my_table)
        self.my_table.clear_rows()