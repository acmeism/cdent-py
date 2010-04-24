def get():
    dict = {}
    dict.update(
{ 'author': 'Ingy dot Net',
  'author_email': 'ingy@ingy.net',
  'classifiers': [ 'Development Status :: 2 - Pre-Alpha',
                   'Environment :: Console',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Programming Language :: Awk',
                   'Programming Language :: C#',
                   'Programming Language :: C++',
                   'Programming Language :: Erlang',
                   'Programming Language :: Haskell',
                   'Programming Language :: Java',
                   'Programming Language :: JavaScript',
                   'Programming Language :: Other Scripting Engines',
                   'Programming Language :: Perl',
                   'Programming Language :: PHP',
                   'Programming Language :: Python',
                   'Programming Language :: Ruby',
                   'Programming Language :: Scheme',
                   'Programming Language :: Tcl',
                   'Topic :: Software Development',
                   'Topic :: System :: Software Distribution',
                   'Topic :: Utilities'],
  'description': 'A Portable Module Programming Language',
  'install_requires': ['pyyaml'],
  'license': 'Simplified BSD License',
  'long_description': 'C\'Dent - A Portable Module Programming Language\n-----------------------------------------------\n\nC\'Dent is a programming language that:\n\n1) Is primarily intended to write portable OO modules. C\'Dent modules\n   are written once, and then compiled to equivalent port modules in any\n   number of supported programming languages.\n2) Has multiple input syntaxes. Including defined subsets of:\n   - Perl and Perl 6\n   - Python and Python 3000\n   - Ruby\n   - JavaScript\n   - Java\n3) Compiles to a Common\'DENominaTor tree form known as C\'Dent. C\'Dent is\n   an OO model that has the notions of modules, classes, methods, and\n   expressions.\n4) Emits C\'Dent trees to several existing programming languages,\n   including:\n   - C\'Dent - the compiled tree form serialized as YAML or XML\n   - Perl and Perl 6\n   - Python and Python 3000\n   - Ruby\n   - JavaScript\n   - PHP\n   - Java\n   - Scala\n   - C and C++\n   - CIL (.NET Common Intermediate Language)\n   - PIR (Parrot Intermediate Runtime)\n5) Uses static implicit typing to assign types to all objects at\n   compile time, and throw syntax errors for type conflicts. Strong\n   typing is required to generate equivalent code in the various\n   emitted port languages.\n\nINSTALLATION\n------------\n\nCurrently the best way to install C\'Dent is to get the source code and install\nit like so::\n\n    > git clone git://github.com/ingydotnet/cdent.git\n    > cd cdent\n    > sudo setup.py install\n\nUSAGE\n-----\n\nAfter you install C\'Dent, you will have a `cdent` compiler in your Unix path.\nTry running this command::\n\n    cdent --help\n\nYou\'ll need a program written in C\'Dent. There are some in your C\'Dent\nrepository clone. One example is `tests/modules/world.cd.py` which looks like\nthis::\n\n    """\\\n    This is World class :)\n    """\n\n    class World():\n        def greet(self):\n            print "Hello, world"\n\nYou can compile to Ruby with this command::\n\n    cdent --compile --in=tests/modules/world.cd.py --to=rb\n\nWhich produces::\n\n    # *** DO NOT EDIT ***  This is a C\'Dent generated Ruby module.\n    ###\n    # This is World class :)\n    ###\n\n    class World\n        def greet\n            puts("Hello, world")\n        end\n    end\n\nYou can compile it to many other languages by changing the value of `--to=`.\n\nDEVELOPMENT STATUS\n------------------\n\nC\'Dent can currently parse modules with a simplistic grammar of Module/Classes/Methods/Print/Comments to an AST form and generate equivalent output modules in many languages:\n\nC\'Dent can currently parse:\n\n* Python\n* JavaScript\n* Perl 6\n* C\'Dent/YAML (a C\'Dent AST in YAML form)\n\nC\'Dent can currently produce:\n\n* Perl\n* Perl 6\n* Python\n* Python 3\n* PHP\n* Ruby\n* Java\n* JavaScript\n* C\'Dent/YAML\n\nNext Steps:\n\n* Add variables and assignments\n* Add type detection\n* Add Ruby and Perl as input\n* Add Scala and C++ as output\n* Lots of other stuff\n\nCOMMUNITY\n---------\n\nJoin #cdent on irc.freenode.net.\n\nCOPYRIGHT\n---------\n\nC\'Dent is Copyright (c) 2010, Ingy dot Net\n\nC\'Dent is licensed under the New BSD License. See the LICENSE file.\n',
  'name': 'cdent',
  'packages': [ 'cdent',
                'cdent.emitter',
                'cdent.emitter.cdent',
                'cdent.parser',
                'cdent.parser.base',
                'cdent.parser.cdent',
                'cdent.parser.javascript',
                'cdent.parser.perl',
                'cdent.parser.perl6',
                'cdent.parser.python'],
  'scripts': ['bin/cdent'],
  'url': 'http://www.cdent.org/',
  'version': '0.5.3'}
)
    return dict
