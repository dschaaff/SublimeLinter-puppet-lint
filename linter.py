#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Andrew Grim
# Copyright (c) 2014 Andrew Grim
#
# License: MIT
#

"""This module exports the PuppetLint plugin class."""

from SublimeLinter.lint import RubyLinter


class PuppetLint(RubyLinter):
    """Provides an interface to puppet-lint."""

    defaults = {
        'selector': 'source.puppet'
    }

    cmd = ('puppet-lint', '--log-format', '%{line}:%{column}:%{kind}:%{message}')
    regex = (
        r'^(?P<line>\d+):(?P<col>\d+):'
        r'((?P<warning>warning)|(?P<error>error)):'
        r'(?P<message>.+)'
    )
    tempfile_suffix = '-'

    def cmd(self):
        """Build command, using bundle exec if the option is set."""

        settings = self.get_view_settings()

        command = []

        if settings.get('use_bundle_exec', False):
            command.extend(['bundle', 'exec'])

        command.extend([
            'puppet-lint',
            '--log-format',
            '%{line}:%{column}:%{kind}:%{message}',
        ])

        return command
