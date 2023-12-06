class Solution:

    def totalMoney(self, n: int) -> int:

        total = 0
        count = 1

        for days in range(n):
            # Calculate the week number (q) and day within the week (r)
            q, r = divmod(days, 7)

            # Increment the daily amount
            daily = count + r

            # Accumulate the total
            total += daily

            # Check if a new week has started
            if r == 6:
                count += 1

        return total
