# S Jill Stocks, Evangelos Kontopantelis, Artur Akbarov, Sarah Rodgers, Anthony J Avery, Darren M Aschroft, 2023.

import sys, csv, re

codes = [{"code":"13015","system":"gprdproduct"},{"code":"15275","system":"gprdproduct"},{"code":"1977","system":"gprdproduct"},{"code":"24301","system":"gprdproduct"},{"code":"26699","system":"gprdproduct"},{"code":"276","system":"gprdproduct"},{"code":"30926","system":"gprdproduct"},{"code":"32914","system":"gprdproduct"},{"code":"33022","system":"gprdproduct"},{"code":"33326","system":"gprdproduct"},{"code":"34332","system":"gprdproduct"},{"code":"34568","system":"gprdproduct"},{"code":"34571","system":"gprdproduct"},{"code":"34792","system":"gprdproduct"},{"code":"35101","system":"gprdproduct"},{"code":"36892","system":"gprdproduct"},{"code":"41992","system":"gprdproduct"},{"code":"42898","system":"gprdproduct"},{"code":"52971","system":"gprdproduct"},{"code":"53337","system":"gprdproduct"},{"code":"54539","system":"gprdproduct"},{"code":"54746","system":"gprdproduct"},{"code":"55745","system":"gprdproduct"},{"code":"57541","system":"gprdproduct"},{"code":"57648","system":"gprdproduct"},{"code":"58030","system":"gprdproduct"},{"code":"58946","system":"gprdproduct"},{"code":"59296","system":"gprdproduct"},{"code":"60230","system":"gprdproduct"},{"code":"89","system":"gprdproduct"},{"code":"9851","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('gastroprotection-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["gastroprotection-100mg---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["gastroprotection-100mg---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["gastroprotection-100mg---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
