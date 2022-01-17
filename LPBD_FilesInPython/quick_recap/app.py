# file_read = open("data.txt", "r")   #file name, mode and here r is for read only mode
# file_content = file_read.read()
# file_read.close()

# print(file_content)

# file_write = open("data.txt", "w")  #file name, mode and here w is for write mode
# file_write.write(file_content + "\n" + "new content")
# file_write.close()


# people_file = open("../people.txt")
# people_content = [line.strip() for line in people_file.readlines()]
# people_file.close()

# print(type(people_content))
# print(people_content)

# Quiz system - practice for files open/read/write/close
# correct_answers = 0

# quiz_q_files = open("questions.txt", "r")
# quiz_contents = [q.strip() for q in quiz_q_files.readlines()] 

# quiz_q_files.close()
# print(quiz_contents)

# for question in quiz_contents:
#     q, a = question.split("=")
#     user_answer = input(f"What is the answer for {q}: ")
#     if user_answer == a:
#         correct_answers +=1 

# quiz_result = f"your final score is {correct_answers}/{len(quiz_contents)}"
# print(quiz_result)

import csv

fund_data_list = []

with open('COWZ-holdings.csv', 'r') as fund_holdings:
    fund_data_reader = list(csv.reader(fund_holdings))

    def holdings_csv_parser(document):
        loc_ignored_lines = 0
        loc_info_lines = 0
        info_lines_list = []
        header_fullfilled = False
        
        for line in document:
            if len(line) == 0:
                loc_ignored_lines += 1
            
            elif len(line) == 1:
                info_lines_list.append(line)
                loc_info_lines += 1
            
            elif len(line) == 3 and header_fullfilled:
                fund_data_list.append({
                    "Data Type": "Data",
                    "Fund Name": line[0],
                    "Fund Ticker": line[1],
                    "Fund Weight": line[2]
                })
            
            elif len(line) == 3 and header_fullfilled == False:
                fund_data_list.append({
                    "Data Type": "header",
                    "Fund Name H": line[0],
                    "Fund Ticker H": line[1],
                    "Fund Weight H": line[2]
                })
                header_fullfilled = True
        
        fund_data_list.append({
                    "Data Type": "info",
                    "Fund Info": info_lines_list
                })
        print(loc_ignored_lines)
        print(loc_info_lines)
        return fund_data_list

cowz_sheet = holdings_csv_parser(fund_data_reader)
print(cowz_sheet)