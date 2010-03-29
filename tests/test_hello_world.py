import sys
import os

import cdent.test

class TestHelloWorld(cdent.test.TestCase):
    cmds = [
        'PYTHONPATH=. python bin/cdent --compile --from=yaml --to=py --input=hello-world/World.cd --output=output',
        'PYTHONPATH=. python bin/cdent --compile --from=yaml --to=pm --input=hello-world/World.cd --output=output',
        'PYTHONPATH=. python bin/cdent --compile --from=yaml --to=js --input=hello-world/World.cd --output=output',
        'PYTHONPATH=. python bin/cdent --compile --from=yaml --to=rb --input=hello-world/World.cd --output=output',
        'cd hello-world; js hello_world.js',
        'cd hello-world; php hello_world.php',
        'cd hello-world; perl6 hello_world.p6',
        'cd hello-world; perl hello_world.pl',
        'cd hello-world; python hello_world.py',
        'cd hello-world; python3 hello_world.py3',
        'cd hello-world; ruby hello_world.rb',
        '# Done',
    ]

    def test_commands(self):
        for cmd in self.cmds:
            print cmd
            rc = os.system(cmd)
            self.assertTrue(rc == 0, "Command: %s" % cmd)

    def tearDown(self):
        if os.path.exists('output'):
            os.unlink('output')

if __name__ == '__main__':
    cdent.test.main()