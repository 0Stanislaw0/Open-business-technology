from objectpack.ui import BaseEditWindow
from m3_ext.ui import all_components as ext


class UserAddWindow(BaseEditWindow):

    def _init_components(self):
        """
        Здесь следует инициализировать компоненты окна и складывать их в
        :attr:`self`.
        """
        super(UserAddWindow, self)._init_components()

        self.field__username = ext.ExtStringField(
            label=u'username',
            name='username',
            allow_blank=False,
            anchor='100%')

        self.field__first_name = ext.ExtStringField(
            label=u'first name',
            name='first_name',
            allow_blank=False,
            anchor='100%')

        self.field__last_name = ext.ExtStringField(
            label=u'last name',
            name='last_name',
            allow_blank=False,
            anchor='100%')

        self.field__password = ext.ExtStringField(
            label=u'password',
            name='password',
            anchor='100%')

        self.field__email = ext.ExtStringField(
            label=u'email',
            name='email',
            anchor='100%')

        self.field__is_staff = ext.ExtCheckBox(
            label=u'staff status',
            name='is_staff',
            anchor='100%')

        self.field__is_superuser = ext.ExtCheckBox(
            label=u'superuser status',
            name='is_superuser',
            anchor='100%')

        self.field__is_active = ext.ExtCheckBox(
            label=u'active status',
            name='is_active',
            anchor='100%')

        self.field__date_joined = ext.ExtDateField(
            label=u'date joined',
            name='date_joined',
            format='d.m.Y'
        )
        self.field__last_login = ext.ExtDateField(
            label=u'last login',
            name='last_login',
            format='d.m.Y'
        )

    def _do_layout(self):
        """
        Здесь размещаем компоненты в окне
        """
        super(UserAddWindow, self)._do_layout()
        self.form.items.extend((
            self.field__username,
            self.field__is_superuser,
            self.field__last_login,
            self.field__first_name,
            self.field__last_name,
            self.field__email,
            self.field__password,
            self.field__is_staff,
            self.field__is_active,
            self.field__date_joined,
        ))

    def set_params(self, params):
        """
        Установка параметров окна

        :params: Словарь с параметрами, передается из пака
        """
        super(UserAddWindow, self).set_params(params)
        self.height = 'auto'


class UserEditWindow(UserAddWindow):
    pass
