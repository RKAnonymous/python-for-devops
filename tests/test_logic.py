from mylib.logic import wiki


def test_wiki():
    result = wiki()
    assert result is not None and "Uzbekistan" in result