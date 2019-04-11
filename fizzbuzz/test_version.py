import pytest

"""
@pytest.fixture
def v():
    from version import Version
    version = Version(1, 4, 2)
    version = Version(-1, 4, 2)
    return version
"""


class TestVersion():

    class Testどれかのフィールドが負だとエラーを返す:

        @pytest.mark.do
        def test_バージョンのmajorフィールドが負だとエラーを返す(self):
            from version import Version
            try:
                Version(-1, 1, 1)
                assert False
            except(Exception):
                pass

        @pytest.mark.do
        def test_バージョンのminorフィールドが負だとエラーを返す(self):
            from version import Version
            try:
                Version(1, -1, 1)
                assert False
            except(Exception):
                pass

        @pytest.mark.do
        def test_バージョンのpatchフィールドが負だとエラーを返す(self):
            from version import Version
            try:
                Version(1, 1, -1)
                assert False
            except(Exception):
                pass

    def test_オブジェクトが文字列表現を返す(self):
        from version import Version
        v = Version(1, 1, 1)
        assert str(v) == '1.1.1'

    class Testバージョンオブジェクトは透過性比較や大小比較ができる():
        def test_Ver1_4_2_NE_Ver2_1_0(self):
            from version import Version
            v1 = Version(1, 4, 2)
            v2 = Version(2, 1, 0)
            assert v1 != v2

        def test_Ver10_3_5_EQ_Ver10_3_5(self):
            from version import Version
            v1 = Version(10, 3, 5)
            v2 = Version(10, 3, 5)
            assert v1 == v2

        def test_Ver2_23_1_LT_Ver5_1_2(self):
            from version import Version
            v1 = Version(2, 23, 1)
            v2 = Version(5, 1, 2)
            assert v1 < v2
