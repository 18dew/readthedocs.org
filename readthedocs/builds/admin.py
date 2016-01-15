"""Django admin interface for `~builds.models.Build` and related models.

"""

from django.contrib import admin
from readthedocs.builds.models import Build, VersionAlias, Version, BuildCommandResult
from guardian.admin import GuardedModelAdmin


class BuildCommandResultInline(admin.TabularInline):
    model = BuildCommandResult
    fields = ('command', 'exit_code')


class BuildAdmin(admin.ModelAdmin):
    fields = ('project', 'version', 'type', 'state', 'success', 'length')
    list_display = ('project', 'success', 'type', 'state')
    raw_id_fields = ('project', 'version')
    inlines = (BuildCommandResultInline,)


class VersionAdmin(GuardedModelAdmin):
    search_fields = ('slug', 'project__name')
    list_filter = ('project', 'privacy_level')


admin.site.register(Build, BuildAdmin)
admin.site.register(VersionAlias)
admin.site.register(Version, VersionAdmin)
