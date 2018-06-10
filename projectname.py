import click


@click.group(invoke_without_command=True)
@click.argument('name', nargs=1, required=False)
@click.option('-c', '--count')
def cli(name, count):
    """
    Simple example of a click application for writing
    complex command line applications in python
    """
    if count is None:
        count = 1
    if name is None:
        name = 'fellow Python programmer'
    for _ in range(int(count)):
        print('Hello, ' + name + '!!')
