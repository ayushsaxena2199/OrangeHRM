import xlrd

path = r"D:\POM Frameworks\Orange HRM\data\login_details.xlsx"

login_workbook = xlrd.open_workbook(path)
login_worksheet = login_workbook.sheet_by_name('login')
login_rows = login_worksheet.get_rows()
login_header = next(login_rows)


def login_details():
    login_dict = {}
    for i in login_rows:
        login_dict[i[0].value] = (i[1].value, i[2].value)
    return login_dict


#########################################################################################
# logout locator

logout_workbook = xlrd.open_workbook(path)
logout_worksheet = logout_workbook.sheet_by_name('logout')
logout_rows = logout_worksheet.get_rows()
logout_header = next(logout_rows)


def logout_locators():
    logout_dict = {}
    for i in login_rows:
        logout_dict[i[0].value] = (i[1].value, i[2].value)
    return logout_dict


######################################################################################
# myinfo locator

info_workbook = xlrd.open_workbook(path)
info_worksheet = info_workbook.sheet_by_name('myinfo')
info_rows = info_worksheet.get_rows()
info_header = next(info_rows)


def info_locator():
    info_dict = {}
    for i in info_rows:
        info_dict[i[0].value] = (i[1].value, i[2].value)
    return info_dict

################################################################################################
# PIM


pim_workbook = xlrd.open_workbook(path)
pim_worksheet = pim_workbook.sheet_by_name('PIM')
pim_rows = pim_worksheet.get_rows()
pim_header = next(pim_rows)


def pim_locator():
    pim_dict = {}
    for i in pim_rows:
        pim_dict[i[0].value] = (i[1].value, i[2].value)
    return pim_dict

#####################################################################################

# recruitmentlocator


recruit_workbook = xlrd.open_workbook(path)
recruit_worksheet = recruit_workbook.sheet_by_name('recruitement')
recruit_rows = recruit_worksheet.get_rows()
recruit_header = next(recruit_rows)


def recruit_locator():
    recruit_dict = {}
    for i in recruit_rows:
        recruit_dict[i[0].value] = (i[1].value, i[2].value)
    return recruit_dict
