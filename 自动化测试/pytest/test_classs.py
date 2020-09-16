# -*- coding：utf-8 -*-
'''
UI自动化全部打开浏览器，只执行一次

'''
import pytest
#login是登录，要加到购物车和支付之前，是他们依赖方法 fixture
# @pytest.fixture()
@pytest.fixture(scope='module',autouse=True)
def open_browser():
    print("打开浏览器，登录")
    yield
    print('关闭浏览器')
@pytest.fixture()
def login():
    print('登录')
def test_search():
    print("root")
@pytest.mark.usefixtures('login')
def test_cart():
    print("pin")
def test_pay():
    print("job")

if __name__ == '__main__':
        pytest.main()