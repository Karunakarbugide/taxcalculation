
class Tax_Computation:


    def tax_compute(self, income_amount):

        amount = int(income_amount)


        with open('tax.txt') as f:
            lines = f.readlines()
            # print(lines[0])

        tax_rate = lines[::2]
        max_income = lines[1::2]

        tax_rate = [x.replace('\n', "") for x in tax_rate]
        max_income = [x.replace('\n', "") for x in max_income]

        rate_index = zip(max_income, tax_rate)
        rate_dict = dict(rate_index)

        tax_rate = 0

        if amount < 9875:
            a = amount * (float(rate_dict['9875']))
            tax_rate = rate_dict['9875']
        elif amount < 40125:
            a = (amount - 9875) * (float(rate_dict['40125'])) + ((float(rate_dict['9875'])) * 9875)
            tax_rate = rate_dict['40125']
        elif amount < 85525:
            a = (amount - 40125) * (float(rate_dict['85525'])) + ((float(rate_dict['40125'])) * (40125 - 9875)) + (
                    (float(rate_dict['9875'])) * 9875)
            tax_rate = rate_dict['85525']
        elif amount < 163300:
            a = (amount - 85525) * (float(rate_dict['163300'])) + (float(rate_dict['85525'])) * (85525 - 4012) + (
                    (float(rate_dict['40125'])) * (4012 - 9875)) + \
                ((float(rate_dict['9875'])) * 9875)
            tax_rate = rate_dict['163300']
        elif amount < 207350:
            a = (amount - 163300) * (float(rate_dict['207350'])) + (float(rate_dict['163300'])) * (163300 - 85525) + (
                float(rate_dict['85525'])) * (85525 - 4012) + \
                ((float(rate_dict['40125'])) * (4012 - 9875)) + ((float(rate_dict['9875'])) * 9875)

            tax_rate = rate_dict['207350']
        elif amount < 518400:
            a = (amount - 207350) * (float(rate_dict['518400'])) + (float(rate_dict['207350'])) * (207350 - 163300) + (
                float(rate_dict['163300'])) * (163300 - 85525) + \
                (float(rate_dict['85525'])) * (85525 - 4012) + \
                ((float(rate_dict['40125'])) * (4012 - 9875)) + ((float(rate_dict['9875'])) * 9875)
            tax_rate = rate_dict['518400']
        else:
            a = (amount - 518400) * (float(rate_dict['Inf'])) + (float(rate_dict['518400'])) * (518400 - 207350) + (
                float(rate_dict['207350'])) * (207350 - 163300) + (float(rate_dict['163300'])) * (163300 - 85525) + \
                (float(rate_dict['85525'])) * (85525 - 4012) + \
                ((float(rate_dict['40125'])) * (4012 - 9875)) + ((float(rate_dict['9875'])) * 9875)
            tax_rate = rate_dict['Inf']

        return a,tax_rate

