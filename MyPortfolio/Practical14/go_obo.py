import xml.dom.minidom
import re
import pandas as pd

GOTree = xml.dom.minidom.parse('go_obo.xml')
obo = GOTree.documentElement
terms = obo.getElementsByTagName("term")

GOid = []
GOname = []
GOdef = []


for term in terms:
    define = term.getElementsByTagName('def')[0]
    defstr = define.getElementsByTagName('defstr')[0]
    if re.search(r'[Aa]utophagosome', defstr.childNodes[0].data):
        GOdef.append(defstr.childNodes[0].data)
        GOid.append(term.getElementsByTagName('id')[0].childNodes[0].data)
        GOname.append(term.getElementsByTagName('name')[0].childNodes[0].data)
        

GOcn = [0]*len(GOid)

            
def Find_is_a(anid, fidList, aGOid):
        for term in terms:
            is_as = term.getElementsByTagName('is_a')
            for is_a in is_as:
                if is_a.childNodes[0].data == anid:
                    GOcn[GOid.index(aGOid)] += 1
                    fidList.append(term.getElementsByTagName('id')[0].childNodes[0].data)
        if len(fidList) > 0:
            Find_is_a_list(fidList, aGOid)
                    
def Find_is_a_list(idList, aGOid):
    for anid in idList:
        Find_is_a(anid, [], aGOid)
    
    

for anid in GOid:
    Find_is_a(anid, [], anid)


#print(GOid)
#print(GOcn)
#print(GOdef)
#print(GOname)

GO_information = pd.DataFrame({
        'id':GOid, 
        'name':GOname, 
        'definition':GOdef, 
        'childnodes':GOcn})

GO_information.to_excel('GO_information.xlsx', sheet_name='GO information', index=False)