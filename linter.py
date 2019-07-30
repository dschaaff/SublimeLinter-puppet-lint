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

from SublimeLinter.lint import RubyLinter, util


class PuppetLint(RubyLinter):

    """Provides an interface to puppet-lint."""

    defaults = {
        'selector': 'source.puppet'
    }
    cmd = ('puppet-lint', '--log-format', '%{line}:%{column}:%{kind}:%{message}', '*')
    executable = None
    regex = (
        r'^(?P<line>\d+):(?P<col>\d+):'
        r'((?P<warning>warning)|(?P<error>error)):'
        r'(?P<message>.+)'
    )
    tempfile_suffix = '-'
    error_stream = util.STREAM_STDOUT
    word_re = r'^(".*?"|[-\w]+)'
