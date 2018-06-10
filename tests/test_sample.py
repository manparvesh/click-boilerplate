from unittest import TestCase

from click.testing import CliRunner

from projectname import cli


class TestSample(TestCase):
    """
        Sample Test
    """

    def __init__(self, methodName='runTest'):
        super(TestSample, self).__init__()
        self.runner = CliRunner()

    def runTest(self):
        # run cli normally
        result = self.runner.invoke(cli)
        output_string = str(result.output.encode('ascii', 'ignore'))
        self.assertEqual(0, result.exit_code)
        self.assertEqual("Hello, fellow Python programmer!!\n", output_string)

        # run with name only
        result = self.runner.invoke(cli, ['Man'])
        output_string = str(result.output.encode('ascii', 'ignore'))
        self.assertEqual(0, result.exit_code)
        self.assertEqual("Hello, Man!!\n", output_string)

        # run with name and flag
        result = self.runner.invoke(cli, ['--count', '2', 'Man'])
        output_string = str(result.output.encode('ascii', 'ignore'))
        self.assertEqual(0, result.exit_code)
        self.assertEqual("Hello, Man!!\nHello, Man!!\n", output_string)
