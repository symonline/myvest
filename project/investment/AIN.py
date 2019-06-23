from datetime import datetime as DateTime, timedelta as TimeDelta


def pro_plan(a):  # business logic
    # Determine the exact plan base on principal range from-
    # AMIN product rate guide Chat

    if a >= 500000 and a <= 999999:
        return 'lite'
    elif a >= 1000000 and a <= 9999999:
        return 'bronze'
    elif a>= 10000000 and a <= 49999999:
        return 'silver'
    elif a >= 50000000 and a <= 99999999:
        return 'gold'
    elif a > 99999999:
        return 'platinum'
    '''else:
        return 'invalid' '''

def pro_interest(pro_plan, r_chart, tenor):
    # fetch the appropriate interest based on tenor and plan
    for plan, rate in r_chart.items():
        if pro_plan in plan and tenor == 30:
            return [rate[0], pro_plan]
        elif pro_plan in plan and tenor == 60:
            return [rate[1], pro_plan]
        elif pro_plan in plan and tenor == 90:
            return [rate[2], pro_plan]
        elif pro_plan in plan and tenor == 182:
            return [rate[3], pro_plan]
        elif pro_plan in plan and tenor == 365:
            return [rate[4], pro_plan]
        '''else:
            return [0, pro_plan]'''

def computed_yield(rate, tenor, principal):
    # y=principal*(rate/100)*(tenor/365)

    value = principal * (float(rate[0]) / 100) * (tenor / 365)
    return value

def comp_wht(comp_yield, fee_type='flat', fee=0, WHT=0.1):
    # deducting Withholding Tax and other admin charges
    value_ = (comp_yield * WHT)
    '''if fee_type=='varies':
        fee=(fee/100)*comp_yield
        value_=(value_-fee)
        return value
    else:
    '''
    return value_  # (value_ - fee)

def proceed(principal, comp_y):
    # interest plus principal
    # (NAV)
    return principal + comp_y


def mature_date(tenor, startdate):
    # determine the maturity date

    date_str = startdate  # The date - 29 Dec 2017
    format_str = '%d/%m/%Y'  # The format
    datetime_obj = DateTime.strptime(date_str, format_str)
    mydate = datetime_obj.date()
    end_date = mydate + TimeDelta(days=tenor)
    return end_date


def adjust_rate_chart(plan):
    #
    pass

def enter_letter():
        #
    letter = str(input('Enter Duration e.g A=30Days,'
                       ' B=60Days, C=90Days, D=182Days, E=365Days : '))
    if letter not in ['A', 'B', 'C', 'D', 'E']:
        print('Invalid Tenor entered')
        return ['False', letter]
    else:
        return ['True', letter]

def _principal():
    return input('Enter Principal Amount to be Invested > =N 499,999.99 : ')

def invest():
    pass

def rollover():
    pass
#  ..................................................................


class user:
    # ...
    total_user = 0

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def open_account(self,):
        #
        pass

    def invest_fund(self,):
        #
        def rollover():
            #
            pass

        pass

    def change_name(self,):
        #
        pass

    def change_address(self,):
        #
        pass

    def change_details(self,):
        #
        pass

    def change_name(self,):
        #
        pass


class Customer(user):
    pass

new_name=Customer()



def main():
    #
    # All inputs
    product = 'APEL INVESTMENT NOTE(AIN)'
    principal = float(input('ENTER PRINCIPAL :'))
    #tenor=60

    lists = (list(enter_letter()))
    if 'True' in lists:
        if lists[1] == 'A':
            tenor = 30
        elif lists[1]=='B':
            tenor = 60
        elif lists[1]=='C':
            tenor = 90
        elif lists[1]=='D':
            tenor = 182
        elif lists[1]=='E':
            tenor = 365
        else:
            tenor = 0

    start_date = '02/04/2019'

    rate_chart = {'lite': [6.50, 7.00, 7.50, 8.00, 10.50],
                  'bronze': [8.00, 10.00, 12.00, 12.50, 13.00],
                  'silver': [9.00, 11.00, 13.00, 13.75, 14.50],
                  'gold': [10.50, 12.00, 14.00, 14.50, 16.00],
                  'platinum': [11.50, 13.00, 15.00, 15.50, 16.50],
                  'invalid': [0.00, 0.00, 0.00, 0.00, 0.00],
                  }
    # Program logic

    plans = pro_plan(principal)  # help identify the plan
    pro_int = (pro_interest(plans, rate_chart, tenor))  # help identify the rate to use
    cmp_yld = round(computed_yield(pro_int, tenor, principal),2)

    compute_wht = round(comp_wht(cmp_yld),2)
    proc = round(proceed(principal, cmp_yld)-compute_wht, 2)
    mat_dt = mature_date(tenor, start_date)

    # Screen output

    print(f'PRODUCT NAME:              {product}')
    print('PRINCIPAL:                 =N {:,.2f}'.format(principal))
    print('RATE:                         {:,.2f} %'.format(pro_int[0]))
    print(f'TENOR:                        {tenor} days')
    print(f'EFFECTIVE DATE:               {start_date}')
    print(f'MATURITY DATE:                {mat_dt}')
    print('INTEREST:                  =N {:,.2f}'.format(cmp_yld))
    print('WITHOLDING TAX:            =N {:,.2f}'.format(compute_wht))
    print('VALUE AT MATURITY:         =N {:,.2f}'.format(proc))


main()


