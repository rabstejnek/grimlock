from grimlock import commands


def test_hello_world():
    assert commands.hello_world(None) == "Hello, World!"
