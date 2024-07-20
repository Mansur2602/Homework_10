import requests

url = 'https://pogoda.mail.ru/prognoz/astana/24hours/'
response = requests.get(url)


data = response.text
start_tag = '<span class="p-forecast__temperature-value">'
end_tag = '</span>'
start_index = data.find(start_tag)
    
start_index != -1
start_index += len(start_tag)
end_index = data.find(end_tag, start_index)
        
end_index != -1
temperature_data = data[start_index:end_index]
temperature = temperature_data.split()[0]
print(f'Текущая температура в Астане: {temperature}')
        








