"""
C'Dent Python parser grammar module.
"""

from cdent.grammar import *

class Grammar():
    def __init__(self):
        self.__dict__.update(
{ 'BlankLine': Re({'_': '[\\ \\t]*\\r?\\n'}),
  'Class': All({'_': [Rule({'_': 'ClassSignature'}), Rule({'_': 'ClassBody'})]}),
  'ClassBody': All({'_': [Indent({}), Rule({'x': '*', '_': 'Comment'}), Rule({'_': 'Method'}), Any({'x': '*', '_': [Rule({'_': 'Method'}), Rule({'_': 'Comment'})]}), Undent({})]}),
  'ClassSignature': Re({'_': 'class[\\ \\t]+\\w+\\((?:\\w+)?\\):\\r?\\n'}),
  'Comment': Any({'_': [Rule({'_': 'LineComment'}), Rule({'_': 'BlankLine'})]}),
  'DocComment': All({'_': [Rule({'_': 'DocCommentBegin'}), All({'x': '*', '_': [Rule({'!': True, '_': 'DocCommentEnd'}), Rule({'_': 'DocCommentLine'})]}), Rule({'_': 'DocCommentEnd'})]}),
  'DocCommentBegin': Re({'_': '"""\\\\[\\ \\t]*\\r?\\n'}),
  'DocCommentEnd': Re({'_': '"""[\\ \\t]*\\r?\\n'}),
  'DocCommentLine': Re({'_': '(.*\\r?\\n)'}),
  'Ending': Re({'_': ''}),
  'Id': Re({'_': '\\w+'}),
  'IncludeCDent': Re({'_': 'from cdent import \\*'}),
  'Line': Re({'_': '.*\\r?\\n'}),
  'LineComment': Re({'_': '#(.*\\r?\\n)'}),
  'Method': All({'_': [Rule({'_': 'MethodSignature'}), Rule({'_': 'MethodBody'})]}),
  'MethodBody': All({'_': [Indent({}), Rule({'x': '+', '_': 'Statement'}), Undent({})]}),
  'MethodSignature': Re({'_': '^def[\\ \\t]+\\w+\\((?:\\w+)?\\):\\r?\\n'}),
  'Module': All({'_': [Rule({'x': '?', '_': 'DocComment'}), Rule({'x': '*', '_': 'Comment'}), Rule({'x': '?', '_': 'IncludeCDent'}), Rule({'x': '*', '_': 'Comment'}), Rule({'_': 'Class'}), Any({'x': '*', '_': [Rule({'_': 'Class'}), Rule({'_': 'Comment'})]}), Rule({'_': 'Ending'}), Rule({'x': '*', '_': 'Comment'})]}),
  'PrintLn': Re({'_': 'print[\\ \\t]+(.+)\\r?\\n'}),
  'Statement': Any({'_': [Rule({'_': 'PrintLn'}), Rule({'_': 'Comment'})]}),
  'line_comment_start': Re({'_': '#'})}
)

