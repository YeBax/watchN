import xadmin
from xadmin import views
from xadmin.plugins.auth import UserAdmin


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSetting(object):
    site_title = 'Watch-N'   # 设置头标题
    site_footer = '小N问答语料库管理平台'  # 设置脚标题
    menu_style = "accordion"


class UserProfileAdmin(UserAdmin):
    pass


xadmin.site.register(views.CommAdminView, GlobalSetting)
xadmin.site.register(views.BaseAdminView, BaseSetting)
