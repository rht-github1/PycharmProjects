import pytest
import allure

@allure.feature("这是一个加法的计算器，加数{0}与加数{1}相加功能")
def add_caculator(num1,num2):
    sum = num1+num2
    return sum

@allure.testcase('www.baidu.com','这是测试连接')
@allure.description('这是加法的计算器测试加法的各种情况结果是否正确')
@allure.story('正确的测试用例')
@pytest.mark.parametrize("num1,num2,result",[[1,2, 3], [3,12, 15],[1,4,5]],ids=["10以内","10以外","小数"])
def test_add_caculator(num1,num2,result):
    with allure.step("如果错误截图"):
        allure.attach.file("1.png", attachment_type=allure.attachment_type.PNG)
        allure.attach("加数1+加数2=","{0},{1},{2}")
        sum=add_caculator(num1,num2)
        allure.attach("<html><body>这是我们要测试的加法</body></html>")
        assert sum ==result