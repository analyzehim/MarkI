day_file = "day.txt" #param 0
week_file = "week.txt" #param 1
backlog_file = "backlog.txt" #param 2

def parse_file(filename):
    mas=[]
    f = open(filename,"r")
    for line in f:
        if line[-1]!='\n':
            line+='\n'
        mas.append(line)
    f.close()
    return mas
    
def write_file(filename, mas):
    f = open(filename, "w")
    for line in mas:
        f.write(line)
    f.close()
    return 0

def make_output(mas):
    output=""
    for i in range(len(mas)):
        output+=str(i)+': '+str(mas[i])
    return output

class Diary:
    def return_list(self, flag):
        return make_output(self.matr[int(flag)])

        
    def update_files(self):
        write_file(day_file, self.matr[0])
        write_file(week_file, self.matr[1])
        write_file(backlog_file, self.matr[2])
    
        
    def change_flag(self, id, flag_old, flag_new):
        self.matr[flag_new].append(self.matr[flag_old].pop(id))
        self.update_files()
        return 0
        
    def add_line(self, line, flag):
        self.matr[int(flag)].append(line)
        return 0
    
    def __str__(self):
        output=''
        output+='0______ DAY:\n' + self.return_list(0) + '\n'
        output+='1______ WEEK:\n'+ self.return_list(1) + '\n'
        output+='2______ BACKLOG:\n'+ self.return_list(2)
        return output
    
    def __init__(self):
        self.matr=[[],[],[]]

        self.matr[0] = parse_file(day_file)
        self.matr[1] = parse_file(week_file)
        self.matr[2] = parse_file(backlog_file)
        
d = Diary()
d.update_files()
print d
#d.change_flag(0,2,1)
#print d



