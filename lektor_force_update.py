# -*- coding: utf-8 -*-
from lektor.pluginsystem import Plugin
from lektor.assets import File
from lektor.db import Page
from lektor.utils import bool_from_string as asBool
from lektor.reporter import reporter


class ForceUpdatePlugin(Plugin):
    name = u'Force Update'
    description = u'Update files regardless of changed state'
    msg_init_config = '''Plugin not properly configured.

configs/force-update.ini:
  enabled = yes
  endswith = .appcache, .webmanifest, ...
'''
    patterns = list()

    def matchesPattern(self, source):
        if isinstance(source, Page):
            path = source.path
        elif isinstance(source, File):
            path = source.source_filename
        else:
            return False
        return any(path.endswith(x) for x in self.patterns)

    def on_after_build(self, builder, build_state, source, prog, **extra):
        if self.enabled and self.matchesPattern(source):
            for artifact in prog.artifacts:
                artifact.set_dirty_flag()

    def on_setup_env(self, **extra):
        prefs = self.get_config()
        endswith = prefs.get('endswith')
        if endswith is None:
            raise RuntimeError(self.msg_init_config)

        self.enabled = asBool(prefs.get('enabled'), default=True)
        if self.enabled:
            for pattern in endswith.split(','):
                self.patterns.append(pattern.strip())
            if len(self.patterns) == 0:
                self.enabled = False

        readable = 'ENABLED' if self.enabled else 'DISABLED'
        reporter.report_generic('Plugin ' + readable + ': force-update')
