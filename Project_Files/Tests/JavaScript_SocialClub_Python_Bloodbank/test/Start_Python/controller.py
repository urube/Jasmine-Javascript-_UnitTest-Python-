from bloodbank import BloodBank
from datetime import date


def setup():
    the_blood_bank = BloodBank()
    the_blood_bank.add_donor(9800100, 'Jonathan', 'Watts', 'M')
    the_blood_bank.add_donor(4023500, 'Sandy', 'Moore', 'F')
    the_blood_bank.add_donor(7906553, 'John', 'Burk', 'M')
    the_blood_bank.add_donor(5000990, 'Daniel', 'McDonald', 'M')
    the_blood_bank.add_donor(6896701, 'Cathy', 'Watson', 'F')

    # NationalId  First Name  Last Name  Gender
    # 9800100     Jonathan    Watts       M
    # 4023500     Sandy       Moore       F
    # 7906553     John        Burk        M
    # 5000990     Daniel      McDonald    M
    # 6896701     Cathy       Watson      F
    
    # ADD CODE BELOW HERE FOR QUESTION 2
    
    
  
    # NationalId   BranchName     Town      DonationDate    BloodGroup
    # 4023500      Christchurch  Addington  01/12/2018      AB+
    # 5000990      Wellington    Newtown    30/08/2017      O-
    # 6896701      Auckland      Manuka     11/07/2019      O+
    # 7906553      North Shore   Takapuna   15/12/2016      B-
    # 9800100      Nelson        Tahunanui  09/11/2017      AB+
    # 9800100      Otago         Dunedin    05/10/2018      AB+




if __name__ == '__main__':
    a_bank = setup()
