city = int(input("Введите число 1 - Тазовский или 2 - Газ-сале"))
if city == 1:
     city = 1
elif city == 2:
     city = 2
elif city != 1 and city != 2:
     print("Выбрано неверное значение, запустите файл заного")

plata = int(input('Введите номер платы(первое число с тех. данных)'))
port = int(input('Введите номер физического порта(второе число с тех. данных)'))
v_port = int(input('Введите номер виртуального порта(третье число с тех.данных'))

ploam = int(input('Введите ploam пароль (10 чисел, пример: 0123456789), обычно номер порта:'))

desc = input('Введите описание порта, улица/дом/квартира или организация, пример Pochtovaya_31A_2 или Pochtovaya_31_Myzei_')

ONT = int(input('Если оборудование GM/G670 то введите 1\n'
                'Если оборудование Huawei HG8245 H/T или смежное введите 2'))
if ONT == 1:
     ONT = 1
elif ONT == 2:
     ONT = 2
elif ONT != 1 and ONT != 2:
     print("Выбрано неверное значение, запустите файл заного")

if city == 1:
     profile = int(input('Введите профиль: 23 (Default_TR069) или 24 (Default)'))
elif city == 2:
     profile = int(input('Введите профиль: 23 (Default_TR069_old) или 123 (Default) или 124 (Defailt_TR69)'))

ims = int(input('c IMS - 1, без IMS - 2'))

if ONT == 1 and ims == 2:
     print(f'interface 0/{plata}\n'
           f'ont add {port} {v_port} password-auth "{ploam}" always-on omci ont-lineprofile-id {profile} ont-srvprofile-id {profile} desc "{desc}"\n'
           f'ont ipconfig  {port} {v_port} dhcp vlan 69 priority 5\n'
           f'quit\n'
           f'service-port vlan 3588 gpon {plata}/{port}/{v_port} ont 10 gemport 4 multi-service user-vlan 69 rx-cttr 10 tx-cttr 10\n'
           f'service-port vlan 3508 gpon {plata}/{port}/{v_port} ont 10 gemport 0 multi-service user-vlan 20 user-encap pppoe\n'
           f' \n')
elif ONT == 1 and ims == 1:
     print(f'interface 0/{plata}\n'
           f'ont add {port} {v_port} password-auth "{ploam}" always-on omci ont-lineprofile-id {profile} ont-srvprofile-id {profile} desc "{desc}"\n'
           f'ont ipconfig  {port} {v_port} dhcp vlan 69 priority 5\n'
           f'quit\n'
           f'service-port vlan 3588 gpon {plata}/{port}/{v_port} ont 10 gemport 4 multi-service user-vlan 69 rx-cttr 10 tx-cttr 10\n'
           f'service-port vlan 3548 gpon {plata}/{port}/{v_port} ont 10 gemport 2 multi-service user-vlan 30 inbound traffic-table name SIP outbound traffic-table name SIP'
           f'service-port vlan 3508 gpon {plata}/{port}/{v_port} ont 10 gemport 0 multi-service user-vlan 20 user-encap pppoe\n'
           f' \n')
elif ONT == 2 and ims == 2:
     print(f'interface 0/{plata}\n'
           f'ont add {port} {v_port} password-auth "{ploam}" always-on omci ont-lineprofile-id {profile} ont-srvprofile-id {profile} desc "{desc}"\n'
           f'ont ipconfig  {port} {v_port} dhcp vlan 69 priority 5\n'
           f'ont tr069-server-config 6 10 profile-id 1\n'
           f'quit\n'
           f'service-port vlan 3588 gpon {plata}/{port}/{v_port} ont 10 gemport 4 multi-service user-vlan 69 rx-cttr 10 tx-cttr 10\n'
           f'service-port vlan 3508 gpon {plata}/{port}/{v_port} ont 10 gemport 0 multi-service user-vlan 20 user-encap pppoe\n'
           f' \n')
elif ONT == 2 and ims == 1:
     print(f'interface 0/{plata}\n'
           f'ont add {port} {v_port} password-auth "{ploam}" always-on omci ont-lineprofile-id {profile} ont-srvprofile-id {profile} desc "{desc}"\n'
           f'ont ipconfig  {port} {v_port} dhcp vlan 69 priority 5\n'
           f'ont tr069-server-config 6 10 profile-id 1\n'
           f'quit\n'
           f'service-port vlan 3588 gpon {plata}/{port}/{v_port} ont 10 gemport 4 multi-service user-vlan 69 rx-cttr 10 tx-cttr 10\n'
           f'service-port vlan 3548 gpon {plata}/{port}/{v_port} ont 10 gemport 2 multi-service user-vlan 30 inbound traffic-table name SIP outbound traffic-table name SIP'
           f'service-port vlan 3508 gpon {plata}/{port}/{v_port} ont 10 gemport 0 multi-service user-vlan 20 user-encap pppoe\n'
           f' \n')