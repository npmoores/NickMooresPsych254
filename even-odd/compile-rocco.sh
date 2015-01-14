#!/bin/bash

# 2013/01/13 rocco install notes (OS X 10.7):
# sudo gem install rocco
# (but then i get an error when i try running rocco,
# something about `process_markdown': uninitialized constant Rocco
# )
# apply quickfix to rocco binary, as noted by https://github.com/rtomayko/rocco/issues/69#issuecomment-4488791

rocco -o docs experiment.js even-odd.html style.css
# stopgap fix for new docco CSS location
cd docs
sed -e "s/http:\/\/jashkenas\.github\.com\/docco\/resources\///" -i .bak *
rm *.bak

osascript <<'APPLESCRIPT'
tell application "Google Chrome"
  set i to 0
    repeat with t in (tabs of first window)
        set i to i + 1
        if ({"experiment.js","even-odd.html","style.css"} contains title of t ) then
            tell t
              execute javascript "window.location.reload()"
            end tell
        end if
    end repeat
end tell
APPLESCRIPT