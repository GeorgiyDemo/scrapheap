# content of test_sample.py
def inc(x):
    return x + 1


def test_answer():
    for i in range(100):
        assert inc(i) == i+1

def test_check():
    assert inc(3) == 4