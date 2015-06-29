import os

import sublime
import sublime_plugin


class CsshintCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        filepath = self.view.file_name()
        packages = sublime.packages_path()
        args = {
            "cmd": [
                "csshint",
                filepath,
                # "--reporter",
                # os.path.join(packages, "CSSHint", "reporter.js")
            ],
            "file_regex": r"CSSHint: (.+)\]",
            "line_regex": r"(\d+),(\d+): (.*)$"
        }

        if sublime.platform() == "windows":
            args['cmd'][0] += ".cmd"
        elif sublime.platform() == "osx":
            args['path'] = "/usr/local/share/npm/bin:/usr/local/bin:/opt/local/bin"

        self.view.window().run_command('exec', args)
