from antlr4 import *
from antlr4.tree.Trees import Trees
from antlr4.error.ErrorListener import ErrorListener
import antlr4.Utils as Utils
from parso import parse
from YAPLParser import YAPLParser
from YAPLLexer import YAPLLexer
from YAPLModVisitor import myVisitor

import sys

class TreeUtils():
    def __init__(self):
        self.eol = "\n"
        self.idents = "  "
        self.level = 0

    def toPrettyTree(self, t, rulenames):
        self.level = 0
        return self.process(t, rulenames).replace("(?m)^\\s+$", "").replace("\\r?\\n\\r?\\n", self.eol)

    def process(self, t, ruleNames):
        if t.getChildCount() == 0:
            return Utils.escapeWhitespace(Trees.getNodeText(t, ruleNames), False)
        sb = ""
        sb += self.lead(self.level)
        self.level += 1
        s = Utils.escapeWhitespace(Trees.getNodeText(t, ruleNames), False)
        sb += s + " "
        for i in range(t.getChildCount()):
            sb += self.process(t.getChild(i), ruleNames)
        
        self.level -= 1
        sb += self.lead(self.level)
        
        return sb

    def lead (self, level):
        sb = ""
        if level > 0:
            sb += self.eol
            for i in range(level):
                sb += self.idents

        return sb
        
class MyErrorListener(ErrorListener):
    def __init__(self):
        self.hasErrors = False
        self.sintaxErrors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.hasErrors = True
        errorMsg = f' => En linea {line}:{column} Se encontro {str(offendingSymbol).split("=")[1].split(",")[0]} Se esperaba {msg.split("expecting")[1]}'
        self.sintaxErrors.append(errorMsg)

    def getHasError(self):
        return self.hasErrors

    def getErrors(self):
        return self.sintaxErrors

class tks():
    def __init__(self, tk, line, type):
        self.tk = tk
        self.line = line
        self.type = type


def getError(tks):
    return tks != YAPLLexer.ERR_TOKEN

contentHasErr = False
filename = "antlr/aritmetica.yapl"
print(f'Parsing file: {filename}')

inputStream = FileStream(filename)
lexer = YAPLLexer(inputStream)
stream = CommonTokenStream(lexer)
listTks = []

actualTk = lexer.nextToken()
while actualTk.type != Token.EOF:
    is_error = getError(actualTk.type)
    if not is_error:
        print(f'Error caracter no reconocido: {actualTk.text} \n')
        contentHasErr = True
    listTks.append(tks(actualTk.text, actualTk.line, actualTk.type))
    actualTk = lexer.nextToken()

print("Todos los tokens encontradods: \n")
for tk in listTks:
    if not getError(tk.type):
        print(f'Token de error: {tk.tk}')
    else:
        print(f'Token: {tk.tk}')

if not contentHasErr:
    print("\nAnalisis lexico realizado correctamente")
else:
    print("\nHay errores lexicos")

lexer.reset()
stream = CommonTokenStream(lexer)
parser = YAPLParser(stream)

parser.removeErrorListeners()
listener = MyErrorListener()
parser.addErrorListener(listener)
parser.buildParseTrees = True
tree = parser.program()
rulenames = parser.ruleNames
prettyTree = TreeUtils().toPrettyTree(tree, rulenames)

sintErr = listener.getErrors()

if len(sintErr) > 0:
    print("\nHay errores sintacticos:")
    for err in sintErr:
        print(err)
else:
    print("\nAnalisis sintactico realizado correctamente")

if len(sintErr) < 1 and not contentHasErr:
    print("\nArbol de analisis sintactico:")
    print(prettyTree)

    my_v = myVisitor()
    my_v.visit(tree)
    my_v.symtab.print_table()