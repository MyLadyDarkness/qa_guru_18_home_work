import logging
import json
import allure
import requests
from requests import Response
from allure_commons.types import AttachmentType


def api_request(url, endpoint, method, data=None, params=None, cookies=None):
    request_url = f"{url}{endpoint}"
    response = requests.request(method, request_url, data=data, params=params, cookies=cookies)
    response_logging(response)
    response_attaching(response)

    return response


def response_logging(response: Response):
    logging.info("Request: " + response.request.url)
    if response.request.body:
        logging.info("INFO Request body: " + response.request.body)  # логирование тела запроса если оно есть
    logging.info("Request headers: " + str(response.request.headers))
    logging.info("Response code " + str(response.status_code))
    logging.info("Response: " + response.text)


def response_attaching(response: Response):
    allure.attach(
        body=response.request.url,
        name="Request url",
        attachment_type=AttachmentType.TEXT,
    )

    if response.request.body:  # логирование тела запроса если оно есть
        allure.attach(
            body=json.dumps(response.request.body, indent=4, ensure_ascii=True),
            name="Request body",
            attachment_type=AttachmentType.JSON,
            extension="json",
        )
