# Async Requests | Don't Let the Server Down kata
# https://www.codewars.com/kata/6417797d022e4c003ebbd575/train/python

import asyncio
from preloaded import send_request

async def gather_responses_bulk(n: int) -> str:
    res = await asyncio.gather(*[send_request() for i in range(n)])
    return ''.join(res)

async def request_manager(n: int) -> str:
    output = ''
    while n > 0:
        req_count = 150 if n >= 150 else n
        output += await gather_responses_bulk(req_count)
        n -= req_count

    return ''.join(output)
