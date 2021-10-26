# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.

from typing import List
from linglufa.settings import ACCESS_KEY_ID,ACCESS_KEY_SECRET

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
from aliyunsdkcore.auth.credentials import AccessKeyCredential
from aliyunsdkcore.auth.credentials import StsTokenCredential

def send_sms(PhoneNumbers,SignName,TemplateCode,TemplateParam):
    credentials = AccessKeyCredential(ACCESS_KEY_ID, ACCESS_KEY_SECRET)
    client = AcsClient(region_id='cn-shenzhen', credential=credentials)
    request = CommonRequest()
    request.set_accept_format('json')
    request.set_domain('dysmsapi.aliyuncs.com')
    request.set_method('POST')
    request.set_protocol_type('https')  # https | http
    request.set_version('2017-05-25')
    request.set_action_name('SendSms')

    request.add_query_param('PhoneNumbers', PhoneNumbers)
    request.add_query_param('SignName', SignName)
    request.add_query_param('TemplateCode', TemplateCode)
    request.add_query_param('TemplateParam', TemplateParam)

    response = client.do_action(request)

    # python2:  print(response)
    print(str(response, encoding='utf-8'))

#用法参考
# send_sms('18388588491','领路发','SMS_226840048','{"code":888888}')