import csv,os


def __extract_cscs_master(file_name):
    # use in extracting the CSCS_Master file
    with open(file_name, newline='') as data:
        extracted = csv.DictReader(data, delimiter='\t', fieldnames=[])
        inner_list = []
        for i, rec in enumerate(extracted, 1):
            inner_list.append(rec[None][0][:])
        return inner_list


def __list_cleaner(raw_list):
    # use in selecting & cleaning  needed fields from the extracted
    # cscs master list
    all_record = []
    for field in raw_list:
        chn, name, address = field[:15].upper(), field[15:55].upper(), field[55:175].upper(),
        state, email, phone = field[175:200].upper(), field[273:313].upper(), field[313:353].upper()
        all_record.append([chn.strip(),
                            name.strip(),
                            address.strip(),
                            state.strip(),
                            email.strip(),
                            phone.strip()])
    return all_record


def investors(raw_file):
    try:
        raw = __extract_cscs_master(raw_file)     # generate raw list
        investor_rec = __list_cleaner(raw)  # clean the list
        print(f'File Name: {raw_file}')
        return investor_rec
    except FileNotFoundError:
        return 'File Not Found'


def state_validation(investors_list):

    pass


def chn_validation():
    pass


def run():
    a = 0
    trial = 3
    while a < 3:
        print(f'\nYou have {trial} More Trail \n')
        file = str(input('Enter file name : '))
        if not os.path.exists(file):
            a += 1
            trial -= 1
            print('\nFILE NOT FOUND!')
            if trial == 0:
                print('GOODBYE!!!')
            # print(f'You have {trial} Trails')
        else:
            print(investors(file))
            break


# Execute program
if __name__ == '__main__':
    run()

#states = [abia:umu]