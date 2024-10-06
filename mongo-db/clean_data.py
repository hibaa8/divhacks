import json
import re

with open('data.jsonl', 'r') as file_stream, open('cleaned_data.jsonl', 'w') as write_stream:
    for line in file_stream:
        try:
            item = json.loads(line)

            item['fabric'] = item.pop('product_details')

            if 'price' in item and isinstance(item['price'], str):
                cleaned_price = re.findall(r'\d+', item['price'])
                if cleaned_price:
                    item['price'] = str(int(''.join(cleaned_price)))

            if 'description' in item and item['description'].startswith('Description'):
                item['description'] = item['description'].replace('Description ', '', 1)

            if 'type' in item and isinstance(item['type'], str):
                item['type'] = item['type'].lower()
                if item['type'] == 'underwear':
                    item['type'] = 'other'

            write_stream.write(json.dumps(item) + '\n')

        except json.JSONDecodeError as error:
            print(f'Error processing line: {error}')

print('Data cleaning complete.')
