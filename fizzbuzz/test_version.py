import pytest

from version import Version


def _field_check(major, minor, patch, err):
    try:
        Version(major, minor, patch)
        assert False
    except(err):
        pass


class TestVersion():

    class Test各フィールドを評価():

        class Test各フィールドが負だとエラー():

            def test_バージョンのmajorフィールドが負だとエラー(self):
                _field_check(-1, 1, 1, ValueError)

            def test_バージョンのminorフィールドが負だとエラー(self):
                _field_check(1, -1, 1, ValueError)

            def test_バージョンのpatchフィールドが負だとエラー(self):
                _field_check(1, 1, -1, ValueError)

        class Test各フィールドが文字列だとエラー():
            def test_バージョンのmajorフィールドが文字列だとエラー(self):
                _field_check("1", 1, 1, TypeError)

            def test_バージョンのminorフィールドが文字列だとエラー(self):
                _field_check(1, "1", 1, TypeError)

            def test_バージョンのpatchフィールドが文字列だとエラー(self):
                _field_check(1, 1, "1", TypeError)

        class Test各フィールドが小数だとエラー():
            def test_バージョンのmajorフィールドが小数だとエラー(self):
                _field_check(1.1, 1, 1, TypeError)

            def test_バージョンのminorフィールドが小数だとエラー(self):
                _field_check(1, 1.1, 1, TypeError)

            def test_バージョンのpatchフィールドが小数だとエラー(self):
                _field_check(1, 1, 1.1, TypeError)

    def test_オブジェクトが文字列表現(self):
        assert str(Version(1, 1, 1)) == '1.1.1'

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
