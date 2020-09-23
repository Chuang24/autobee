import os
import sys


def generate(name,number,email,ID,serialN):
    print(name + number)

def convertoStr(input_seq,seperator):
    final_str = seperator.join(input_seq)
    return final_str

def createScriptCisco(name,number,email,ID,serialN):
    
    all_lines=[]
    all_lines.append("document.getElementById('ContactId').value='"+ ID +"';\n")
    all_lines.append("document.getElementById('ContactName').value='"+ name +"';\n")
    all_lines.append("document.getElementById('ContactPhoneNumber').value='"+ number +"';\n")
    all_lines.append("document.getElementById('EmailAddress').value='"+ email +"';\n")
    all_lines.append("document.getElementById('SerialNumber').value='"+ serialN +"';\n")
    return (convertoStr(all_lines,""))

def createScriptZendesk(id,name,number,email,serialN):   
    of=os.path.splitext('Zendesk')[0]+'.txt'
    all_lines=[]
    id=int(id)
    id13=str(id+13)
    id1=str(id+1)
    id2=str(id+2)
    id=str(id)
    all_lines.append("document.getElementById('" + id13  + "val-field_1.3.4--input').value='"+ name +"';\n")
    all_lines.append("document.getElementById('" + id + "val-field_1.3.4--input').value='"+ number +"';\n")
    all_lines.append("document.getElementById('" + id1  + "val-field_1.3.4--input').value='"+ email +"';\n")
    all_lines.append("document.getElementById('" + id2  + "val-field_1.3.4--input').value='"+ serialN +"';\n")
    # all_lines.append("document.getElementById(1790val-field_1.3.4--input).value='"+ name +"';\n")
    # all_lines.append("document.getElementById(1777val-field_1.3.4--input).value='"+ number +"';\n")
    # all_lines.append("document.getElementById(1778val-field_1.3.4--input).value='"+ email +"';\n")
    # all_lines.append("document.getElementById(1779val-field_1.3.4--input).value='"+ serialN +"';\n")
    return (convertoStr(all_lines,""))
    # outF=open(of,'w')
    # outF.writelines(all_lines)
    # outF.close()

    # print(all_lines)
print(createScriptZendesk(100,'chris','6138909242','1@gmail.com','1111'))
#createScriptCisco('chris','612321123','hzh94kobe24@hotmail.com','1764067','4118882929')
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