########################
import requests
import json
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials

scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

credentials = Credentials.from_service_account_file(
    'lego-hangang-2020-e30ccd2df9c8.json',
    scopes=scopes
)

gc = gspread.authorize(credentials)


spreadsheet_url = 'https://docs.google.com/spreadsheets/d/1RjMijAbTt2K1WIQlTPX5_hxu2xS6qNQQx0EXtTgc6gg/edit#gid=0'

# 스프레스시트 문서 가져오기
doc = gc.open_by_url(spreadsheet_url)

# 시트 선택하기
worksheet = doc.worksheet('여의도')

url = 'https://pcmap-api.place.naver.com/graphql'
query = """query {
    restaurants {
    items {
      name
      microReview
      priceCategory
      roadAddress
      visitorReviewScore
      blogCafeReviewCount
      businessCategory
      businessHours
      category
    }
  }
}"""

r = requests.post(url, json={'query': query})
json_data = json.loads(r.text)
df_data = json_data["restaurants"]["items"]
df = pd.DataFrame(df_data)
##########################################