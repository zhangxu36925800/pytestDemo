import pytest
@pytest.mark.incremental
class TestAdd:

    def test_01(self):
        print('test_01 用例执行中...')

    def test_02(self):
        pytest.xfail('以后的用例都失败了0')

    def test_03(self):
        print('test_03 用例执行中...')


if __name__ == "__main__":
    pytest.main()
