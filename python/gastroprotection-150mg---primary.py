# S Jill Stocks, Evangelos Kontopantelis, Artur Akbarov, Sarah Rodgers, Anthony J Avery, Darren M Aschroft, 2023.

import sys, csv, re

codes = [{"code":"19272","system":"gprdproduct"},{"code":"21","system":"gprdproduct"},{"code":"26170","system":"gprdproduct"},{"code":"27288","system":"gprdproduct"},{"code":"30863","system":"gprdproduct"},{"code":"31533","system":"gprdproduct"},{"code":"34295","system":"gprdproduct"},{"code":"34403","system":"gprdproduct"},{"code":"34433","system":"gprdproduct"},{"code":"34480","system":"gprdproduct"},{"code":"34708","system":"gprdproduct"},{"code":"34886","system":"gprdproduct"},{"code":"43529","system":"gprdproduct"},{"code":"45214","system":"gprdproduct"},{"code":"45232","system":"gprdproduct"},{"code":"4885","system":"gprdproduct"},{"code":"53335","system":"gprdproduct"},{"code":"54784","system":"gprdproduct"},{"code":"58711","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('gastroprotection-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["gastroprotection-150mg---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["gastroprotection-150mg---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["gastroprotection-150mg---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
