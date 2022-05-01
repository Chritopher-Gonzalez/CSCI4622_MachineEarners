import numpy as np


def basicStrat(dealer, player, isSoft):
	# Hit:   return True
	# Stand: return False
	if(isSoft == False):
		if(player >= 17):
			return False

		if(player >= 13):
			if(dealer <= 6):
				return False
			else:
				return True

		if(player == 12):
			if(dealer <= 3):
				return True
			if(dealer <= 6):
				return False
			else:
				return True

		else:
			return True

	else:
		if(player >= 19):
			return False

		if(player == 18):
			if(dealer <= 8):
				return False

	return True