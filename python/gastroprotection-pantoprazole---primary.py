# S Jill Stocks, Evangelos Kontopantelis, Artur Akbarov, Sarah Rodgers, Anthony J Avery, Darren M Aschroft, 2023.

import sys, csv, re

codes = [{"code":"1986","system":"gprdproduct"},{"code":"49375","system":"gprdproduct"},{"code":"51804","system":"gprdproduct"},{"code":"5419","system":"gprdproduct"},{"code":"54693","system":"gprdproduct"},{"code":"59390","system":"gprdproduct"},{"code":"59711","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('gastroprotection-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["gastroprotection-pantoprazole---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["gastroprotection-pantoprazole---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["gastroprotection-pantoprazole---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
