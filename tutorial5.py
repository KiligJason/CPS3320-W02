#Tutorial 5
#Ziyiyang Wang 1098529
#Zhaoze Wang 1098471

import re


str1 = "abb29ABCLK%lCnrDBCabbbb"
# match = re.search(r'abbbb',str1)
match = re.search('ab{4}',str1) # return when match followed by 4 repeat b
                # 'ab*?',     # a followed by zero or more b
                # 'ab+?',     # a followed by one or more b
                # 'ab??',     # a followed by zero or one b
print (match.group())

match2 = re.search("[A-Z][a-z]",str1) # one upper case letter followed by lower case letters
print (match2.group())