import pandas as pd

data = [
    164, 292, 102, 153, 139, 18, 92, 236, 241, 202, 31, 24, 145, 188, 293, 204,
    32, 220, 154, 131, 45, 214, 62, 188, 129, 171, 161, 151, 142, 118, 171, 190,
    129, 115, 168, 94, 230, 139, 100, 99, 99, 72, 103, 109, 176, 111, 59, 44,
    140, 135
]

bins_name = ["0 ~ 50", "50 ~ 100", "100 ~ 150",
             "150 ~ 200", "200 ~ 250", "250 ~ 300", "Total"]

# Pandas Series로 변환
data_series = pd.Series(data)

# 구간 정의
bins = [0, 50, 100, 150, 200, 250, 300]

# 데이터를 구간으로 분할
data_bins = pd.cut(data_series, bins)

# 도수분포표 생성
frequency_table = pd.crosstab(index=data_bins, colnames=["Data"],
                              columns="Frequency", margins=True)
frequency_table.index = bins_name

# 결과 출력
print(frequency_table)
