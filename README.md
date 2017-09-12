# wilddog-sms

![](https://docs.wilddog.com/images/logo-d2df5d3b45.svg)

[Wilddog SMS](https://docs.wilddog.com/sms/index.html) SDK for Python

## Getting started

### 安装:

[download the source code
(ZIP)](https://github.com/WildDogTeam/sms-sdk-python/zipball/master "sms-sdk-python
source code") for `sms-sdk-python`, and then run:

`python setup.py install`

*不同环境下，可能需要root或sudo权限执行*

### 初始化

```python
from wilddog import SmsClient

smsclinet = SmsClient('YOUR_APPID', 'SMS_KEY')
```

### 发送验证码短信

#### 使用野狗生成验证码
```python
mobile = 'PHONE1'
templateId = 'YOUR_TEMPLATE_ID'
res = smsclient.send_code(mobile, templateId, None)
```

#### 使用自生成验证码
```python
templateId = 'YOUR_TEMPLATE_ID'
mobiles = 'PHONE1'
params = "['Var1', 'Var2']"
res = smsclient.send_code(mobile, templateId, params)
```

### 校验验证码

```python
mobile = 'PHONE1'
code = 'USER CAPTCHA'
res = smsclient.check_code(mobile, code)
```

### 发送通知短信

```python
templateId = 'YOUR_TEMPLATE_ID'
mobiles = '["PHONE1", "PHONE2"]'
params = "['Var1', 'Var2']"
res = smsclinet.send_notify(mobiles, templateId, params)
```

### 查询发送状态

```python
rrid = 'The rrid in send_code/send_notify response'
res = smsclient.query_status(rrid)
```

### 查询账户余额

```python
res = smsclient.query_balance()
```