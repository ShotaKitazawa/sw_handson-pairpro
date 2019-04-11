import pytest

from version import Version


def pytest_generate_tests(metafunc):
    """
    Parametrizing test methods through per-class configuration
    http://pytest.org/latest-ja/example/parametrize.html#id5
    """
    try:
        funcarglist = metafunc.cls.params[metafunc.function.__name__]
    except AttributeError:
        return
    argnames = list(funcarglist[0])
    metafunc.parametrize(
        argnames,
        [[funcargs[name] for name in argnames] for funcargs in funcarglist]
    )


class TestVersion():

    @pytest.mark.one
    class Testどれかのフィールドが負だとエラーを返す:

        def test_バージョンのmajorフィールドが負だとエラーを返す(self):
            try:
                Version(-1, 1, 1)
                assert False
            except(Exception):
                pass

        def test_バージョンのminorフィールドが負だとエラーを返す(self):
            try:
                Version(1, -1, 1)
                assert False
            except(Exception):
                pass

        def test_バージョンのpatchフィールドが負だとエラーを返す(self):
            try:
                Version(1, 1, -1)
                assert False
            except(Exception):
                pass

    @pytest.mark.two
    def test_オブジェクトが文字列表現を返す(self):
        assert str(Version(1, 1, 1)) == '1.1.1'

    @pytest.mark.three
    class Testバージョンオブジェクトは透過性比較や大小比較ができる():
        def test_Ver1_4_2_NE_Ver2_1_0(self):
            assert Version(1, 4, 2) != Version(2, 1, 0)

        def test_Ver10_3_5_EQ_Ver10_3_5(self):
            assert Version(10, 3, 5) == Version(10, 3, 5)

        def test_Ver2_23_1_LT_Ver5_1_2(self):
            assert Version(2, 23, 1) < Version(5, 1, 2)

        def test_Ver10_3_5_GT_Ver2_23_1(self):
            assert Version(10, 3, 5) > Version(2, 23, 1)

        def test_Ver2_23_1_LE_Ver5_1_2(self):
            assert Version(2, 23, 1) <= Version(5, 1, 2)

        def test_Ver10_3_5_GE_Ver10_3_5(self):
            assert Version(10, 3, 5) >= Version(10, 3, 5)
