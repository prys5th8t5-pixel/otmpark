import base64,os
here=os.path.dirname(os.path.abspath(__file__))
pv_css=open(os.path.join(here,'personvern.css'),encoding='utf-8').read()
pv_body=open(os.path.join(here,'personvern_body.html'),encoding='utf-8').read()
def pv(s): return s.replace('{{PV_CSS}}',pv_css).replace('{{PV_BODY}}',pv_body)
s=pv(open(os.path.join(here,'src.html'),encoding='utf-8').read())
for n in ['hero','julemarked','skilt','vinter','kamera','gjerde']:
    b=base64.b64encode(open(os.path.join(here,'img',f'{n}.jpg'),'rb').read()).decode()
    s=s.replace('{{%s}}'%n,'data:image/jpeg;base64,'+b)
assert '{{' not in s
os.makedirs(os.path.join(here,'site'),exist_ok=True)
open(os.path.join(here,'site','index.html'),'w',encoding='utf-8').write(s); print('index',len(s))
p=pv(open(os.path.join(here,'personvern_page.html'),encoding='utf-8').read())
assert '{{' not in p
open(os.path.join(here,'site','personvern.html'),'w',encoding='utf-8').write(p); print('personvern',len(p))
