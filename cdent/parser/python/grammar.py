"""
C'Dent Python parser grammar module.
"""

from cdent.grammar import *

class Grammar():
    def __init__(self):
        self.__dict__.update(
{ 'BlankLine': Re({'_': '[\\ \\t]*\\r?\\n'}),
  'Class': All({'_': [Rule({'_': 'ClassSignature'}), Rule({'_': 'ClassBody'})]}),
  'ClassBody': All({'_': [Indent({}), Any({'x': '*', '_': [Rule({'_': 'Method'}), Rule({'_': 'Comment'})]}), Undent({})]}),
  'ClassSignature': Re({'_': 'class[\\ \\t]+\\w+\\((?:\\w+)?\\):\\r?\\n'}),
  'Comment': Any({'_': [Rule({'_': 'LineComment'}), Rule({'_': 'BlankLine'})]}),
  'DocComment': All({'_': [Rule({'_': 'DocCommentBegin'}), All({'x': '*', '_': [Not({'_': Rule({'_': 'DocCommentEnd'})}), Rule({'_': 'DocCommentLine'})]}), Rule({'_': 'DocCommentEnd'})]}),
  'DocCommentBegin': Re({'_': '"""\\\\[\\ \\t]*\\r?\\n'}),
  'DocCommentEnd': Re({'_': '"""[\\ \\t]*\\r?\\n'}),
  'DocCommentLine': Re({'_': '(.*\\r?\\n)'}),
  'Ending': Re({'_': ''}),
  'Id': Re({'_': '\\w+'}),
  'IncludeCDent': Re({'_': 'from cdent import \\*'}),
  'Line': Re({'_': '.*\\r?\\n'}),
  'LineComment': Re({'_': '#(.*\\r?\\n)'}),
  'Method': All({'_': [Rule({'_': 'MethodSignature'}), Rule({'_': 'MethodBody'})]}),
  'MethodSignature': Re({'_': '^def[\\ \\t]+\\w+\\((?:\\w+)?\\):\\r?\\n'}),
  'Module': All({'_': [Rule({'_': 'DocComment'}), Rule({'x': '*', '_': 'Comment'}), Rule({'_': 'IncludeCDent'}), Rule({'x': '*', '_': 'Comment'}), Rule({'_': 'Class'}), Any({'x': '*', '_': [Rule({'_': 'Class'}), Rule({'_': 'Comment'})]}), Rule({'_': 'Ending'}), Rule({'x': '*', '_': 'Comments'})]}),
  'line_comment_start': Re({'_': '#'})}
)

