import random as rand
from data.hl7_data import facilities, hl7_apps
from data.names_data import male_names, female_names, last_names
from data.radiology_data import chest_xray_interpretations, abdominal_xray_interpretations, spinal_xray_interpretations, extremity_xray_interpretations, pediatric_xray_interpretations, miscellaneous_xray_interpretations
from clinical import xray
from personal import first_name, last_name, dob, sex, phone_number, ssn, address

def hl7_message(msg_type=None):
    if msg_type == None:
        msg_type = rand.choice(['adt', 'orm', 'dft'])

    if msg_type == 'adt': 
        MSH = f"MSH|^~\\&|{rand.choice(hl7_apps)}|{rand.choice(facilities)}|{rand.choice(hl7_apps)}|{rand.choice(facilities)}|202310031200||ORM^O01|1234567890|P|2.3"
        PID = f"PID|1||123456^^^Hospital^MR||{rand.choice(last_names)}^{rand.choice(male_names + female_names)}^^^||{dob()}|{sex()}|||{address('street')}^^{address('city')}^{address('state')}^{address('zip')}||{phone_number()}|||||||"
        PV1 = f"PV1|1|{rand.choice(['I', 'O', 'E'])}|Floor^Room^Bed|U|A0||||{rand.randint(100000000, 999999999)}^^{rand.choice(male_names + female_names)}^^^Dr.|||||||||||||||202310031200"
        ORC = f"ORC|NW|1234567890||||||202310031200|||A0"
        OBR = f"OBR|1|1234567890|9876543210^Radiology^L|||202310031200|||||||||||||||202310031200|||||||F|||||||"
        OBX = f"OBX|1|{address('state')}|12345^Radiology Report^L||{xray()}|||F|||202310031200"
        hl7_message = "\n".join([MSH, PID, PV1, ORC, OBR, OBX])

    elif msg_type == 'orm':
        MSH = f"MSH|^~\\&|{rand.choice(hl7_apps)}|{rand.choice(facilities)}|{rand.choice(hl7_apps)}|{rand.choice(facilities)}|202310031200||ORM^O01|1234567890|P|2.3"
        PID = "PID|1||123456^^^Hospital^MR||Doe^John^^^Mr.||19800101|M|||123 Main St^^Anytown^CA^12345||(555)555-5555|||||||"
        ORC = "ORC|NW|1234567890||||||202310031200|||A0"
        OBR = "OBR|1|1234567890|9876543210^Radiology^L|||202310031200|||||||||||||||202310031200|||||||F|||||||"
        hl7_message = "\n".join([MSH, PID, ORC, OBR])
    elif msg_type == 'dft':
        MSH = f"MSH|^~\\&|{rand.choice(hl7_apps)}|{rand.choice(facilities)}|{rand.choice(hl7_apps)}|{rand.choice(facilities)}|202310031200||DFT^P03|1234567890|P|2.3"
        PID = "PID|1||123456^^^Hospital^MR||Doe^John^^^Mr.||19800101|M|||123 Main St^^Anytown^CA^12345||(555)555-5555|||||||"
        FT1 = "FT1|1|1234567890||||202310031200|||A0|||||||"
        PV1 = "PV1|1|I|Ward^Room^Bed|U|A0||||1234^Smith^John^^^Dr.|||||||||||||||202310031200"
        IN1 = "IN1|1|123456^^^Insurance^ID||Doe^John^^^Mr.|||||||||||||||202310031200"
        hl7_message = "\n".join([MSH, PID, FT1])
    
    return hl7_message
