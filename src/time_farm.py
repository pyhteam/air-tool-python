import requests

from src.api_constant import ApiConstant

class TimeFarmAuto:
    
    def __init__(self, init_data, platform):
        self.init_data = init_data
        self.platform = platform
        
    def auth(self):
        payload = {
            "initData": self.init_data,
            "platform": self.platform
        }
        try:
            response = requests.post(ApiConstant.TimeFarm.Login, json=payload)
            response.raise_for_status()  # Kiểm tra lỗi HTTP
            return response.json()  # Trả về kết quả từ API
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None