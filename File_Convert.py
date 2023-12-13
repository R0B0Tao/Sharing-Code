import codecs
import csv
import os
import pandas as pd

def convert_dat_to_csv(dat_file, csv_file):
    with codecs.open(dat_file, 'r', encoding='utf-16') as datfile, open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
      
        dat_reader = csv.reader(datfile, delimiter='\t')

        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(dat_reader)

# 入力フォルダのパス
input_folder = '-----'

# 出力フォルダのパス
output_folder = '-----'

dat_files = [file for file in os.listdir(input_folder) if file.endswith('.dat')]

if not dat_files:
    print("No dat file find.")
else:
    for dat_file in dat_files:
        dat_path = os.path.join(input_folder, dat_file)
        csv_path = os.path.join(output_folder, f"{os.path.splitext(dat_file)[0]}.csv")
        convert_dat_to_csv(dat_path, csv_path)
        
print(f"File has been converted to CSV.")

csv_files = [file for file in os.listdir(output_folder) if file.endswith('.csv')]

selected_columns_df = pd.DataFrame()

# 抽出したい列を指定
# ここは2列目＝１（列数は0から）
selected_columns_positions = [1] 

for csv_file in csv_files:
    file_path = os.path.join(output_folder, csv_file)
    # headerをNoneに指定（カラム名がない）
    df = pd.read_csv(file_path, header=None, encoding='utf-8') 
    
    selected_data = df.iloc[:, selected_columns_positions]
    
    selected_columns_df = pd.concat([selected_columns_df, selected_data], axis=1)

combined_csv_path = os.path.join(output_folder, 'New_Sum_Selected.csv')
selected_columns_df.to_csv(combined_csv_path, index=False, encoding='utf-8')

print(f"File Saved: {combined_csv_path}")