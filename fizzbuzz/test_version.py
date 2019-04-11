import pytest


@pytest.fixture
def v():
    from version import Version
    version = Version(1, 4, 2)
    version = Version(-1, 4, 2)
    return version


class TestVersion():

    # @pytest.mark.do
    def test_バージョンのmajorフィールドが正(self):
        from version import Version
        v = Version(1, 1, 1)
        assert v.major >= 0

    @pytest.mark.do
    def test_バージョンのmajorフィールドが負だとエラーを返す(self):
        from version import Version
        try:
            Version(-1, 1, 1)
            assert False
        except(Exception):
            pass

    def test_バージョンのminorフィールドが負だとエラーを返す(self, v):
        from version import Version
        flag = False
        try:
            Version(1, -1, 1)
        except(Exception):
            flag = True
        finally:
            assert flag

    def test_バージョンのpatchフィールドが負だとエラーを返す(self, v):
        from version import Version
        flag = False
        try:
            Version(1, 1, -1)
        except(Exception):
            flag = True
        finally:
            assert flag
