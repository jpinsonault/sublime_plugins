import sublime, sublime_plugin
import re

class SelectNextMatchingWordCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        regions = view.sel()
        new_regions = []
        for region in regions:
            # last = regions[-1]
            search_start = region.end()

            search_string = r"(?<=\W){}(?=\W)".format(re.escape(view.substr(region)))
            next_match = view.find(search_string, search_start)
            if next_match and not view.sel().contains(next_match):
                view.sel().add(next_match)
                view.show(next_match)
                break
            # Else wrap search from the top
            else:
                wrapped_match = view.find(search_string, 0)
                if wrapped_match and not view.sel().contains(next_match):
                    view.sel().add(wrapped_match)
                    view.show(wrapped_match)
                    break


                    



