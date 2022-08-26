import pytest


class TestSample1:
    def test_001(self):
        globals().setdefault("test1", "我是")
        globals().setdefault("test2", "zhangxu")
        aa = globals().get("test1")
        bb = globals().get("test2")
        print(aa,bb)


testsample = TestSample1()
testsample.test_001()
