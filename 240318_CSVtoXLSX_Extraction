import os
import pandas as pd
import glob

# 输入フォルダのパス
input_folder = '----'

# 出力フォルダのパス
output_folder = '----'

csv_files = [file for file in os.listdir(input_folder) if file.endswith('.CSV') or file.endswith('.csv')]

if not csv_files:
    print("No file found.")

# 抽出したい列を指定
# ここは2列目＝１（列数は0から）
selected_column_position = 1

for csv_file in csv_files:
    file_path = os.path.join(input_folder, csv_file)

    # header=抽出したい行目
    # ここは2行目 → header=1（行数は0から）
    df = pd.read_csv(file_path, header=1, encoding='utf-8')
   
    # 抽出したいデータを指定
    # ここは5より小さい値を抽出 → selected_column_position] < 5
    selected_rows_whole_df = df[df.iloc[:, selected_column_position] < 5]
    
    file_name = os.path.splitext(csv_file)[0]
    output_file_path_rows = os.path.join(output_folder, f"{file_name}_modified.csv")
    selected_rows_whole_df.to_csv(output_file_path_rows, index=False, encoding='utf-8')
    
    print(f"File Saved: {output_file_path_rows}")

for csv_file in glob.glob(os.path.join(output_folder, '*.csv')):
    xlsx_file = csv_file.replace('.csv', '.xlsx')
    df = pd.read_csv(csv_file)
    df.to_excel(xlsx_file, index=False)

    print(f"File Saved: {xlsx_file}")
