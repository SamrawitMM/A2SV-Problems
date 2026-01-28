class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = []
        losers = []
        
        for won, lost in matches:
            winners.append(won)
            losers.append(lost)

        
        never_lost = sorted(set(winners) - set(losers))

        freq_loser = {}
        for loser in losers:
            freq_loser[loser] = freq_loser.get(loser, 0) + 1

    
        lost_once = sorted(
            [ loser for loser, freq in freq_loser.items() if freq == 1]
            )

        
        return [never_lost, lost_once]

        
