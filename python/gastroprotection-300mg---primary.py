# S Jill Stocks, Evangelos Kontopantelis, Artur Akbarov, Sarah Rodgers, Anthony J Avery, Darren M Aschroft, 2023.

import sys, csv, re

codes = [{"code":"1556","system":"gprdproduct"},{"code":"19249","system":"gprdproduct"},{"code":"19277","system":"gprdproduct"},{"code":"34531","system":"gprdproduct"},{"code":"37815","system":"gprdproduct"},{"code":"39","system":"gprdproduct"},{"code":"40152","system":"gprdproduct"},{"code":"40896","system":"gprdproduct"},{"code":"41536","system":"gprdproduct"},{"code":"42382","system":"gprdproduct"},{"code":"42532","system":"gprdproduct"},{"code":"42730","system":"gprdproduct"},{"code":"43057","system":"gprdproduct"},{"code":"44753","system":"gprdproduct"},{"code":"45322","system":"gprdproduct"},{"code":"4742","system":"gprdproduct"},{"code":"47909","system":"gprdproduct"},{"code":"48063","system":"gprdproduct"},{"code":"50492","system":"gprdproduct"},{"code":"51801","system":"gprdproduct"},{"code":"53871","system":"gprdproduct"},{"code":"54188","system":"gprdproduct"},{"code":"57158","system":"gprdproduct"},{"code":"59106","system":"gprdproduct"},{"code":"59404","system":"gprdproduct"},{"code":"59586","system":"gprdproduct"},{"code":"60537","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('gastroprotection-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["gastroprotection-300mg---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["gastroprotection-300mg---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["gastroprotection-300mg---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
