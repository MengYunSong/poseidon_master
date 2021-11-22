# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Index, Integer, SmallInteger, String, text
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class AccountChangeNameLog(Base):
    __tablename__ = 'Account_ChangeNameLog'

    Id = Column(Integer, primary_key=True)
    UserId = Column(Integer, nullable=False, index=True, server_default=text("'0'"))
    CurrUserName = Column(String(20), nullable=False, index=True, server_default=text("''"))
    NewUserName = Column(String(20), nullable=False, index=True, server_default=text("''"))
    Created = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))


class AnonymousUser(Base):
    __tablename__ = 'AnonymousUser'
    __table_args__ = (
        Index('IX_DeviceID_AppID_Upgrade', 'DeviceId', 'AppId', 'IsUpgrade'),
    )

    Id = Column(Integer, primary_key=True)
    UserId = Column(Integer, nullable=False, index=True, server_default=text("'0'"))
    DeviceId = Column(String(100), nullable=False, server_default=text("''"))
    AppId = Column(String(100), nullable=False, server_default=text("''"))
    Created = Column(DateTime, nullable=False)
    IsUpgrade = Column(Integer, nullable=False, server_default=text("'0'"))
    UpgradeTime = Column(DateTime, nullable=False)


class ApiAppConfig(Base):
    __tablename__ = 'ApiAppConfig'

    Id = Column(Integer, primary_key=True)
    AppName = Column(String(50), nullable=False, server_default=text("''"))
    AppKey = Column(String(50), nullable=False, server_default=text("''"))
    AppSecret = Column(String(50), nullable=False, server_default=text("''"))
    Status = Column(Integer, nullable=False, server_default=text("'1'"))
    Created = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))


class AppOperationError(Base):
    __tablename__ = 'App_OperationError'

    OperationID = Column(Integer, primary_key=True)
    ErrorID = Column(Integer, nullable=False, index=True, server_default=text("'0'"))
    ErrorMessage = Column(String(500), server_default=text("''"))
    UserID = Column(Integer, nullable=False, index=True, server_default=text("'0'"))
    AccessToken = Column(String(50), nullable=False, server_default=text("''"))
    AppKey = Column(String(50), nullable=False, server_default=text("''"))
    Ip = Column(String(50), nullable=False, server_default=text("''"))
    ErrorTime = Column(DateTime, nullable=False)
    ServerID = Column(String(50), nullable=False, server_default=text("''"))
    Parameter = Column(String(500), server_default=text("''"))


class AppOperationErrorTye(Base):
    __tablename__ = 'App_OperationErrorTye'

    ErrorID = Column(Integer, primary_key=True, server_default=text("'0'"))
    ErrorName = Column(String(100), server_default=text("''"))
    UserMessage = Column(String(200), server_default=text("''"))
    SystemMessage = Column(String(200), server_default=text("''"))


class AppSkipWhiteList(Base):
    __tablename__ = 'App_SkipWhiteList'

    ID = Column(Integer, primary_key=True)
    Url = Column(String(1024), nullable=False, server_default=text("''"))
    Skips = Column(String(500), nullable=False, server_default=text("''"))
    Disables = Column(String(500), nullable=False, server_default=text("''"))
    Description = Column(String(500), server_default=text("''"))
    Status = Column(Integer, nullable=False, server_default=text("'0'"))
    CreateTime = Column(DateTime, nullable=False)
    CreateUser = Column(Integer, nullable=False, server_default=text("'0'"))
    UpdateTime = Column(DateTime, nullable=False)
    UpdateUser = Column(Integer, nullable=False, server_default=text("'0'"))


class Avatar(Base):
    __tablename__ = 'Avatar_0'

    UserId = Column(Integer, primary_key=True, server_default=text("'0'"))
    AvatarHash = Column(String(50), nullable=False, server_default=text("''"))
    Created = Column(DateTime, nullable=False)
    Updated = Column(DateTime)


class BaseUser(Base):
    __tablename__ = 'BaseUser_0'

    UserId = Column(Integer, primary_key=True)
    UserName = Column(String(50), nullable=False, server_default=text("''"))
    ValidationCode = Column(String(16), nullable=False, server_default=text("''"))
    Validation = Column(String(32), nullable=False, server_default=text("''"))
    Created = Column(DateTime, nullable=False)
    Updated = Column(DateTime, nullable=False)

class DeviceType(Base):
    __tablename__ = 'DeviceType'

    Id = Column(Integer, primary_key=True)
    ClientRawdata = Column(String(300))
    RawDataHash = Column(String(32), unique=True)
    Platform = Column(String(30))
    DeviceModel = Column(String(30))
    OSVersion = Column(String(20))
    AppName = Column(String(40))
    AppVersion = Column(String(20))
    CreateTime = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))

class K12User(Base):
    __tablename__ = 'K12User'

    Id = Column(Integer, primary_key=True)
    UserId = Column(Integer, nullable=False, index=True, server_default=text("'0'"))
    GroupId = Column(Integer, nullable=False, server_default=text("'0'"))
    CategoryId = Column(Integer, nullable=False, server_default=text("'0'"))
    Created = Column(DateTime, nullable=False)
    Ext1 = Column(Integer, nullable=False, server_default=text("'0'"))
    Ext2 = Column(Integer, nullable=False, server_default=text("'0'"))
    Ext3 = Column(String(200), nullable=False, server_default=text("''"))
    Ext4 = Column(String(200), nullable=False, server_default=text("''"))


class RefreshTokenStorage(Base):
    __tablename__ = 'RefreshTokenStorage_0'

    Id = Column(BigInteger, primary_key=True)
    AppKey = Column(String(50), nullable=False, server_default=text("''"))
    UserId = Column(Integer, nullable=False, index=True, server_default=text("'0'"))
    AccessToken = Column(String(50), nullable=False, server_default=text("''"))
    Created = Column(DateTime, nullable=False)
    DeviceId = Column(String(50), nullable=False, server_default=text("''"))
    DeviceType = Column(String(50), nullable=False, server_default=text("''"))
    Expired = Column(DateTime, nullable=False)
    RefreshToken = Column(String(50), nullable=False, index=True, server_default=text("''"))



class RegField(Base):
    __tablename__ = 'Reg_Field'

    Id = Column(Integer, primary_key=True)
    Title = Column(String(50), nullable=False, server_default=text("''"))
    Icon = Column(String(200), nullable=False, server_default=text("''"))
    DisplayOrder = Column(Integer, nullable=False, server_default=text("'0'"))
    Created = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    Status = Column(Integer, nullable=False, server_default=text("'0'"))
    FollowerCount = Column(Integer, nullable=False, server_default=text("'0'"))
    Tag = Column(String(50), nullable=False, server_default=text("''"))
    Lang = Column(String(10), nullable=False, server_default=text("''"))


class RegFieldMap(Base):
    __tablename__ = 'Reg_FieldMap_0'

    Id = Column(Integer, primary_key=True)
    UserId = Column(Integer, nullable=False, index=True, server_default=text("'0'"))
    FieldId = Column(Integer, nullable=False, index=True, server_default=text("'0'"))
    Created = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    Modified = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    ProductId = Column(Integer, nullable=False, server_default=text("'0'"))
    IsActive = Column(Integer, nullable=False, server_default=text("'1'"))



class RegIpFilter(Base):
    __tablename__ = 'Reg_IpFilter'

    Id = Column(Integer, primary_key=True)
    Ip = Column(String(15), nullable=False, server_default=text("''"))
    FilterType = Column(Integer, nullable=False, server_default=text("'1'"))
    Status = Column(Integer, nullable=False, server_default=text("'1'"))
    Created = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    Creator = Column(String(50), nullable=False, server_default=text("''"))


class RegVisitorInfo(Base):
    __tablename__ = 'Reg_VisitorInfo_0'

    UserID = Column(Integer, primary_key=True, server_default=text("'0'"))
    VisitorID = Column(String(64))
    SessionID = Column(String(64))
    SiteSessionID = Column(String(50))
    PageUrl = Column(String(4000))
    DeviceID = Column(String(100))
    Terminal = Column(String(32))
    BiLogType = Column(String(120))
    RegSource = Column(String(128))
    UpdateTime = Column(DateTime, nullable=False)
    DateAdded = Column(DateTime, nullable=False)
    OpenId = Column(String(64))
    UnionId = Column(String(64))
    AppCode = Column(String(100))
    RegSourceParams = Column(String(64))
    BusinessDomain = Column(String(30))
    ExtJson = Column(String(6000))




class SmsValidationHistory(Base):
    __tablename__ = 'SmsValidationHistory'

    id = Column(Integer, primary_key=True)
    UserId = Column(Integer, nullable=False, index=True, server_default=text("'0'"))
    Mobile = Column(String(50), nullable=False, server_default=text("''"))
    ValidationTime = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))


class SubscriberCategoryInfo(Base):
    __tablename__ = 'SubscriberCategoryInfo'

    Id = Column(Integer, primary_key=True)
    Title = Column(String(128), nullable=False)
    Status = Column(Integer, nullable=False)
    CreateDate = Column(DateTime, nullable=False)
    UpdateDate = Column(DateTime, nullable=False)
    Type = Column(String(50))


class SubscriberInfo(Base):
    __tablename__ = 'SubscriberInfo'

    Id = Column(Integer, primary_key=True)
    UserId = Column(Integer, nullable=False, index=True)
    CategoryId = Column(Integer, nullable=False)
    Status = Column(SmallInteger, nullable=False)
    CreateDate = Column(DateTime, nullable=False, index=True)
    UpdateDate = Column(DateTime, nullable=False, index=True)


class UnsubscribeLog(Base):
    __tablename__ = 'UnsubscribeLog'

    Id = Column(Integer, primary_key=True)
    UserId = Column(Integer, nullable=False)
    Reason = Column(String(128), nullable=False)
    UnsubscribeDate = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))


class UserChangeLog(Base):
    __tablename__ = 'UserChangeLog'
    __table_args__ = (
        Index('IX_OperatorName', 'OperatorName', 'TargetUserName', 'OperateTime'),
        Index('IX_TargetUserID', 'TargetUserID', 'OperateColumn')
    )

    ID = Column(BigInteger, primary_key=True)
    OperateColumn = Column(String(50), nullable=False, server_default=text("''"))
    OldValue = Column(String(512), nullable=False, server_default=text("''"))
    NewValue = Column(String(512), nullable=False, server_default=text("''"))
    OperatorID = Column(Integer, nullable=False, server_default=text("'0'"))
    OperatorName = Column(String(50), nullable=False, server_default=text("''"))
    OperationWay = Column(String(50), nullable=False, server_default=text("''"))
    TargetUserID = Column(Integer, nullable=False, server_default=text("'0'"))
    TargetUserName = Column(String(50), nullable=False, server_default=text("''"))
    OperateTime = Column(DateTime, nullable=False)
    Summary = Column(String(200), nullable=False, server_default=text("''"))


class UserFlag(Base):
    __tablename__ = 'UserFlag'

    UserId = Column(Integer, primary_key=True, server_default=text("'0'"))
    Flags = Column(Integer, nullable=False, server_default=text("'0'"))
    AvatarUpdated = Column(DateTime, nullable=False)
    Updated = Column(DateTime, nullable=False)


class UserNotificationSetting(Base):
    __tablename__ = 'UserNotificationSetting'
    __table_args__ = (
        Index('INX_UserId', 'UserId', 'AppId'),
    )

    Id = Column(Integer, primary_key=True)
    UserId = Column(Integer, nullable=False, server_default=text("'0'"))
    AppId = Column(String(50), nullable=False, server_default=text("''"))
    ModuleId = Column(String(50), nullable=False, server_default=text("''"))
    FlagId = Column(String(50), nullable=False, server_default=text("''"))
    Created = Column(DateTime, nullable=False)
    Ext1 = Column(Integer, nullable=False, server_default=text("'0'"))
    Ext2 = Column(String(200), nullable=False, server_default=text("''"))
    DeviceId = Column(String(50), nullable=False, server_default=text("''"))


class WechatAppConfig(Base):
    __tablename__ = 'WechatAppConfig'

    id = Column(Integer, primary_key=True)
    applicationName = Column(String(100), nullable=False, server_default=text("''"))
    appId = Column(String(50), nullable=False, server_default=text("''"))
    appsecret = Column(String(50), nullable=False, server_default=text("''"))
    addTime = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updateTime = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    status = Column(Integer, nullable=False, server_default=text("'0'"))


class WhiteList(Base):
    __tablename__ = 'WhiteList'

    Id = Column(Integer, primary_key=True)
    UserId = Column(Integer, nullable=False, index=True, server_default=text("'0'"))
    UserType = Column(Integer, nullable=False, server_default=text("'0'"))
    Status = Column(Integer, nullable=False, server_default=text("'0'"))
    Created = Column(DateTime, nullable=False)


class AppUserLogin(Base):
    __tablename__ = 'app_UserLogin_0'

    ID = Column(BigInteger, primary_key=True)
    UserID = Column(Integer, nullable=False, index=True, server_default=text("'0'"))
    LoginType = Column(Integer, nullable=False, server_default=text("'0'"))
    LoginDateValue = Column(Integer, nullable=False, server_default=text("'0'"))
    CreateTime = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    loginFrom = Column(Integer, nullable=False, server_default=text("'0'"))
    loginIp = Column(String(50), nullable=False, server_default=text("''"))
    UserName = Column(String(50), nullable=False, server_default=text("''"))
    LoginAction = Column(String(24))
    DeviceId = Column(String(120))
    AreaInfo = Column(String(30))
    DeviceType = Column(Integer)


class ClubSignature(Base):
    __tablename__ = 'club_Signature'

    UserID = Column(Integer, primary_key=True, server_default=text("'0'"))
    UserName = Column(String(50), nullable=False, server_default=text("''"))
    NickName = Column(String(100), server_default=text("''"))
    Signature = Column(String(20), nullable=False, server_default=text("''"))
    Introduction = Column(String(100), nullable=False, server_default=text("''"))
    LastUpdated = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    AuditType = Column(Integer, server_default=text("'0'"))


class UserRegdevice(Base):
    __tablename__ = 'user_regdevice'

    UserId = Column(Integer, primary_key=True, server_default=text("'0'"))
    Device = Column(String(10), nullable=False, server_default=text("''"))
    OS = Column(String(10), nullable=False, server_default=text("''"))
    Created = Column(DateTime, nullable=False)





class AdminActionInfo(Base):
    __tablename__ = 'Admin_ActionInfo'

    ID = Column(Integer, primary_key=True)
    ActionName = Column(String(50), nullable=False, server_default=text("''"))
    ActionPath = Column(String(200), nullable=False, server_default=text("''"))
    Status = Column(Integer, nullable=False, server_default=text("'0'"))
    CreateTime = Column(DateTime, nullable=False)
    CreateUser = Column(Integer, nullable=False, server_default=text("'0'"))
    UpdateTime = Column(DateTime, nullable=False)
    UpdateUser = Column(Integer, nullable=False, server_default=text("'0'"))


class AdminOperationLog(Base):
    __tablename__ = 'Admin_OperationLog'

    ID = Column(Integer, primary_key=True)
    LogType = Column(Integer, nullable=False, server_default=text("'0'"))
    Operator = Column(String(50), nullable=False, server_default=text("''"))
    OperateTime = Column(DateTime, nullable=False)
    Title = Column(String(200), nullable=False, server_default=text("''"))
    Content = Column(String(1000), nullable=False, server_default=text("''"))


class AdminRoleAction(Base):
    __tablename__ = 'Admin_RoleAction'
    __table_args__ = (
        Index('IX_Admin_RoleAction', 'RoleID', 'ActionID'),
    )

    ID = Column(Integer, primary_key=True)
    RoleID = Column(Integer, nullable=False, server_default=text("'0'"))
    ActionID = Column(Integer, nullable=False, server_default=text("'0'"))
    Status = Column(Integer, nullable=False, server_default=text("'0'"))
    CreateTime = Column(DateTime, nullable=False)
    CreateUser = Column(Integer, nullable=False, server_default=text("'0'"))
    UpdateTime = Column(DateTime, nullable=False)
    UpdateUser = Column(Integer, nullable=False, server_default=text("'0'"))


class AdminRoleInfo(Base):
    __tablename__ = 'Admin_RoleInfo'

    ID = Column(Integer, primary_key=True)
    RoleName = Column(String(50), nullable=False, server_default=text("''"))
    Status = Column(Integer, nullable=False, server_default=text("'0'"))
    CreateTime = Column(DateTime, nullable=False)
    CreateUser = Column(Integer, nullable=False, server_default=text("'0'"))
    UpdateTime = Column(DateTime, nullable=False)
    UpdateUser = Column(Integer, nullable=False, server_default=text("'0'"))


class AdminUserInfo(Base):
    __tablename__ = 'Admin_UserInfo'

    UserID = Column(Integer, primary_key=True, server_default=text("'0'"))
    Name = Column(String(50), nullable=False, server_default=text("''"))
    Description = Column(String(200), server_default=text("''"))
    Status = Column(Integer, nullable=False, server_default=text("'0'"))
    CreateTime = Column(DateTime, nullable=False)
    CreateUser = Column(Integer, nullable=False, server_default=text("'0'"))
    UpdateTime = Column(DateTime, nullable=False)
    UpdateUser = Column(Integer, nullable=False, server_default=text("'0'"))


class AdminUserRole(Base):
    __tablename__ = 'Admin_UserRole'
    __table_args__ = (
        Index('IX_Admin_UserRole', 'UserID', 'RoleID'),
    )

    ID = Column(Integer, primary_key=True)
    UserID = Column(Integer, nullable=False, server_default=text("'0'"))
    RoleID = Column(Integer, nullable=False, server_default=text("'0'"))
    Status = Column(Integer, nullable=False, server_default=text("'0'"))
    CreateTime = Column(DateTime, nullable=False)
    CreateUser = Column(Integer, nullable=False, server_default=text("'0'"))
    UpdateTime = Column(DateTime, nullable=False)
    UpdateUser = Column(Integer, nullable=False, server_default=text("'0'"))
