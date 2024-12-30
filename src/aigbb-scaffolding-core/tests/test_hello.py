from aigbb_scaffolding_core import hello

class TestHello:
    def test_hello(self):
        assert hello("test") == "Hello test from aigbb_scaffolding_core!"
