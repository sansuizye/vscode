import easygui as e
import sys
while 1:
    msg = "你是男的女的"
    xingbie = ["男","女"]
    
    title = "调查"
               
    choice = e.choicebox(msg,title,xingbie)
    if choice=="男":
        m = ""
        oc = ["是","不是"]
        p = e.choicebox(msg = "你是男大学生吗",choices = oc)
        sys.exit(0)
    else:
        e.msgbox("牛逼")
        sys.exit(0)

    
   

