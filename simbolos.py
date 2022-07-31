from prettytable import PrettyTable

class TablaSimbolos():
    def __init__(self):
        self.symb_table = []

    def add_symb(self, name, type, scope):
        if(self.find_symb(name) == -1):
            return self.symb_table.append((name, type, scope))

    def find_symb(self, name):
        for symbol in self.symb_table:
            if name == symbol[0]:
                return symbol
        return -1

    def print_table(self):
        table = PrettyTable(['Nombre', 'Tipo', 'Ambiente'])
        for symbol in self.symb_table:
            table.add_row([symbol[0], symbol[1], symbol[2]])
        print(table)