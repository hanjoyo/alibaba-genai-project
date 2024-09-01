from http import HTTPStatus
import dashscope
from dashscope import Application

dashscope.base_http_api_url = 'https://dashscope-intl.aliyuncs.com/api/v1'

def call_with_stream(query):
    messages = [
        {'role': 'user', 'content': query}]
    
    response = Application.call(app_id='aadcb110701d46259242032e022f3af8',
                                prompt=query,
                             api_key='sk-c0f01f27c2a948db8bf81ee78dcf264d',)
    if response.status_code == HTTPStatus.OK:
        print(response.output,end='')
        return response.output
    else:
        print('Request id: %s, Status code: %s, error code: %s, error message: %s' % (
            response.request_id, response.status_code,
            response.code, response.message
        ))
        return f'Request id: {response.request_id}, Status code: {response.status_code}, error code: {response.code}, error message: {response.message}'
