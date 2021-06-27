class SBI:
    def rate_of_interest(self):
        return 8


class GTBANK:
    def rate_of_interest(self):
        return 4


class ACCESS:
    def rate_of_interest(self):
        return 10


def common_interest(bank):
    return bank.rate_of_interest()


a = ACCESS()
print(common_interest(a))
