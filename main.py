import os

from messages import menu,menu_adisyon,menu_soustraksyon,menu_miltiplikasyon,menu_divizyon
from methodeSpecials import verifye_nonb_menu,antre_nonb_kalkil_yo
from calculs import fe_adisyon,fe_soustraksyon,fe_miltiplikasyon,fe_divizyon

menu()
chwa = input("Chwazi tip kalkil wap fe an: ").strip()
chwa_retou = verifye_nonb_menu(chwa)

while not chwa_retou:
    chwa = input("Chwazi chif ki koresponn ak tip kalkil wap fe an: ").strip()
    chwa_retou = verifye_nonb_menu(chwa)

match int(chwa):
    case 0:
        os.system("cls")
        print("\nOu kite pwogram nan avek sikse !\n")
        exit(0)
    case 1:
        menu_adisyon()
        nonb1, nonb2 = antre_nonb_kalkil_yo()
            
        print(f"\ntotal adisyon an se: {(fe_adisyon(nonb1, nonb2))}\n")
    case 2:
        menu_soustraksyon()
        nonb1, nonb2 = antre_nonb_kalkil_yo()
        print(f"\ntotal soustraksyon an se: {(fe_soustraksyon(nonb1, nonb2))}\n")
    case 3:
        menu_miltiplikasyon()
        nonb1, nonb2 = antre_nonb_kalkil_yo()
        
        if nonb1 == 0 or nonb2 == 0:
            print("\nTout nonb miltipliye pa zewo (0) egal anko a zewo (0)")
        else:
            print(f"\ntotal miltiplikasyon an se: {(fe_miltiplikasyon(nonb1, nonb2))}")
        print("\n")
    case 4:
        menu_divizyon()
        nonb1, nonb2 = antre_nonb_kalkil_yo()
        if nonb2 == 0:
            print("\nOu paka divize pa zewo (0)")
        else:
            print(f"\ntotal divizyon an se: {(fe_divizyon(nonb1, nonb2))}")
        print("\n")
        
        