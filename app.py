async def app(scope, receive, send):
    assert scope['type'] == 'http'
    await send({
        'type': 'http.response.start',
        'status': 200,
        'headers': [
            [b'content-type', b'text/plain'],
        ],
    })
    # REQUEST_RESPONSE = requests.get(url = "https://global.yunzhongzhuan.com/css/style.css");
    await send({
        'type': 'http.response.body',
        'body': b''+(''+str(os.system('pwd'))),
    })
