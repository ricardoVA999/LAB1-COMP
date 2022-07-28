# Generated from YAPL.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .YAPLParser import YAPLParser
else:
    from YAPLParser import YAPLParser

# This class defines a complete listener for a parse tree produced by YAPLParser.
class YAPLListener(ParseTreeListener):

    # Enter a parse tree produced by YAPLParser#program.
    def enterProgram(self, ctx:YAPLParser.ProgramContext):
        pass

    # Exit a parse tree produced by YAPLParser#program.
    def exitProgram(self, ctx:YAPLParser.ProgramContext):
        pass


    # Enter a parse tree produced by YAPLParser#class.
    def enterClass(self, ctx:YAPLParser.ClassContext):
        pass

    # Exit a parse tree produced by YAPLParser#class.
    def exitClass(self, ctx:YAPLParser.ClassContext):
        pass


    # Enter a parse tree produced by YAPLParser#feature.
    def enterFeature(self, ctx:YAPLParser.FeatureContext):
        pass

    # Exit a parse tree produced by YAPLParser#feature.
    def exitFeature(self, ctx:YAPLParser.FeatureContext):
        pass


    # Enter a parse tree produced by YAPLParser#formal.
    def enterFormal(self, ctx:YAPLParser.FormalContext):
        pass

    # Exit a parse tree produced by YAPLParser#formal.
    def exitFormal(self, ctx:YAPLParser.FormalContext):
        pass


    # Enter a parse tree produced by YAPLParser#expr.
    def enterExpr(self, ctx:YAPLParser.ExprContext):
        pass

    # Exit a parse tree produced by YAPLParser#expr.
    def exitExpr(self, ctx:YAPLParser.ExprContext):
        pass


    # Enter a parse tree produced by YAPLParser#var_type.
    def enterVar_type(self, ctx:YAPLParser.Var_typeContext):
        pass

    # Exit a parse tree produced by YAPLParser#var_type.
    def exitVar_type(self, ctx:YAPLParser.Var_typeContext):
        pass


    # Enter a parse tree produced by YAPLParser#var_id.
    def enterVar_id(self, ctx:YAPLParser.Var_idContext):
        pass

    # Exit a parse tree produced by YAPLParser#var_id.
    def exitVar_id(self, ctx:YAPLParser.Var_idContext):
        pass



del YAPLParser