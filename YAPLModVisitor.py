from antlr4 import *
from YAPLVisitor import YAPLVisitor
from simbolos import TablaSimbolos
from YAPLParser import YAPLParser

class myVisitor(YAPLVisitor):
    def __init__(self) -> None:
        self.symtab = TablaSimbolos()

    def visitClass(self, ctx):
        this_class = ctx.var_type()[0].getText()
        self.symtab.add_symb(str(this_class), "Class: "+str(this_class), "General")
        return self.visitChildren(ctx)

    def visitFeature(self, ctx):
        this_feature = ctx.var_id().getText()
        this_type = ctx.var_type().getText()
        if "<-" in ctx.getText():
            self.symtab.add_symb(str(this_feature), "Feature: "+str(this_type), "Set Feature")
        else:
            self.symtab.add_symb(str(this_feature), "Feature: "+str(this_type), "Brace Feature")
        return super().visitChildren(ctx)


    def visitFormal(self, ctx: YAPLParser.FormalContext):
        this_name = ctx.var_id().getText()
        this_type = ctx.var_type().getText()
        self.symtab.add_symb(str(this_name), str(this_type), "Formal")
        return super().visitChildren(ctx)

    def visitAssign_expr(self, ctx: YAPLParser.Assign_exprContext):
        return super().visitChildren(ctx)
    
    def visitExpr_expr(self, ctx: YAPLParser.Expr_exprContext):
        return super().visitChildren(ctx)
    
    def visitCall_expr(self, ctx: YAPLParser.Call_exprContext):
        return super().visitChildren(ctx)
    
    def visitConditional_expr(self, ctx: YAPLParser.Conditional_exprContext):
        return super().visitChildren(ctx)

    def visitLoop_expr(self, ctx: YAPLParser.Loop_exprContext):
        return super().visitChildren(ctx)
    
    def visitBr_expr(self, ctx: YAPLParser.Br_exprContext):
        return super().visitChildren(ctx)

    def visitLet_expr(self, ctx: YAPLParser.Let_exprContext):
        this_name = ctx.var_id()
        this_type = ctx.var_type()
        for i in range(0, len(this_name)):
            self.symtab.add_symb(str(this_name[i].getText()), str(this_type[i].getText()), "Let Variable" if i == 0 else "Let Parameter")
        return super().visitChildren(ctx)
    
    def visitNew_expr(self, ctx: YAPLParser.New_exprContext):
        return super().visitChildren(ctx)
    
    def visitVoid_expr(self, ctx: YAPLParser.Void_exprContext):
        return super().visitChildren(ctx)
    
    def visitAdd_expr(self, ctx: YAPLParser.Add_exprContext):
        return super().visitChildren(ctx)

    def visitSub_expr(self, ctx: YAPLParser.Sub_exprContext):
        return super().visitChildren(ctx)

    def visitMul_expr(self, ctx: YAPLParser.Mul_exprContext):
        return super().visitChildren(ctx)

    def visitDiv_expr(self, ctx: YAPLParser.Div_exprContext):
        return super().visitChildren(ctx)

    def visitInt_expr(self, ctx: YAPLParser.Int_exprContext):
        return super().visitChildren(ctx)
    
    def visitNeg_expr(self, ctx: YAPLParser.Neg_exprContext):
        return super().visitChildren(ctx)
    
    def visitLess_expr(self, ctx: YAPLParser.Less_exprContext):
        return super().visitChildren(ctx)
    
    def visitLessEq_expr(self, ctx: YAPLParser.LessEq_exprContext):
        return super().visitChildren(ctx)
    
    def visitEq_expr(self, ctx: YAPLParser.Eq_exprContext):
        return super().visitChildren(ctx)
    
    def visitNot_expr(self, ctx: YAPLParser.Not_exprContext):
        return super().visitChildren(ctx)
    
    def visitPar_expr(self, ctx: YAPLParser.Par_exprContext):
        return super().visitChildren(ctx)
    
    def visitVar_expr(self, ctx: YAPLParser.Var_exprContext):
        return {'Type': 'Var_ID', 'Value': ctx.var_id().getText()}
    
    def visitInt_expr(self, ctx: YAPLParser.Int_exprContext):
        return {'Type': 'Int', 'Value': ctx.getText()}
    
    def visitString_expr(self, ctx: YAPLParser.String_exprContext):
        return {'Type': 'String', 'Value': ctx.getText()}
    
    def visitTrue_expr(self, ctx: YAPLParser.True_exprContext):
        return {'Type': 'Bool', 'Value': ctx.getText()}
        
    def visitFalse_expr(self, ctx: YAPLParser.False_exprContext):
        return {'Type': 'Bool', 'Value': ctx.getText()}