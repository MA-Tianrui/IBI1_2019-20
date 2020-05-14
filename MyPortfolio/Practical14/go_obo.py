import xml.dom.minidom
import re
import pandas as pd

# extract root-obo and element-term from xml
GOTree = xml.dom.minidom.parse('go_obo.xml')
obo = GOTree.documentElement
terms = obo.getElementsByTagName("term")

# initial setting
GOid = []
GOname = []
GOdef = []



# search all terms
for term in terms:
    define = term.getElementsByTagName('def')[0]
    defstr = define.getElementsByTagName('defstr')[0]
    if re.search(r'[Aa]utophagosome', defstr.childNodes[0].data):  # find definition including autophagosome
        GOdef.append(defstr.childNodes[0].data)  # extract definition
        GOid.append(term.getElementsByTagName('id')[0].childNodes[0].data)  # extract id
        GOname.append(term.getElementsByTagName('name')[0].childNodes[0].data)  # extract name



# find the number of childnodes
# initial setting of number of childnodes
GOcn = [0]*len(GOid)

def Find_is_a(anid, fidList, aGOid):
    """
    input: a GO id (a string), a empty list to store sub-GO id and a parent GO id whose sub-GO is needed to calculate
    return: none
    put all sub-GO id of the given GO into the fidList
    """
    for term in terms:
        is_as = term.getElementsByTagName('is_a')
        for is_a in is_as:
            if is_a.childNodes[0].data == anid:  # find the sub-GO
                GOcn[GOid.index(aGOid)] += 1  # when find a sub-GO of the GO, add 1 to the corresponding position in the GOcn list
                fidList.append(term.getElementsByTagName('id')[0].childNodes[0].data)
    if len(fidList) > 0:
        Find_is_a_list(fidList, aGOid)

def Find_is_a_list(idList, aGOid):
    """
    input: a list containing GO id and a parent GO id whose sub-GO is needed to calculate
    return: none
    """
    for anid in idList:
        Find_is_a(anid, [], aGOid)
    
# find all the sub_GO of each GO in previous list
for anid in GOid:
    Find_is_a(anid, [], anid)



# found a dataframe from dict
GO_information = pd.DataFrame({
        'id':GOid, 
        'name':GOname, 
        'definition':GOdef, 
        'childnodes':GOcn})

# put the dataframe into a new excel file
GO_information.to_excel('GO_information.xlsx', sheet_name='GO information', index=False)