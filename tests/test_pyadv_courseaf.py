from pyadv_courseaf import algos

def test_add_one():
    out = algos.add_one(2)
    assert out == 2, f'output should be 2 but is {out}'

def test_add_two():
    out = algos.add_one(2)
    assert out == 3