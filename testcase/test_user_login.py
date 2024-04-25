import pytest
import allure
from operation.user import login_user
from testcase.conftest import api_data
from common.Logger import logger

@allure.step("步骤1 ==>> 登录用户")
def step_1(userAccount ):
    logger.info("步骤1 ==>> 登录用户：{}".format(userAccount ))


@allure.severity(allure.severity_level.NORMAL)
@allure.epic("针对登录接口的测试")
@allure.feature("用户登录模块")
class Test_login_user:
    @allure.story("用户登录")
    @allure.description("登录接口的测试用例")
    @allure.issue("http://192.168.16.201/chandao.rantron.biz")
    @allure.testcase("http://chandao.rantron.biz:8083/bug-view-3573.html")
    @allure.title("测试数据：【'userAccount', 'userPwd','rcode', 'scode'】")
    # @pytest.mark.single
    @pytest.mark.parametrize("userAccount, userPwd, rcode, scode", api_data['test_user_login'])
    def test_login(self,userAccount ,userPwd, rcode, scode):
        logger.info("*************** 开始执行用例 ***************")
        step_1(userAccount )
        result = login_user(userAccount ,userPwd)
        print(result)
        assert result.response.status_code == 200
        assert result.response.json().get('rcode') == rcode
        assert result.response.json().get('scode') == scode
        logger.info("*************** 结束执行用例 ***************")


