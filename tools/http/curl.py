import httpx
from httpx import request, Request, RequestNotRead, post, Client


def make_curl_from_request(request: Request):
    """
    Конвертирует данные http-запроса в curl команду

    :param request: Данные http-запроса, из которого будет сформирована curl-строка
    :return: Строка с curl-командой
    """
    result: list[str] = [f"curl -X '{request.method}'", f"{request.url}"]

    for header, value in request.headers.items():
        result.append(f"-H '{header}: {value}'")

    try:
        if body := request.content:
            result.append(f"-d '{body.decode('utf-8')}'")
    except RequestNotRead:
        pass

    return '\\\n '.join(result)