import utils.ReadExcel
import requests
import json
datas = utils.ReadExcel.Read_Excel.read_excel('test')
for i in range(0,len(datas)):
    str = json.loads(datas[i].get(4))
    print(str)
    request = requests.get(datas[i].get(3),datas[i].get(4))
    print(request.url)
