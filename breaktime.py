import time
total_breaks = 3
break_count = 0

print("This program started on "+time.ctime())
while (break_count < total_breaks):
    import webbrowser
    time.sleep(2)
    webbrowser.open("http://patrick-essa.squarespace.com")
    break_count = break_count + 1
print("This program ended on "+time.ctime())
 



