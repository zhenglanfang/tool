import json
import xlwt

def readExcel():
    with open('Specialist for Flight Tickets.json','r') as ajh:
        jsonfile=json.loads(ajh.read())
    jsonfile.get('utterances')
    return jsonfile

def writeM():
    jsonfile=readExcel()
    jsonfile = jsonfile.get('utterances')
    book = xlwt.Workbook()
    sheet = book.add_sheet('london',cell_overwrite_ok=True)
    title=[ "text","intent","entities","entity","startPos","endPos"]
    for i in range(len(title)):
        sheet.write(0,i,title[i])
    for index, item in enumerate(jsonfile):
        for i in range(len(title)):
            if title[i] == "entities":
                sheet.write(index+1,i,'')
            elif i > title.index('entities'):
                entities = item['entities']
                if entities:
                    entities = entities[0]
                    sheet.write(index+1,i,entities[title[i]])
                else:
                    sheet.write(index+1,i,'')
            else:
                sheet.write(index+1,i,item[title[i]])

    # for i in range(len(title)):
    #     sheet.write(0,i,title[i])
    # for j in range(len(jsonfile)):
    #     for line in jsonfile[j]:
    #         for i in range(len(title)):
    #             if line==title[i]:
    #                 sheet.write(j+1,i,jsonfile[j][line])
                    
    book.save('london_chris.xls')
                
if __name__ == '__main__':
    writeM()
            
