import logging
from typing import List

import requests

logger = logging.getLogger(__name__)

API_TIMEOUT_SECONDS = 60


class StoreOrderApiError(Exception):
    def __init__(self, msg, response):
        super().__init__(msg)
        self.msg = msg
        self.response = response


class StoreOrderClient:
    """
    Клиент для работы с warehouse api
    """

    def __init__(self, endpoint, token):
        """
        :param endpoint:
        :param token:
        """
        self._endpoint = endpoint
        self._token = token

    def products(self, ids: List[str]):
        """
        :param ids: Unique identifier for the products.
        :return:
        """
        url = f"{self._endpoint}"

        logging.debug('Request products report for {ids}'.format(ids=','.join(ids)))
        response = requests.request(
            method="POST",
            url=url,
            json={"ids": list(ids)}
        )
        logging.debug('Response products report for {ids} is {response_text}'
                      .format(ids=','.join(ids), response_text=response.text))

        if response.status_code != 200:
            raise StoreOrderApiError(f"API error. Error code {response.status_code}", response)

        return response.json()
