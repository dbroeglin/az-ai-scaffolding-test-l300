from az_ai_scaffolding_core import hello

class TestHello:
    def test_hello(self):
        assert hello("test") == "Hello test from az_ai_scaffolding_core!"
