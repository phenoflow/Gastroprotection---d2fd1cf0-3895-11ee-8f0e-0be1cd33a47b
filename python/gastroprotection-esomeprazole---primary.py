# S Jill Stocks, Evangelos Kontopantelis, Artur Akbarov, Sarah Rodgers, Anthony J Avery, Darren M Aschroft, 2023.

import sys, csv, re

codes = [{"code":"13282","system":"gprdproduct"},{"code":"1451","system":"gprdproduct"},{"code":"18","system":"gprdproduct"},{"code":"29457","system":"gprdproduct"},{"code":"29468","system":"gprdproduct"},{"code":"32919","system":"gprdproduct"},{"code":"32924","system":"gprdproduct"},{"code":"33565","system":"gprdproduct"},{"code":"34302","system":"gprdproduct"},{"code":"34411","system":"gprdproduct"},{"code":"34577","system":"gprdproduct"},{"code":"34791","system":"gprdproduct"},{"code":"34812","system":"gprdproduct"},{"code":"34841","system":"gprdproduct"},{"code":"34843","system":"gprdproduct"},{"code":"34967","system":"gprdproduct"},{"code":"35257","system":"gprdproduct"},{"code":"35383","system":"gprdproduct"},{"code":"36046","system":"gprdproduct"},{"code":"42091","system":"gprdproduct"},{"code":"42533","system":"gprdproduct"},{"code":"42736","system":"gprdproduct"},{"code":"42900","system":"gprdproduct"},{"code":"43948","system":"gprdproduct"},{"code":"43957","system":"gprdproduct"},{"code":"43995","system":"gprdproduct"},{"code":"44252","system":"gprdproduct"},{"code":"45173","system":"gprdproduct"},{"code":"47511","system":"gprdproduct"},{"code":"49163","system":"gprdproduct"},{"code":"49433","system":"gprdproduct"},{"code":"49584","system":"gprdproduct"},{"code":"50365","system":"gprdproduct"},{"code":"50372","system":"gprdproduct"},{"code":"51260","system":"gprdproduct"},{"code":"51357","system":"gprdproduct"},{"code":"5178","system":"gprdproduct"},{"code":"52379","system":"gprdproduct"},{"code":"52866","system":"gprdproduct"},{"code":"53518","system":"gprdproduct"},{"code":"53843","system":"gprdproduct"},{"code":"55468","system":"gprdproduct"},{"code":"55700","system":"gprdproduct"},{"code":"55744","system":"gprdproduct"},{"code":"5604","system":"gprdproduct"},{"code":"56235","system":"gprdproduct"},{"code":"56432","system":"gprdproduct"},{"code":"56433","system":"gprdproduct"},{"code":"57177","system":"gprdproduct"},{"code":"57311","system":"gprdproduct"},{"code":"57738","system":"gprdproduct"},{"code":"58066","system":"gprdproduct"},{"code":"58216","system":"gprdproduct"},{"code":"58332","system":"gprdproduct"},{"code":"59135","system":"gprdproduct"},{"code":"59547","system":"gprdproduct"},{"code":"59725","system":"gprdproduct"},{"code":"60403","system":"gprdproduct"},{"code":"6114","system":"gprdproduct"},{"code":"7255","system":"gprdproduct"},{"code":"9989","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('gastroprotection-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["gastroprotection-esomeprazole---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["gastroprotection-esomeprazole---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["gastroprotection-esomeprazole---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
