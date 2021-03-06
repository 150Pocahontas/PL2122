
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'BAR DOTS EXCLAM FUNCTION HASH LINE NEWLINE NUM STAR STRING TAB TERMAxiom : AllAll : EntryAll : All EntryEntry : Production NEWLINEEntry : actEntry : FunctionFunction : FUNCTION StringProduction : Identification DOTS SymbolsProduction : Identification DOTS Symbols EXCLAM LINEProduction : BAR SymbolsProduction : BAR Symbols EXCLAM LINESymbols : SymbolSymbols : Symbols SymbolSymbol : TERMSymbol : terminalact : HASH Identification DOTS Stringact : HASH Identification STAR NUM DOTS StringString : LINE NEWLINE StringsString : LINEString : NEWLINE StringsString : LINE NEWLINEStrings : NEWLINEStrings : TAB NEWLINEStrings : Strings TAB NEWLINEIdentification : STRINGterminal : STRING'
    
_lr_action_items = {'BAR':([0,2,3,5,6,12,13,21,22,29,30,31,35,37,39,42,43,],[8,8,-2,-5,-6,-3,-4,-7,-19,-21,-22,-20,-16,-18,-23,-24,-17,]),'HASH':([0,2,3,5,6,12,13,21,22,29,30,31,35,37,39,42,43,],[9,9,-2,-5,-6,-3,-4,-7,-19,-21,-22,-20,-16,-18,-23,-24,-17,]),'FUNCTION':([0,2,3,5,6,12,13,21,22,29,30,31,35,37,39,42,43,],[10,10,-2,-5,-6,-3,-4,-7,-19,-21,-22,-20,-16,-18,-23,-24,-17,]),'STRING':([0,2,3,5,6,8,9,12,13,14,15,16,17,18,19,21,22,24,26,29,30,31,35,37,39,42,43,],[11,11,-2,-5,-6,19,11,-3,-4,19,19,-12,-14,-15,-26,-7,-19,19,-13,-21,-22,-20,-16,-18,-23,-24,-17,]),'$end':([1,2,3,5,6,12,13,21,22,29,30,31,35,37,39,42,43,],[0,-1,-2,-5,-6,-3,-4,-7,-19,-21,-22,-20,-16,-18,-23,-24,-17,]),'NEWLINE':([4,10,15,16,17,18,19,22,23,24,26,27,29,32,34,38,40,41,],[13,23,-10,-12,-14,-15,-26,29,30,-8,-13,23,30,39,-11,42,-9,23,]),'DOTS':([7,11,20,36,],[14,-25,27,41,]),'TERM':([8,14,15,16,17,18,19,24,26,],[17,17,17,-12,-14,-15,-26,17,-13,]),'LINE':([10,25,27,33,41,],[22,34,22,40,22,]),'STAR':([11,20,],[-25,28,]),'EXCLAM':([15,16,17,18,19,24,26,],[25,-12,-14,-15,-26,33,-13,]),'TAB':([23,29,30,31,37,39,42,],[32,32,-22,38,38,-23,-24,]),'NUM':([28,],[36,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'Axiom':([0,],[1,]),'All':([0,],[2,]),'Entry':([0,2,],[3,12,]),'Production':([0,2,],[4,4,]),'act':([0,2,],[5,5,]),'Function':([0,2,],[6,6,]),'Identification':([0,2,9,],[7,7,20,]),'Symbols':([8,14,],[15,24,]),'Symbol':([8,14,15,24,],[16,16,26,26,]),'terminal':([8,14,15,24,],[18,18,18,18,]),'String':([10,27,41,],[21,35,43,]),'Strings':([23,29,],[31,37,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> Axiom","S'",1,None,None,None),
  ('Axiom -> All','Axiom',1,'p_Axiom','prog_yacc.py',13),
  ('All -> Entry','All',1,'p_all','prog_yacc.py',17),
  ('All -> All Entry','All',2,'p_All_Entry','prog_yacc.py',21),
  ('Entry -> Production NEWLINE','Entry',2,'p_Entry','prog_yacc.py',25),
  ('Entry -> act','Entry',1,'p_Entry_Action','prog_yacc.py',37),
  ('Entry -> Function','Entry',1,'p_Entry_Function','prog_yacc.py',41),
  ('Function -> FUNCTION String','Function',2,'p_Function','prog_yacc.py',45),
  ('Production -> Identification DOTS Symbols','Production',3,'p_Production','prog_yacc.py',52),
  ('Production -> Identification DOTS Symbols EXCLAM LINE','Production',5,'p_Production_identification_symbols','prog_yacc.py',57),
  ('Production -> BAR Symbols','Production',2,'p_Production_bar_symbols','prog_yacc.py',62),
  ('Production -> BAR Symbols EXCLAM LINE','Production',4,'p_Production_bar_symbols_exclam','prog_yacc.py',68),
  ('Symbols -> Symbol','Symbols',1,'p_Symbols','prog_yacc.py',78),
  ('Symbols -> Symbols Symbol','Symbols',2,'p_Symbols_symbol','prog_yacc.py',82),
  ('Symbol -> TERM','Symbol',1,'p_Symbol','prog_yacc.py',86),
  ('Symbol -> terminal','Symbol',1,'p_Symbol_term','prog_yacc.py',94),
  ('act -> HASH Identification DOTS String','act',4,'p_Action_dot','prog_yacc.py',100),
  ('act -> HASH Identification STAR NUM DOTS String','act',6,'p_Action_star','prog_yacc.py',109),
  ('String -> LINE NEWLINE Strings','String',3,'p_String','prog_yacc.py',123),
  ('String -> LINE','String',1,'p_String_line','prog_yacc.py',127),
  ('String -> NEWLINE Strings','String',2,'p_String_newline','prog_yacc.py',131),
  ('String -> LINE NEWLINE','String',2,'p_String_line_newline','prog_yacc.py',135),
  ('Strings -> NEWLINE','Strings',1,'p_Strings_newline','prog_yacc.py',139),
  ('Strings -> TAB NEWLINE','Strings',2,'p_Strings_tab','prog_yacc.py',143),
  ('Strings -> Strings TAB NEWLINE','Strings',3,'p_Strings_tab_newline','prog_yacc.py',147),
  ('Identification -> STRING','Identification',1,'p_Identification','prog_yacc.py',155),
  ('terminal -> STRING','terminal',1,'p_terminal','prog_yacc.py',159),
]
