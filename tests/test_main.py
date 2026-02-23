from n4.main import hello_world


def test_main():
    assert hello_world("foo") == "foo"
