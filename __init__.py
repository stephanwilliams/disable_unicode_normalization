import unicodedata

from anki.hooks import addHook
from aqt import mw
from aqt.qt import QAction

# save the original function
oldNormalize = unicodedata.normalize

# replacement function
def nop_normalize(norm, str):
    return str

normalizationDisabled = False

normalizationActions = {
    True: nop_normalize,
    False: oldNormalize
}

def toggleNormalization(action):
    global normalizationDisabled

    normalizationDisabled = not normalizationDisabled

    unicodedata.normalize = normalizationActions[normalizationDisabled]

    normalizationAction.setChecked(normalizationDisabled)

# config
def loadConfig():
    global normalizationDisabled

    normalizationDisabled = mw.pm.profile.get("normalizationDisabled", False)

    normalizationAction.setChecked(normalizationDisabled)

def saveConfig():
    mw.pm.profile["normalizationDisabled"] = normalizationDisabled

# create menu item
normalizationAction = QAction("Disable Unicode Normalization")
normalizationAction.setCheckable(True)
normalizationAction.triggered.connect(toggleNormalization)

mw.form.menuTools.addAction(normalizationAction)

# hooks
addHook("profileLoaded", loadConfig)
addHook("unloadProfile", saveConfig)
