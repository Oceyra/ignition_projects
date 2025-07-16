def queryStatus(minPriority = 0, maxPriority = 4, tagPath = None, displayPath = None, includeAcked = True, includeCleared = False, includeShelved = False):
	"""Queries the current state of alarms. The result is a list of alarm events, which can be parsed for individual properties. The results provided by this function represent the current state of alarms
	Args:
		minPriority (int): Minimum priority to match. Priorities values: Diagnostic(0), Low(1), Medium(2), High(3), Critical(4).
		maxPriority (int): Maximum priority to match.
		tagPath (str): Source path to search at. The wildcard "*" may be used.
		displayPath (str): Display path to search at. Display path is separated by "/", and if path ends in "/*", everything below that path will be searched as well.
		includeAcked (bool): A flag indicating whether acked events should be included in the results.
		includeCleared (bool): A flag indicating whether cleared events should be included in the results.
		includeShelved (bool): A flag indicating whether shelved events should be included in the results.
	Returns:
		A list of alarm events
	"""

	"""
	String			Integer Representation
	ClearUnacked	0
	ClearAcked		1
	ActiveUnacked	2
	ActiveAcked		3
	"""
	states = range(0, 4)
	
	if not includeAcked:
		states = [state for state in states if state%2 == 0]

	if not includeCleared:
		states = [state for state in states if state >= 2]
	
	results = system.alarm.queryStatus(
		priority = range(minPriority, maxPriority + 1),
		state = states,
		path = [ tagPath ],
		displaypath = [ displayPath ],
		includeShelved = includeShelved)
	
	return [{
		'id': result.getId(),
		'name': result.getName(),
		'priority': result.getPriority(),
		'state': result.getState()
	} for result in results]