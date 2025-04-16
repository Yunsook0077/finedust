import streamlit as st
import requests

# 대도시와 해당 지역의 미세먼지 API parameter 설정
cities = {
    "서울": "서울특별시",
    "부산": "부산광역시",
    "대구": "대구광역시",
    "인천": "인천광역시",
    "대전": "대전광역시",
    "광주": "광주광역시",
    "울산": "울산광역시",
    "세종": "세종특별자치시",
    "경기도": "경기도",
    "강원도": "강원도",
    "충청북도": "충청북도",
    "충청남도": "충청남도",
    "전라북도": "전라북도",
    "전라남도": "전라남도",
    "경상북도": "경상북도",
    "경상남도": "경상남도",
    "제주도": "제주특별자치도"
}

# Streamlit 앱 시작
st.title("대한민국 대도시 미세먼지 농도 조회")

# 선택 옵션
city_selected = st.selectbox("대도시를 선택하세요:", list(cities.keys()))

# 데이터 조회 버튼
if st.button("미세먼지 농도 확인"):
    # API 요청
    api_key = 'YOUR_API_KEY'  # 여기에 실제 API 키를 입력하세요
    url = f"http://openAPI.seoul.go.kr:8088/{api_key}/json/RealtimeCityAir/1/1/{cities[city_selected]}"

    try:
        response = requests.get(url)
        data = response.json()

        # 미세먼지 농도 데이터 추출
        if 'RealtimeCityAir' in data:
            dust_level = data['RealtimeCityAir']['row'][0]['pm10']  # PM10 값을 가져옴
            st.write(f"{city_selected}의 미세먼지 농도(PM10): {dust_level} μg/m³")
        else:
            st.write("데이터를 가져오는 데 문제가 발생했습니다.")
    except Exception as e:
        st.write("오류 발생:", e)

