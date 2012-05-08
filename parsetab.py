
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.2'

_lr_method = 'LALR'

_lr_signature = 'M\xe3\x9a\xea\x93\xf0\x83\xa5O\x81c\xe6.\xa7\x96\xa6'
    
_lr_action_items = {'SET':([0,3,4,8,9,10,11,12,],[1,-6,1,-1,-3,-4,-2,-5,]),'STRING':([7,],[8,]),'FLOAT':([7,],[9,]),'EQUAL':([5,],[7,]),'DELIMITER':([8,9,10,11,],[-1,-3,12,-2,]),'VARIABLE':([1,],[5,]),'INTEGER':([7,],[11,]),'$end':([2,3,6,8,9,10,11,12,],[0,-6,-7,-1,-3,-4,-2,-5,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'setstatement':([0,4,],[3,3,]),'compoundstatement':([0,],[2,]),'value':([7,],[10,]),'statement':([0,4,],[4,6,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> compoundstatement","S'",1,None,None,None),
  ('value -> STRING','value',1,'p_value','mparser.py',11),
  ('value -> INTEGER','value',1,'p_value','mparser.py',12),
  ('value -> FLOAT','value',1,'p_value','mparser.py',13),
  ('setstatement -> SET VARIABLE EQUAL value','setstatement',4,'p_setstatement','mparser.py',18),
  ('setstatement -> SET VARIABLE EQUAL value DELIMITER','setstatement',5,'p_setstatement','mparser.py',19),
  ('statement -> setstatement','statement',1,'p_statement','mparser.py',25),
  ('compoundstatement -> statement statement','compoundstatement',2,'p_compoundstatement','mparser.py',32),
]