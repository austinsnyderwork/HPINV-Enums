
from enum import Enum


class TypeId(Enum):
    PHY = 'PHY'
    PA = 'PA'
    APN = 'APN'
    DDS = 'DDS'
    PHA = 'PHA'


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


class ActiveStatusValue(Enum):
    ACTIVE = 'ACT'
    INACTIVE = 'I'


class WorksiteColumn(Enum):
    WORKSITE_ID = 'worksiteid'
    WORKSITE_NAME = 'worksitename'
    PARENT_WORKSITE_ID = 'parentworksiteid'
    PARENT_WORKSITE_NAME = 'parentworksitename'
    ACTIVE_STATUS = 'detailactive'
    PHONE = 'phone'
    CITY = 'city'
    ADDRESS_1 = 'address1'
    ADDRESS_2 = 'address2'
    STATE = 'state'
    ZIP = 'zip'
    CALL_DATE = 'calldate'
    MEMO = 'memo'


class HcpColumn(Enum):
    HCP_ID = 'hcpid'
    TYPE_ID = 'typeid'
    FIRST_NAME = 'firstname'
    LAST_NAME = 'lastname'


class AuxiliaryColumn(Enum):
    HOURS = 'workhrsweek'
    ASSISTANTS = 'rdas'
    HYGIENISTS = 'rdhs'
    TRAINING_ASSISTANTS = 'dats'


class HcpPositionColumn(Enum):
    WORKSITE_HISTORY_ID = 'worksitehistoryid'
    EFFECT_DATE = 'effectdate'
    SPECIALTY_NAME = 'specialtyname'
    FTE = 'fte'
    WORKSITE_TYPE = 'worksitetype'
    WORK_HOURS = 'wkhours'
    WORK_WEEKS = 'wkweeks'
    FACE_TIME = 'facetime'
    PERCENT_MEDICAID = 'pctmedicaid'
    PERCENT_SLIDING_FEE = 'pctslidingfee'
    TRANSACTION_ID = 'transactionid'
