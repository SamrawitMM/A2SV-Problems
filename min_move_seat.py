class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()

        total = 0
        for s, t in zip(students, seats):
            total += abs(s - t)

        return total
