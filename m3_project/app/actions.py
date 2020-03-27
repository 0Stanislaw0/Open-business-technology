import objectpack
import objectpack.ui as ui

from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from objectpack.actions import ObjectPack
from .ui import UserAddWindow, UserEditWindow
from .controller import observer


class PermissionObjectPack(ObjectPack):
    """
    ObjectPack для модели Permission
    """

    model = Permission
    add_to_desktop = True
    add_to_menu = True

    edit_window = add_window = objectpack.ui.ModelEditWindow.fabricate(
        model, model_register=observer
    )

    columns = [
        {
            'data_index': '__unicode__',
            'hidden': True
        },
        {
            'data_index': 'name',
            'header': u'name',
            "searchable": True,

        },
        {
            'data_index': 'content_type',
            'header': u'content type',
            'sortable': True,

        },
        {
            'data_index': 'codename',
            'header': u'codename',
            "searchable": True,

        },
    ]


class GroupObjectPack(ObjectPack):
    """
    ObjectPack для модели Group
    """

    model = Group
    add_to_desktop = True
    add_to_menu = True

    edit_window = add_window = objectpack.ui.ModelEditWindow.fabricate(
        model, model_register=observer
    )

    columns = [
        {
            'data_index': '__unicode__',
            'hidden': True
        },
        {
            'data_index': 'name',
            'header': u'name',
            'sortable': True,
        },
        {
            'data_index': 'permissions',
            'header': u'permissions',
            "searchable": True,
        },
    ]


class ContentTypeObjectPack(ObjectPack):
    """
    ObjectPack для модели ContentType
    """

    model = ContentType
    add_to_desktop = True
    add_to_menu = True

    edit_window = add_window = objectpack.ui.ModelEditWindow.fabricate(
        model, model_register=observer
    )

    columns = [
        {
            'data_index': '__unicode__',
            'hidden': True
        },
        {
            'data_index': 'app_label',
            'header': u'app label',
            'sortable': True,
            'sort_fields': ('Username'),
        },
        {
            'data_index': 'model',
            "searchable": True,
            'header': u'model',
        },
        {
            'data_index': 'name',
            'header': u'name',

        },
    ]


class UserObjectPack(ObjectPack):
    """
    ObjectPack для модели User
    """

    model = User
    add_to_desktop = True
    add_to_menu = True

    add_window = UserAddWindow
    edit_window = UserEditWindow

    columns = [
        {
            'data_index': '__unicode__',
            'hidden': True
        },
        {
            'data_index': 'username',
            'header': u'username',
            'sortable': True,
            "searchable": True,
            'sort_fields': ('username'),
        },
        {
            'data_index': 'first_name',
            'header': u'first name',
            'sortable': True,
            "searchable": True,
            'sort_fields': ('first_name'),
        },
        {
            'data_index': 'last_name',
            'header': u'last name',
            'sortable': True,
            "searchable": True,
            'sort_fields': ('last_name'),
        },
        {
            'data_index': 'is_staff',
            'header': u' is staff',
        },
        {
            'data_index': 'is_superuser',
            'header': u' is superuser',
        },
        {
            'data_index': 'date_joined',
            'header': u' date joined',
            'filter': {
                'type': 'date',
            }
        },
        {
            'data_index': 'last_login',
            'header': u' last login',
            'filter': {
                'type': 'date',
            }
        },
        {
            'data_index': 'password',
            'header': u' password',
        },
    ]

    # def prepare_row(self, obj, request, context):
    #     obj.is_staff = (
    #         '<div class="x-grid3-check-col%s"></div>'
    #         % '-on' if obj.is_staff else ''
    #     )
    #     return obj
