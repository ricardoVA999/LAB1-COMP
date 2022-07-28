grammar YAPL;

// Keywords
CLASS           : 'CLASS' | 'class';
ELSE            : 'ELSE' | 'else';
FI              : 'FI' | 'fi';
IF              : 'IF' | 'if';
IN              : 'IN' | 'in';
INHERITS        : 'INHERITS' | 'inherits';
ISVOID          : 'ISVOID' | 'isvoid';
LOOP            : 'LOOP' | 'loop';
POOL            : 'POOL' | 'pool';
THEN            : 'THEN' | 'then';
WHILE           : 'WHILE' | 'while';
NEW             : 'NEW' | 'new';
NOT             : 'NOT' | 'not';
LET             : 'LET' | 'let';

FALSE           : 'false';
TRUE            : 'true';
SELF            : 'self';
SELF_TYPE       : 'SELF_TYPE';
BOOL            : 'Bool';
INT             : 'Int';
STRING          : 'String';
VOID            : 'void';


// Helpfull symbols
SEMICOLON       : ';';
COLON           : ':';
LBRACE          : '{';
RBRACE          : '}';
LBRACKET        : '[';
RBRACKET        : ']';
LPAR            : '(';
RPAR            : ')';
COMMA           : ',';
QUOTES          : '"';
APOSTROPHE      : '\'';
ADD             : '+';
SUB             : '-';
MULTIPLY        : '*';
DIVIDE          : '/';
NEGATION        : '~';
LESS_OP         : '<';
LESS_EQ_OP      : '<=';
EQUAL_OP        : '=';
DOT           : '.';
AT              : '@';
ASIGN           : '<-';

// Basic expresions

TYPE_ID         : CAP OBJ_ID;
OBJ_ID          : ALPHA ALPHA_NUM*; // for variable name
ALPHA           : [a-zA-Z_];
INTEGER         : [0-9]+;
DIGIT           : [0-9];
CAP             : [A-Z_];
ALPHA_NUM       : ALPHA | DIGIT;
STRING_LIT      : '"' ( '\\' [btnfr"'\\] | ~[\r\n\\"] )* '"'; // obtained from documentation
BOOL_LIT        : TRUE | FALSE;
COMMENT         : '--' .*? '\n' -> skip; // skip comment line starting with --
OTHER_COMMENT   : '..' .*? '..' -> skip; // skip comment between ..
NEWLINE		    : ('\r'? '\n' | '\r')+ -> skip; // skip new line
WHITESPACE	    : [ \t\r\n\f\b]+ -> skip; // skip all kind of whitespaces

// Productions

program         : (class SEMICOLON)+;
class           : CLASS var_type (INHERITS var_type)? LBRACE (feature)* RBRACE;
feature         : var_id LPAR (formal (COMMA formal)*)? RPAR COLON var_type LBRACE expr RBRACE SEMICOLON
                | var_id COLON var_type (ASIGN expr)? SEMICOLON;
formal          : var_id COLON var_type;
expr            : var_id ASIGN expr
                | expr (AT var_type)? DOT var_id LPAR (expr (COMMA expr)*)? RPAR
                | var_id LPAR (expr (COMMA expr)*)? LPAR
                | IF expr THEN expr ELSE expr FI
                | WHILE expr LOOP expr POOL
                | LBRACKET (expr SEMICOLON)+ RBRACKET
                | LET var_id COLON var_type (ASIGN expr)? (COMMA var_id COLON var_type (ASIGN expr)?)* IN expr
                | NEW var_type
                | ISVOID expr
                | expr ADD expr
                | expr SUB expr
                | expr MULTIPLY expr
                | expr DIVIDE expr
                | NEGATION expr
                | expr LESS_OP expr
                | expr LESS_EQ_OP expr
                | expr EQUAL_OP expr
                | NOT expr
                | LPAR expr RPAR
                | var_id
                | INTEGER
                | STRING_LIT
                | TRUE
                | FALSE;

var_type        : INT | BOOL | STRING | TYPE_ID | SELF_TYPE;
var_id          : OBJ_ID | SELF;

ERR_TOKEN : . ;