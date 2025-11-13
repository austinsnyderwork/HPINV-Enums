from enum import Enum


class HpinvTable(Enum):
    WORKSITE = 'Worksite'
    WORKSITE_DETAIL = 'WorksiteDetail'
    HCP = 'Hcp'
    WORKSITE_HISTORY = 'WorksiteHistory'
    EDUCATION = 'Education'
    SCHOOL = 'School'
    TRAINING = 'Training'


class TypeId(Enum):
    PHY = 'PHY'
    PA = 'PA'
    APN = 'APN'
    DDS = 'DDS'
    PHA = 'PHA'
    OTH = 'OTH'
    PCO = 'PCO'
    IDK_WHAT_THIS_IS = 'RS'


class TransactionId(Enum):
    ADD = 'ADD'
    TRF = 'TRF'
    CHG = 'CHG'
    DEL = 'DEL'
    CHG_ADD = 'CHG_ADD'
    CHG_DEL = 'CHG_DEL'


class Activity(Enum):
    ACTIVE = 'ACT'
    INACTIVE = 'I'


class WorksiteType(Enum):
    PRIMARY = 'P'
    SECONDARY = 'S'


class ActiveStatus(Enum):
    ACTIVE = 'ACT'
    INACTIVE = 'I'


class WorksiteColumn(Enum):
    WORKSITE_ID = 'worksiteid'
    WORKSITE_NAME = 'worksitename'
    PARENT_WORKSITE_ID = 'parentworksite'
    PARENT_WORKSITE_NAME = 'parentworksitename'
    ACTIVE_STATUS = 'transactionid'
    PHONE = 'phone'
    CITY = 'city'
    ADDRESS_1 = 'address1'
    ADDRESS_2 = 'address2'
    STATE = 'state'
    ZIP = 'zip'
    COUNTY_ID = 'countyid'
    LATITUDE = 'latitude'
    LONGITUDE = 'longitude'


class WorksiteDetailColumn(Enum):
    WORKSITE_ID = 'worksiteid'
    TYPE_ID = 'typeid'
    CALL_DATE = 'calldate'
    ACTIVE_STATUS = 'transactionid'
    MEMO = 'memo'


class HcpColumn(Enum):
    HCP_ID = 'hcpid'
    TYPE_ID = 'typeid'
    FIRST_NAME = 'firstname'
    LAST_NAME = 'lastname'
    GENDER = 'gender'
    TITLE = 'title'
    BIRTH_DATE = 'birthdate'
    BIRTH_STATE = 'birthstate'
    LICENSE_NUMBER = 'licensenumber'
    NPI_NUMBER = 'npinumber'


class EducationColumn(Enum):
    SCHOOL_ID = 'schoolid'
    TYPE_ID = 'typeid'
    SCHOOL_STATE = 'state'
    DEGREE_ID = 'degreeid'
    GRAD_YEAR = 'gradyear'
    TERMINAL_DEGREE = 'terminaldegflag'


class SchoolColumn(Enum):
    TYPE_ID = 'typeid'
    SCHOOL_ID = 'schoolid'
    SCHOOL_STATE = 'state'


class TrainingColumn(Enum):
    TRAINING_SITE_ID = 'trainingsiteid'
    SPECIALTY_ID = 'specialtyid'
    TRAINING_TYPE_ID = 'trainingtypeid'
    GRAD_YEAR = 'gradyear'


class AuxiliaryColumn(Enum):
    HOURS = 'workhrsweek'
    ASSISTANTS = 'rdas'
    HYGIENISTS = 'rdhs'
    TRAINING_ASSISTANTS = 'dats'


class HcpPositionColumn(Enum):
    HCP_ID = 'hcpid'
    WORKSITE_ID = 'worksiteid'
    WORKSITE_HISTORY_ID = 'worksitehistoryid'
    EFFECT_DATE = 'effectdate'
    ADMIN_DATE = 'admindate'
    SPECIALTY_NAME = 'specialtyname'
    FTE = 'fte'
    WORKSITE_TYPE = 'worksitetype'
    WORK_HOURS = 'wkhours'
    WORK_WEEKS = 'wkweeks'
    FACE_TIME = 'facetime'
    PERCENT_MEDICAID = 'pctmedicaid'
    PERCENT_SLIDING_FEE = 'pctslidingfee'
    TRANSACTION_ID = 'transactionid'
    SPECIALTY_ID = 'specialtyid'
