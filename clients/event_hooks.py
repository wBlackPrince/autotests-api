import allure
from httpx import Request

from tools.http.curl import make_curl_from_request


def curl_event_hook(request: Request):
    """
    Event hook для автоматического прикрепления cURL-команды к Allure-отчету

    :param request: HTTP-запрос в httpx-client
    """
    curl_command = make_curl_from_request(request)

    allure.attach(curl_command, "cUrl command", allure.attachment_type.TEXT)