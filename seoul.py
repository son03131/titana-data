# Crawl 상세페이지 데이터 (리팩토링 버전)

def parse_company_detail(detail_soup):
    result = {
        "자본금": "",
        "매출액": "",
        "대표자": "",
        "설립일": ""
    }
    
    # 상세정보 테이블 선택
    table = detail_soup.select_one("div.company-infomation-row.basic-infomation > div > table > tbody")
    if not table:
        return result
    
    rows = table.find_all("tr")
    
    for row in rows:
        columns = row.find_all("td")
        if len(columns) < 2:
            continue
        # 각 row의 label, value 추출
        label_1 = columns[0].get_text(strip=True)
        value_1 = columns[1].get_text(strip=True)
        if label_1 in result:
            result[label_1] = value_1
        
        # 일부 row는 td가 4개일 수 있음
        if len(columns) >= 4:
            label_2 = columns[2].get_text(strip=True)
            value_2 = columns[3].get_text(strip=True)
            if label_2 in result:
                result[label_2] = value_2

    return result
