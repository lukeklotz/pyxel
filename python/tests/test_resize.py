# python/tests/test_resize.py


def test_resize_updates_globals(init_pyxel):
    import pyxel

    pyxel.resize(320, 240)
    assert pyxel.width == 320
    assert pyxel.height == 240


def test_resize_updates_gobals_small(init_pyxel):
    import pyxel

    pyxel.resize(64, 64)
    assert pyxel.width == 64
    assert pyxel.height == 64


def test_resize_update_multiple_times(init_pyxel):
    import pyxel

    pyxel.resize(320, 240)
    assert pyxel.width == 320
    assert pyxel.height == 240

    pyxel.resize(64, 64)
    assert pyxel.width == 64
    assert pyxel.height == 64

    pyxel.resize(128, 128)
    assert pyxel.width == 128
    assert pyxel.height == 128


def test_resize_invalid(init_pyxel):
    import pyxel

    try:
        pyxel.resize(-1, 240)
        assert False, "Expected ValueError for negative width"
    except OverflowError:
        pass

    try:
        pyxel.resize(320, -1)
        assert False, "Expected ValueError for negative height"
    except OverflowError:
        pass

    try:
        pyxel.resize(0, 240)
        assert False, "Expected ValueError for zero width"
    except ValueError:
        pass

    try:
        pyxel.resize(320, 0)
        assert False, "Expected ValueError for zero height"
    except ValueError:
        pass
