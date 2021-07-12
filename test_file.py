from hello_niksingh710 import say_hello


def test_say_hello_no_params():
    assert say_hello() == "Hello, World! :)"


def test_say_hello_with_params():
    assert say_hello("Everyone") == "Hello, Everyone :)"
