# in ra câu chào
from src.time_farm import TimeFarmAuto



def time_farm():
    payload = {
        "initData": "query_id=AAHXyw8yAgAAANfLDzLmZyP_&user=%7B%22id%22%3A5134863319%2C%22first_name%22%3A%22Sen%F0%9F%90%88%E2%80%8D%E2%AC%9B%22%2C%22last_name%22%3A%22%22%2C%22username%22%3A%22senms9x%22%2C%22language_code%22%3A%22en%22%2C%22allows_write_to_pm%22%3Atrue%7D&auth_date=1727924055&hash=9012a808635366c32e4ee17e49c8e5fef34b9bc65d82fe6bedd5678d80c119d7",
        "platform": "ios",
    }
    timeFarm = TimeFarmAuto(payload, "ios")
    timeFarm.auth()
    

# check if main
if __name__ == "__main__":
    print("Welcome to Airdrop Automation Tool")
    print("Timefarm starting....")
    print("Timefarm login....")
    time_farm()