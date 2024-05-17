# Specify the detected encoding, e.g., 'ISO-8859-1'
detected_encoding = 'ISO-8859-1'

with open('Online_Retail.csv', 'r', encoding=detected_encoding) as source_file:
    with open('Online_Retail_utf8.csv', 'w', encoding='utf-8') as target_file:
        for line in source_file:
            target_file.write(line)
