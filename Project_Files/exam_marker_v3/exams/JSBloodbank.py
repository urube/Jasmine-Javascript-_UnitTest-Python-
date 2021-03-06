language = 'JAVASCRIPT'
whole = 'BloodBank'
part = 'Donor'
add_part = 'addDonor'
find_part = 'findDonor'
part_data = 'NationalID	First Name	Last Name	Gender\n'
part_data += '9800100      Jonathan    Watts       M\n'
part_data += '4023500      Sandy       Moore       F\n'
part_data += '7906553      John        Burk        M\n'
part_data += '5000990      Daniel      McDonald    M\n'
part_data += '6896701      Cathy       Watson      F\n'
part_output = 'Watts, Jonathan [M]\n'
part_output += 'Moore, Sandy [F]\n'
part_output += 'Burk, John [M]\n'
part_output += 'McDonald, Daniel [M]\n'
part_output += 'Waterson, Cathy [F]\n'
get_part = 'displayDonors'
sub_part = 'Donation'
add_sub_part = 'addDonation'
sub_part_data = 'NationalId   BranchName     Town      DonationDate    BloodGroup\n'
sub_part_data += '4023500     Christchurch   Addington  01/12/2018      AB+\n'
sub_part_data += '5000990     Wellington     Newtown    30/08/2017      O-\n'
sub_part_data += '6896701     Auckland       Manuka     11/07/2019      O+\n'
sub_part_data += '7906553     North Shore    Takapuna   15/12/2016      B-\n'
sub_part_data += '9800100     Nelson         Tahunanui  09/11/2017      AB+\n'
sub_part_data += '9800100     Otago          Dunedin    05/10/2018      AB+\n'
boolean_method = 'hasPositiveBloodGroup'
boolean_condition = 'their blood group ends with a \'+\''
boolean_condition3 = 'who has positive blood group'
get_sub_parts = 'displayPositiveDonations'
sub_part_output = 'Moore, Sandy [F]\n'
sub_part_output += '	Has blood group <AB+> donated on 12/1/2018 at Christchurch\n'
sub_part_output += 'Watson, Cathy [F]\n'
sub_part_output += '    Has blood group <O+> donated on 7/15/2019 at Auckland\n'
sub_part_output += 'Watts, Jonathan [M]\n'
sub_part_output += '	Has blood group <AB+> donated on 11/9/2017 at Nelson\n'
sub_part_output += '	Has blood group <AB+> donated on 10/5/2019 at Otago\n'


