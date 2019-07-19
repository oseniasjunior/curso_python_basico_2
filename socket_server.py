import asyncio
import uvloop


async def callback_server(reader, client):
    data = await reader.read(2048)
    message = data.decode('utf-8')
    print('message: {}'.format(message))
    print('client: {}'.format(client.get_extra_info('peername')))
    client.close()


def create_server(host, port):
    # asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    loop = asyncio.get_event_loop()
    coro = asyncio.start_server(callback_server, host=host, port=port, loop=loop)
    server = loop.run_until_complete(coro)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()


create_server(host='127.0.0.1', port=9004)
