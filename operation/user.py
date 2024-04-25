from core.result_base import ResultBase
from api.user import user
from common.Logger import logger

def login_user(userAccount ,userPwd):
    '''
    :param userAccount:账户
    :param userPwd:密码
    :return res.cookies
    '''
    result = ResultBase()
    data = {
        "userAccount": userAccount ,
        "userPwd": userPwd
    }

    res = user.login(data=data, verify =False)
    result.response = res
    result.success = False
    if res.json()['rcode'] == 0:
        result.success = True
    else:
        result.error = "登录用户 ==>> 接口返回码是 【 {} 】".format(res.json()["rcode"])

    logger.info("登录操作 ==>> 返回结果 ==>> {}".format(result.response.text))
    return  result



