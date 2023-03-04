# Model Techniques

This file explains how to represent certain special test results with the given data classes:

- 'Zwarte Vrijstelling': Do not set jokers to a value > 0 and do not set immunity to true even if the player used a
'Vrijstelling' or used any jokers.

- Multiple drop offs: If during an episode multiple players drop off/see a red screen after an execution because they had
the worst score for the same test then it should be modelled as a single Episode dataclass with DropType.EXECUTION_DROP
and the players that dropped off in a single list. If during an episode multiple players drop off/see a red screen after
different executions because they had the worst score in different tests during the same episode n (which for example
happend during season 14 episode 1) then it should be modelled as two Episode dataclasses with episode numbers n and m
with n - 1 < m < n where the first event get the lowest episode number. Both episode dataclasses should have
DropType.EXECUTION_DROP and a list with the player that dropped off (single player). The same should be applied when
two players drop off with different reasons during the same episode (for example during season 13 episode 3). Of course
you should use different DropTypes.

- Returning players: Players that return after they dropped off should still have either DropType.EXECUTION_DROP or
DropType.VOLUNTARY_DROP in the episodes in which they dropped off and should be contained in the list of players in the
episode in which the player returns and in the episodes after that episode until the player drops off.

- Information during finals: If during the finals it is announced that someone is the winner then you should model it as
an Episode dataclass with DropType.POSSIBLE_DROP and with the remaining players contained in the list and the winner
should be added to the ManualExclusion layer. If during the finals it is announced that someone is the loser then you
should model it as an Episode dataclass with DropType.EXECUTION_DROP and the player that lost the game should be
contained in the list. If someone is said not to be the Mol then he should be added to the ManualExclusion Layer and
if someone is said not to be the loser then you should model it as a DropType.POSSIBLE_DROP with the remaining players
contained in the list.
