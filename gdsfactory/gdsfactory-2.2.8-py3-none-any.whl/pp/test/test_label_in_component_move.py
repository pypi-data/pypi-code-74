import pp


def component_with_label_float():
    c = pp.Component("ellipse_with_label")
    c << pp.c.ellipse()
    c.add_label(text="demo", position=(0.0, 0.0), layer=pp.LAYER.TEXT)
    return c


def component_with_label_int():
    c = pp.Component("ellipse_with_label")
    c << pp.c.ellipse()
    c.add_label(text="demo", position=(0, 0), layer=pp.LAYER.TEXT)
    return c


def test_move_float_with_int():
    """ fixed """
    c = component_with_label_float()
    c.x = 10
    c.movex(10)


def test_move_int_with_float():
    """ needs fixing """
    c = component_with_label_int()
    c.x = 10.0
    c.movex(10.0)


if __name__ == "__main__":
    test_move_float_with_int()
    test_move_int_with_float()
    # c = component_with_label()
    # c.x = 10.0
    # pp.show(c)
