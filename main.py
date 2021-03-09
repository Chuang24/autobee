import os
import sys
from collections import OrderedDict



name='chris'
phone='6138909242'
email='hzh94kobe24@hotmail.com'
serialN='4115456457887'
TicketId='177456'



def createBrowserScript(fl, fl_ext, items, pdf_file_name):
    if pdf_file_name and len(fl) > 0:
        of = os.path.splitext(pdf_file_name)[0] + '.txt'
        all_lines = []
        for k, v in items.items():
            print(k + ' -> ' + v)
            if (v in ['/Yes', '/On']):
                all_lines.append("document.getElementById('" + k + "').checked = true;\n");
            elif (v in ['/0'] and k in fl_ext):
                all_lines.append("document.getElementById('" + k + "').checked = true;\n");
            elif (v in ['/No', '/Off', '']):
                all_lines.append("document.getElementById('" + k + "').checked = false;\n");
            elif (v in [''] and k in fl_ext):
                all_lines.append("document.getElementById('" + k + "').checked = false;\n");
            elif (k in fl):
                selectListOption(all_lines, k, v)
            else:
                all_lines.append("document.getElementById('" + k + "').value = '" + v + "';\n");
        outF = open(of, 'w')
        outF.writelines(all_lines)
        outF.close()


def creatScript(name,phone,email):
    all_lines=[]
    all_lines.append("document.getElementById(ContactName).value='"+ name +"';\n")
    all_lines.append("document.getElementById(ContactPhoneNumber).value='"+ phone +"';\n")
    all_lines.append("document.getElementById(EmailAddress).value='"+ email +"';\n")
    print(all_lines)

creatScript(name,phone,email)
