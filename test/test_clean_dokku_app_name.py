from dokkusd.util import clean_dokku_app_name


def test_fine_1():
    assert "cat" == clean_dokku_app_name("cat")


def test_bad_1():
    assert "cat-" == clean_dokku_app_name("cat_")


def test_bad_2():
    assert "cat-" == clean_dokku_app_name("cat:")


def test_bad_3():
    assert "cat-" == clean_dokku_app_name("cat/")


def test_bad_4():
    assert "cat-" == clean_dokku_app_name("cat\\")


def test_bad_5():
    assert "cat" == clean_dokku_app_name("CAT")


def test_bad_6():
    assert "cat-" == clean_dokku_app_name("cat ")
