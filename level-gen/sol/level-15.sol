times(10000) {
	turnRight;
	if (clearInFront?) {
		walkForward;
	} else {
		turnLeft;
		if (clearInFront?) {
			walkForward;
		} else {
			turnLeft;
			if (clearInFront?) {
				walkForward;
			} else {
				turnLeft;
				if (clearInFront?) {
					walkForward;
				} else {
					turnLeft;
					walkForward;
				}
			}
		}
	}
}