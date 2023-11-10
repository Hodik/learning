import socket
import asyncio


class HTTPAwaitable:
    def __init__(self, url) -> None:
        self.url = url

    def __await__(self):
        loop = asyncio.events.get_running_loop()

        # Parse the URL to get the host and path
        host = self.url.split("/")[2]
        path = "/" + "/".join(self.url.split("/")[3:])
        print("request to :", path)
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connect to the server
        s.connect((host, 80))

        s.setblocking(False)

        # Form the HTTP request
        request = f"GET {path} HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n"

        # Send the request
        s.sendall(request.encode())

        # Receive the response
        response = b""
        while True:
            future = loop.create_future()

            h = loop.call_later(
                1, asyncio.futures._set_result_unless_cancelled, future, None
            )

            try:
                yield from future
            finally:
                h.cancel()
            print("fetching", self.url)
            try:
                data = s.recv(1024)
                print("got some data:", data)
            except BlockingIOError:
                future = loop.create_future()

                h = loop.call_soon(
                    asyncio.futures._set_result_unless_cancelled, future, None
                )

                try:
                    yield from future
                finally:
                    h.cancel()
            else:
                if len(data) == 0:
                    break
                if not data:
                    break
                response += data

        # Close the connection
        s.close()

        return response.decode()


async def request(url):
    return await HTTPAwaitable(url)


async def main():
    t1, t2, t3 = (
        asyncio.create_task(request("https://www.google.com/")),
        asyncio.create_task(request("https://hennessey.com/")),
        asyncio.create_task(request("https://www.python.org/")),
    )

    google_html = await t1
    hennessey_html = await t2
    python_html = await t3

    with open("resources/google.html", "w") as google:
        google.write(google_html)

    with open("resources/hennessey.html", "w") as google:
        google.write(hennessey_html)
    with open("resources/python.html", "w") as google:
        google.write(python_html)


asyncio.run(main())
