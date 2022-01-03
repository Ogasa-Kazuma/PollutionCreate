
class ScatterSettingConductor():

  def __init__(self, ax):
      self.__ax = ax

  def ApplySetting(self, aspect = "equal"):
      self.__ax.set_aspect(str(aspect))
