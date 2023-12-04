""" Modil ki gen tout fonksyon spesyal yo. """

import re

""" Fonsyon ki pemet nus verifye si antre yo se antye. """
def verifye_nonb_antye(chwa:str):  
    # foma_regex = re.compile(r"^\-?[0-9][1-9]*$")
    foma_regex = re.compile(r"^\-?[0-9]+(\.[0-9][0-9]?)*$")
    final_regex = re.match(foma_regex, chwa)
    
    if final_regex:
        return True
    else:
        return False
    

def verifye_nonb_menu(chwa:str):  
    foma_regex = re.compile(r"^[0-4]*$")
    final_regex = re.match(foma_regex, chwa)
    
    if final_regex:
        return True
    else:
        return False
    
def antre_nonb_kalkil_yo ():
    nonb1 = input("Antre premye nonb lan: ").strip()
    chwa_retou = verifye_nonb_antye(nonb1)

    while not chwa_retou:
        nonb1 = input("Antre premye nonb valid ou an: ").strip()
        chwa_retou = verifye_nonb_antye(nonb1)
            
    nonb2 = input("Antre dezyem nonb lan: ").strip()
    chwa_retou = verifye_nonb_antye(nonb2)

    while not chwa_retou:
        nonb2 = input("Antre dezyem nonb valid ou an: ").strip()
        chwa_retou = verifye_nonb_antye(nonb2)
        
    if "." in nonb1:
        nonb1 = float(nonb1)
    else:
        nonb1 = int(nonb1)
        
    if "." in nonb2:
        nonb2 = float(nonb2) 
    else:
        nonb2 = int(nonb2) 
    
    return nonb1, nonb2