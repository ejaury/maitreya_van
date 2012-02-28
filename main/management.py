import sys

from django.contrib.auth.management import _get_all_permissions
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.db import models
        
def create_proxy_permissions(app, **kwargs):
    """
        Creates permissions for proxy models which are not created automatically
        by `django.contrib.auth.management.create_permissions`.
        see https://code.djangoproject.com/ticket/11154
        This method is inspired by `django.contrib.auth.managment.create_permissions`.
        
        Since we can't rely on `get_for_model' we must fallback to `get_by_natural_key`.
        However, this method doesn't automatically create missing `ContentType` so
        we must ensure all the model's `ContentType` are created before running this method.
        We do so by unregistering the `update_contenttypes` `post_syncdb` signal and calling
        it in here just before doing everything.

        Adapted from http://djangosnippets.org/snippets/2677/.
    """
    app_mod = models.get_app(app)
    app_models = models.get_models(app_mod)
    # This will hold the permissions we're looking for as
    # (content_type, (codename, name))
    searched_perms = list()
    # The codenames and ctypes that should exist.
    ctypes = set()
    for model in app_models:
        opts = model._meta
        if opts.proxy:
            # We can't use `get_for_model` here since it doesn't return 
            # the correct `ContentType` for proxy models.
            # see https://code.djangoproject.com/ticket/17648
            app_label, model = opts.app_label, opts.object_name.lower()
            ctype = ContentType.objects.get_by_natural_key(app_label, model)
            ctypes.add(ctype)
            for perm in _get_all_permissions(opts):
                searched_perms.append((ctype, perm))
    
    # Find all the Permissions that have a content_type for a model we're
    # looking for. We don't need to check for codenames since we already have
    # a list of the ones we're going to create.
    all_perms = set(Permission.objects.filter(
        content_type__in=ctypes,
    ).values_list(
        "content_type", "codename"
    ))
    
    objs = [
        Permission(codename=codename, name=name, content_type=ctype)
        for ctype, (codename, name) in searched_perms
        if (ctype.pk, codename) not in all_perms
    ]
    for ctype, (codename, name) in searched_perms:
        if (ctype.pk, codename) not in all_perms:
            Permission.objects.get_or_create(codename=codename, name=name, content_type=ctype)

    #for obj in objs:
    #    sys.stdout.write("Adding permission '%s'" % obj)
            
from south import signals
signals.post_migrate.connect(create_proxy_permissions)
