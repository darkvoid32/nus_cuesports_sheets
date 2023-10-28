# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID and range of a master tracking spreadsheet.
SPREADSHEET_ID_MASTER = '1Wvk4UGKgiT_UACsgzUSepydVA7GgO5FbqtsL9p3qM-4'
SPREADSHEET_ID_FORM = '1eEHQB_kuZ0mFfq97kQkPhCSWpli723Szp7TrJWBP3xU'

# MASTER Sheet Constants
MASTER_SHEET_NAME = 'Sem 1'
MASTER_DATA_START = '19'
MASTER_DATE_START = 5

MASTER_ID_NAME = 'A'
MASTER_ID_YEAR = 'B'
MASTER_ID_DISP = 'C'
MASTER_ID_TELE = 'D'

MASTER_ID_NAME_LIST = 0
MASTER_ID_YEAR_LIST = 1
MASTER_ID_DISP_LIST = 2
MASTER_ID_TELE_LIST = 3

# [[Date]]
MASTER_DATE_RANGE = MASTER_SHEET_NAME + '!F2:AF2'
# [[Full Name, Telegram Display name, Telegram Handle]]
MASTER_NAME_RANGE = MASTER_SHEET_NAME + '!A' + MASTER_DATA_START + ':' + MASTER_ID_TELE

# FORM Sheet Constants
FORM_SHEET_NAME = 'Week 11'
FORM_START = '2'

FORM_NAME = 'B'
FORM_DATE = 'E'

FORM_NAME_ID = 0
FORM_YEAR_ID = 1
FORM_TELE_ID = 2
FORM_DATE_ID = 3

FORM_DATA_RANGE = FORM_SHEET_NAME + '!' + FORM_NAME + FORM_START + ':' + FORM_DATE

# ATTENDANCE Sheet Constants
ATTENDANCE_SHEET_NAME = 'Nov 23'
# [[Date]]
ATTENDANCE_SHEET_DATE_RANGE = ATTENDANCE_SHEET_NAME + '!F8:K8'
# [[Full Name, Telegram Handle]]
ATTENDANCE_SHEET_NAME_RANGE = ATTENDANCE_SHEET_NAME + '!B10:E124'

ATTENDANCE_NAME_ID = 0
ATTENDANCE_TELE_ID = 1
ATTENDANCE_ROLE_ID = 2
ATTENDANCE_YEAR_ID = 3

ATTENDANCE_DATA_START = 9

ATTENDANCE_MEMBER_ROLE = 'Member'

# MISC Constants
MON = 'Monday'
WED = 'Wednesday'
BOTH = 'Both Days'

COMING = 'COMING'
PAID = 'PAID'
FREE = 'FREE'
DISCOUNT = 'DISCOUNT'
CASH = 'CASH'

TELE_MON = 'Tele_Mon.txt'
TELE_WED = 'Tele_Wed.txt'

TOKEN = 'token.json'
CREDENTIALS = 'credentials.json'