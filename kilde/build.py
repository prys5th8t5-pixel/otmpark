import base64,re,os
here=os.path.dirname(os.path.abspath(__file__))
s=open(os.path.join(here,'src.html'),encoding='utf-8').read()
for n in ['hero','julemarked','skilt','vinter','kamera','gjerde']:
    b=base64.b64encode(open(os.path.join(here,'img',f'{n}.jpg'),'rb').read()).decode()
    s=s.replace('{{%s}}'%n,'data:image/jpeg;base64,'+b)
assert '{{' not in s
os.makedirs(os.path.join(here,'site'),exist_ok=True)
open(os.path.join(here,'site','index.html'),'w',encoding='utf-8').write(s); print(len(s))
