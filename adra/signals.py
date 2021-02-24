from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
# from .models import Profile
from django.contrib.sites.models import Site
from tenant_schemas.signals import post_schema_sync
from tenant_schemas.models import TenantMixin

#
# @receiver(post_save, sender=User)
# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#
#
# @receiver(post_save, sender=User)
# def save_profile(sender, instance, **kwargs):
#     instance.profile.save()


# def foo_bar(sender, tenant, **kwargs):
#     print(tenant)
#     print(tenant.domain_url)
#     print(sender)
#     from tenant.sh
#     Site.objects.create(domain=tenant.domain_url,name=tenant)
#
#
# post_schema_sync.connect(foo_bar, sender=TenantMixin)
