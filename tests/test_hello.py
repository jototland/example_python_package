# This is an example unit test using `pytest`

from mypackage import hello


def test_hello(capsys):
    hello()
    written = capsys.readouterr()
    assert 'Hello, World!' in written.out
    assert 'hello.txt' in written.out
