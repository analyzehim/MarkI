day_file = "data/day.txt" #param 0
week_file = "data/week.txt" #param 1
backlog_file = "data/backlog.txt" #param 2

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
    
    def delete_id(self, type, id):
        try:
            self.matr[type].pop(id)
        except:
            print "Wrong ID: %s",id
        self.update_files()
        return 0

    def change_flag(self, id, flag_old, flag_new):
        self.matr[flag_new].append(self.matr[flag_old].pop(id))
        self.update_files()
        return 0
        
    def add_line(self, flag, line):
        self.matr[int(flag)].append(line)
        self.update_files()
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



