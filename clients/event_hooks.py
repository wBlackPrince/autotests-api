import allure
from httpx import Request, Response
from tools.http.curl import make_curl_from_request
from tools.logger import get_logger

logger = get_logger("HTTP_logger")

def curl_event_hook(request: Request):
    """
    Event hook для автоматического прикрепления cURL-команды к Allure-отчету

    :param request: HTTP-запрос в httpx-client
    """
    curl_command = make_curl_from_request(request)

    allure.attach(curl_command, "cUrl command", allure.attachment_type.TEXT)

def log_request_event_hook(request: Request):
    """
    Event hook для логирования информации об отправленном HttpRequest

    :param request: объект запроса Httpx
    :return:
    """
    logger.info(f"Make {request.method} request to {request.url}")

def log_response_event_hook(response: Response):
    """
    Event hook для логирования информации о полученном HttpResponse

    :param response: объект ответа Httpx
    :return:
    """
    logger.info(f"Got {response.status_code} {response.reason_phrase} from {response.url}")