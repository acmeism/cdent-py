"""\
JavaScript code generator for C'Dent
"""

from cdent.generator import Generator as Base

class Generator(Base):
    def gen_comment(self, comment):
        for line in comment.val.splitlines():
            self.writeln('// %s' % line)
        self.writeln()

    def gen_class(self, klass): 
        name = klass.name
        self.writeln('(this.%s = function() {}).prototype = {' % name)
        self.indent()
        for node in klass.has:
            self.dispatch(node)
        self.undent()
        self.writeln('}')

    def gen_method(self, method): 
        name = method.name
        self.writeln(name + ': function() {')
        self.indent()
        for node in method.has:
            self.dispatch(node)
        self.undent()
        self.writeln('}')

    def gen_println(self, builtin): 
        self.write('print(', indent=True)
        for node in builtin.args:
            self.dispatch(node)
        self.writeln(');', indent=False)

    def gen_return(self, ret): 
        self.writeln('return;')
