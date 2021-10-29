import re


# Read in the file and write into a new file
d = open('week_07/dracula.html', 'r')
i = open('week_07/izibicki.html', 'w')


# will print 'axample atring'

# Check the words and prepare replacing words
check_words = ('D&nbsp;R&nbsp;A&nbsp;C&nbsp;U&nbsp;L&nbsp;A', 'Dracula', 'DRACULA','Bram &nbsp; Stoker','Bram Stoker')
replace_words = ('<strong>I&nbsp;Z&nbsp;I&nbsp;B&nbsp;I&nbsp;C&nbsp;K&nbsp;I</strong>', '<strong>Izibicki</strong>', '<strong>IZIBICKI</strong>','Eddie &nbsp; Shi','Eddie Shi')


for line in d: #checking every line in the html
  
  for check_word, replace_word in zip(check_words,replace_words): #checking every string in the line and use zip() to aggregate the two word banks
      line = line.replace(check_word, replace_word) #replacing
  line = re.sub(r"\bCount\b", "Professor", line)
  line = re.sub(r"\bcount\b", "professor", line)
  line = re.sub(r"\bCOUNT\b", "PROFESSOR", line)

  i.write(line)





d.close()

i.close()