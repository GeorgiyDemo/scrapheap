from io import StringIO
import double


number_inputs1 = StringIO('1234\n2')
number_inputs2 = StringIO('2')

def test_double(monkeypatch):
    monkeypatch.setattr('sys.stdin', number_inputs1)
    assert double.double() == 2468

def test_str(monkeypatch):
    monkeypatch.setattr('sys.stdin', number_inputs2)
    assert double.i_str() == number_inputs2