from diary_proto import Diary
d = Diary()
d.add_line('Hello\n', 0)
d.update_files()
print d.return_list(0)
