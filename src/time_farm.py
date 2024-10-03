import requests

from src.api_constant import ApiConstant


class TimeFarmAuto:

    def __init__(self, init_data, platform):
        self.init_data = init_data
        self.platform = platform

    def auth(self):
        payload = {"initData": self.init_data, "platform": self.platform}
        headers = {"Content-Type": "application/json"}
        proxies = {"https": "https://172.20.10.1:1082"}
        try:
            response = requests.post(
                ApiConstant.TimeFarm.Login,
                json=payload,
                proxies=proxies,
                headers=headers,
                verify=False,  # Disable SSL verification
            )
            response.raise_for_status()  # Check for HTTP errors
            return response.json()  # Return the API response
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None
