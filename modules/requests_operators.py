import requests, json

def movistar_checker(p):

  MAIN_URL = 'https://mimovistar.movistar.co/u-route/baas/flow/v1.0/run/QueryCustomerInfoForNoLoginPay?t=1706806719580'

  headers = {
    'Content-Type':'application/ueefire',
    "Tenant-Id":"00000000005aCO0k1Bzs",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
  }

  r = requests.post(url=MAIN_URL, headers=headers, json={"model":None,"params":"{\"serviceNumber\":\"%s\"}" % p}).json()

  r = json.loads(r)

  if int(r['resCode']) != 0:
    return False

  data = r['result'][0]

  #NUMBERS CONTACT GET INFORMATION
  numbers_data = data['custContacts_NumberList']['custContacts_List']

  last_data = []

  for number in numbers_data:
    asd_temp = number.get('v01:value','')
    if asd_temp in last_data or asd_temp == '':
      pass
    else:
      last_data.append(asd_temp)

  #EMAILS DATA GET
  emails_data = data['emails']
  presentData, presentData2 =  emails_data.get('customerEmail'), emails_data.get('accountEmail')
  email_final_data = []

  if presentData:
    email_final_data.append(presentData)
  if presentData2:
    if presentData2 in email_final_data:
      pass
    else:
      email_final_data.append(presentData2)


  return {
    'STATUS': True,
    'OPERATOR': 'MOVISTAR',
    'PN': p,
    'DETAILS':{
      'CEDULA': data.get('idNumber'),
      'NAME': f'{data.get("firstName")} {data.get("middleName","")} {data.get("lastName","")} {data.get("secondLastName","")}',
      'EMAIL': email_final_data,
      'NUMBERS_CONTACT': last_data
    }
  }


def wom_checker(p):

  headers = {
      'Cookie': '_gcl_au=1.1.39938727.1706298068; _fbp=fb.1.1706298068713.251770491; _gid=GA1.2.1627795326.1706298069; _omappvp=X3gRsSCIs4VMfLGemjMTq9f5AtZoRg8ZwNdzn4mrY0WepbyRAjLI4HtiU2AJnL49KW4DWU1ctOCUNZgTeCqswJEQ0DMXJkiQ; TPIDC=r0h64p9k-2cf0uihyo-5db1qlo62vkychpf70iz-aqvs82bukwlhn9-negid-rjeo; cus=false; cwdcc=true; _tt_enable_cookie=1; _ttp=GvE0PYZgmZxpKCEFv-3DwdBJ7iq; user_allowed_save_cookie=%7B%221%22%3A1%7D; omSeen-lymfyxvkghjxqdsdwrwq=1706298081676; omSeen-riw2zsmcmjtvhy6oz3mx=1706298081676; om-lymfyxvkghjxqdsdwrwq=1706298084303; om-riw2zsmcmjtvhy6oz3mx=1706298084303; _hjSessionUser_2894450=eyJpZCI6ImQzZmVlNTE0LWJhZTItNWJiMS04M2IwLTdiYjgyNjA1ZjUzNiIsImNyZWF0ZWQiOjE3MDYyOTgwNzUxNTYsImV4aXN0aW5nIjp0cnVlfQ==; blueID=b5829f34-3bcc-4824-a5df-5ef937ed7c18; PHPSESSID=5e90c34374b6c8882ef0456b1709aa54; form_key=p83voBeqqLWFdB17; _clck=76yaqy%7C2%7Cfir%7C0%7C1486; private_content_version=3617d69139ee8871ae57e44156e3ba51; _gat_UA-190343970-1=1; _uetsid=daa3be40bc8211ee913a691f15d701ac; _uetvid=daa510c0bc8211eebb1ebd7cc873b2f6; wpnViewcount=1; cwdscc=true; _hjSession_2894450=eyJpZCI6IjQ2ZDVhZjg4LTAyZGUtNDUwOC05MWJhLWQzMDMzM2Q1ZDI5YSIsImMiOjE3MDYzODYzOTcyNzIsInMiOjAsInIiOjAsInNiIjoxLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=; cto_bundle=Q0x8xl9QZjglMkZFZ05kNFI5RiUyQmk1SDlia2VQMDRzMG9RaDNDd2xLNDhZUTU2UW1reDZySk1BSjIwbUNvZXNXRGpIRE1EMDlEczZ1TVo0SlVINmolMkY0eGppWkpMc0RUdWxWZHQwSGFXT2dxamc4dU5hRUt5a1ZTZXglMkZqMDhxbFFGSXBLMDRiczZTWEgybkI3VDlLJTJGNTRzNWE4c2NRJTNEJTNE; _sp_ses.96b0=*; _sp_id.96b0=e2a91289-7d74-4f07-9363-8b11634cd7c2.1706298077.3.1706386398.1706382667.5ea4513c-221d-4085-a7ae-8d829f5f813f.1ac1336a-fb17-40b3-8106-c2eee1c05a5f.e73b17cb-92de-49d9-868f-90e9685aca75.1706386398119.1; mage-cache-storage={}; mage-cache-storage-section-invalidation={}; mage-cache-sessid=true; _wpn_cotpc=1; sdtpc=1; mage-banners-cache-storage={}; _ga_K3CRD809H5=GS1.1.1706386399.3.0.1706386399.0.0.0; mage-messages=; recently_viewed_product={}; recently_viewed_product_previous={}; recently_compared_product={}; recently_compared_product_previous={}; product_data_storage={}; _ga=GA1.2.729671787.1706298069; _ga_R4XB2V2CLZ=GS1.1.1706386395.3.1.1706386448.7.0.0',
      'Accept': 'application/json, text/javascript, */*; q=0.01',
      'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
      'Accept-Encoding': 'gzip, deflate, br'
  }

  payload = f"phone={p}&form_key=p83voBeqqLWFdB17&valor=3500&is_recharge=2&productsku=IPP1420&productplan=Paquete+Mixto+3+d%C3%ADas&productid=2107"

  r = requests.post(url='https://wom.co/wom/recharge', headers=headers, data=payload).json()

  if r.get('error') == False:
      return {'STATUS': True, 'OPERATOR': 'WOM', 'pn': p} 
  else:
      return False
  
def tigo_checker(p):

  MAIN_URL = 'https://transacciones.tigo.com.co/servicios/purchage_package?q=/servicios/purchage_package&package=shop201%7Chora&_wrapper_format=drupal_modal&ajax_form=1&_wrapper_format=drupal_ajax'

  headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.216 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate, br"
  }

  data = f"msisdn=({p[:3]})+{p[3:6]}-{p[-4:]}&email=test%40test.com&form_id=modal_anonymours_package_purchase_form&_triggering_element_name=op&_triggering_element_value=COMPRAR&_drupal_ajax=1&ajax_page_state%5Btheme%5D=tigo_theme"

  r = requests.post(url=MAIN_URL, headers=headers, data=data).text

  if 'no encontrada, revisa el numero de' in r:
    return False
  
  elif 'es posible ofrecerte el paquete seleccionado, conoce otras ofertas hechas para ti.' in r:
    return {'STATUS': True, 'OPERATOR': 'TIGO', 'PN':p, 'DETAILS': {'TYPE': 'POSPAGO'}}
  else:
    return {'STATUS': True, 'OPERATOR': 'TIGO', 'PN':p, 'DETAILS': {'TYPE': 'PREPAGO'}}

def claro_checker(p):

  MAIN_URL = 'https://portalpagos.claro.com.co/phrame.php'

  headers = {
    'Cookie':'', 
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.216 Safari/537.36'
  }

  payload = f'action=metodo_ajax&metodo=clienteAjax&clase=ajaxclaro&metodo_ejec=consultarPaquetesWS&NumeroCelular={p}&empresa=claro&htmlpaq=1&busca_linea=2&TIPO_COMPRA=2&OrigenPago='

  r = requests.post(url=MAIN_URL, headers=headers, data=payload).text


  if 'registrado, no existe.' in r:
    return False
  
  elif 'OK' in r and 'PREPAGO' in r:
    return {'STATUS': True, 'OPERATOR': 'CLARO', 'PN':p,'DETAILS':{'TYPE':'PREPAGO'}}
  else:
    return {'STATUS': True, 'OPERATOR': 'CLARO', 'PN':p,'DETAILS':{'TYPE':'POSPAGO'}}

