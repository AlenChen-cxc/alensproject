from alensproject.lib import try_me

def test_try_me():
    assert try_me(5) > 0
    assert try_me(0) == 0
    assert try_me(3) == 6
