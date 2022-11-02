from datetime import date

class CreditCard:
    def __init__(self, expiryMonth, expiryYear, firstName, lastName, ccNumber):
        self.__expiryMonth = expiryMonth
        self.__expiryYear = expiryYear
        self.__firstName = firstName
        self.__lastName = lastName
        self.__ccNumber = ccNumber

    def formatExpiryDate(self):
        date_format = str(self.__expiryMonth) + "/" + str(self.__expiryYear)
        return date_format

    def formalFullName(self):
        fullName = self.__firstName + " " + self.__lastName
        return fullName

    def formatCCNumber(self):
        card_number = self.__ccNumber
        n = 4
        split_card_number = [card_number[idx:idx + n] for idx in range(0, len(card_number), n)]
        return (" ".join(split_card_number))

    def is_valid(self):
        current_date = date.today()
        current_month = current_date.strftime("%m")
        current_year = current_date.strftime("%Y")
        if self.__expiryMonth >= int(current_month):
            if self.__expiryYear >= int(current_year):
                return True
            else:
                return False
        elif self.__expiryMonth <= int(current_month):
            if self.__expiryYear <= int(current_year):
                return True
            else:
                return False
    def __str__(self):
        return f'Number: {self.formatCCNumber()} Expiry date: {self.formatExpiryDate()} Account holder: {self.formalFullName()} Is valid? {self.is_valid()}'

cc1 = CreditCard(10,2014,"Bob", "Jones", "1234567890123456")
print(cc1.__str__())
