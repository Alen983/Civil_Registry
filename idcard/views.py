from django.shortcuts import render
import MySQLdb
# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
import datetime
from datetime import datetime
from datetime import date
from datetime import datetime
import urllib.request
import webbrowser

from django.core.files.storage import FileSystemStorage
con=MySQLdb.connect("localhost","root","","civil")
c=con.cursor()

def cusreg(request):
    msg = ""
    d=str(date.today())
    print(d)
    cusid=0
    if  request.POST:
        print("haii")
        na=request.POST.get("n1")
        dob=request.POST.get("n2")       
        gen=request.POST.get("n3")
        addr=request.POST.get("n4")
        email=request.POST.get("n5")
        phno=request.POST.get("n6")
        aadhar=request.POST.get("n7")
       
        uname=request.POST.get("n8")
        pas=request.POST.get("n9")
        
        
        m="insert into cusreg(name,addr,gender,phno,aadhar,dob,email,username) values('"+str(na)+"','"+str(addr)+"','"+str(gen)+"','"+str(phno)+"','"+str(aadhar)+"','"+str(dob)+"','"+str(email)+"','"+str(uname)+"')"
        c.execute(m)
        ty="customer"
        m="insert into login(username,password,type) values('"+str(uname)+"','"+str(pas)+"','"+str(ty)+"')"
        c.execute(m)
        print(m) 
        mm="select cid from cusreg where name='"+str(na)+"' and email='"+str(email)+"'"
        c.execute(mm)
        data12=c.fetchone()
        cusid=data12[0]
        con.commit()
        msg="Registration Success"
    else:
        pass
        # return HttpResponseRedirect("/login/")
    return render(request,'CustomerRegistration.html',{'d':d,'cusid':cusid,'msg':msg})
    
def home(request):
    return render(request,'Home.html')
def customerhome(request):
    return render(request,'CustomerHome.html')
def authorityhome(request):
    return render(request,'RtoHome.html')
def Rtohome(request):
    return render(request,'RtoHome.html')
def passporthome(request):
    return render(request,'passporthome.html')
def rtohomeorg(request):
    return render(request,'rtohomeorg.html')
def Rpohome(request):
    return render(request,'RpoHome.html')
def adminhome(request):
    return render(request,'AdminHome.html')
def contact(request):
    return render(request,'contact.html')
def about(request):
    return render(request,'About.html')
def applications(request):
    return render(request,'applications.html')
def adminviewapplications(request):
    return render(request,'AdminViewApplications.html')
def marriageregistration(request):
    d=str(date.today())
    if 'madd' in request.POST:
        cid=request.session["cid"]
        dob=request.POST.get("n1")
        addr=request.POST.get("n2")
        gen=request.POST.get("n3")
        aadhar=request.POST.get("n4")
        phno=request.POST.get("n5")
        pas=request.POST.get("n6")
        sta="applied"
        m="insert into marriageregistration(dom,pom,localarea,village,taluk,dist,mstatus,uid) values('"+str(dob)+"','"+str(addr)+"','"+str(gen)+"','"+str(aadhar)+"','"+str(phno)+"','"+str(pas)+"','"+str(sta)+"','"+str(cid)+"')"
        c.execute(m)
        con.commit() 
       
        cid=request.session["cid"]
        bid=request.POST.get("id")
        gid=request.POST.get("id2")
        bname=request.POST.get("name1")
        gname=request.POST.get("name2")
        bpic=request.POST.get("p1")
        gpic=request.POST.get("p2")
        bnat=request.POST.get("nat1")
        gnat=request.POST.get("nat2")
        bdob=request.POST.get("dob1")
        gdob=request.POST.get("dob2")
        boccu=request.POST.get("occu1")
        goccu=request.POST.get("occu2")
        baddr=request.POST.get("addr1")
        gaddr=request.POST.get("addr2")
        bpaddr=request.POST.get("paddr1")
        gpaddr=request.POST.get("paddr2")
        bsig=request.POST.get("sig")
        gsig=request.POST.get("sig1")
        bfname=request.POST.get("fname")
        gfname=request.POST.get("fname1")
        bfsig=request.POST.get("fsig")
        gfsig=request.POST.get("fsig1")
        bmname=request.POST.get("mname")
        gmname=request.POST.get("mname1")
        bmsig=request.POST.get("msig")
        gmsig=request.POST.get("msig1")
        wid=request.POST.get("reg")
        wid1=request.POST.get("reg1")
        wname=request.POST.get("wname")
        wname1=request.POST.get("wname1")
        waddr=request.POST.get("waddr")
        waddr1=request.POST.get("waddr1")
        wfile=request.POST.get("wfile")
        wfile1=request.POST.get("wfile1")
        sta="applied"
        m="insert into bride(name,pic,nationality,dob,occu,peraddr,preaddr,sig,fname,fsig,mname,msig,uid) values('"+str(bname)+"','"+str(bpic)+"','"+str(bnat)+"','"+str(bdob)+"','"+str(boccu)+"','"+str(baddr)+"','"+str(bpaddr)+"','"+str(bsig)+"','"+str(bfname)+"','"+str(bfsig)+"','"+str(bmname)+"','"+str(bmsig)+"','"+str(cid)+"')"
        c.execute(m)
        me="insert into groom(name,pic,nationality,dob,occu,peraddr,preaddr,sig,fname,fsig,mname,msig,uid) values('"+str(gname)+"','"+str(gpic)+"','"+str(gnat)+"','"+str(gdob)+"','"+str(goccu)+"','"+str(gaddr)+"','"+str(gpaddr)+"','"+str(gsig)+"','"+str(gfname)+"','"+str(gfsig)+"','"+str(gmname)+"','"+str(gmsig)+"','"+str(cid)+"')"
        c.execute(me)
        me="insert into witness(mcertid,wname,waddr,wsign) values('"+str(wid)+"','"+str(wname)+"','"+str(waddr)+"','"+str(wfile)+"')"
        c.execute(me)
        me="insert into witness(mcertid,wname,waddr,wsign) values('"+str(wid1)+"','"+str(wname1)+"','"+str(waddr1)+"','"+str(wfile1)+"')"
        c.execute(me)
        con.commit()  
        return HttpResponseRedirect("/marriageregistration/")   

    return render(request,'MarriageCertificate.html',{'d':d})

def BirthCertificateregistration(request):
    d=str(date.today())
    msg=""
    msg=request.GET.get("msg")
    if 'birthsubmit' in request.POST:
        dob=request.POST.get("n1")
        tob=request.POST.get("n2")
        dis=request.POST.get("n3")
        gen=request.POST.get("g1")
        cname=request.POST.get("cname")
        mname=request.POST.get("mname")
        fname=request.POST.get("fname")
        paddr=request.POST.get("paddr")
        paddrb=request.POST.get("paddrb")
        pob=request.POST.get("pob")
        hosp=request.POST.get("hosp")
        deli=request.POST.get("deli")
        bw=request.POST.get("bw")
        dur=request.POST.get("dur")
        rep=request.POST.get("rep")
        status="applied"
        cusid=request.session["cid"]
        my_date =datetime.strptime(dob,"%Y-%m-%d")
        yr=my_date.year
        my_datedeath =datetime.strptime(rep,"%Y-%m-%d")
        dyr=my_datedeath.year
        #dyr=pob.year()
        if yr>dyr:
            msg="please check the date....date of birth should be less than reporting date"
            return render(request,'BirthCertificateReg.html',{'d':d})


        else:
            me="insert into birthreg(dob,tob,dis,gen,cname,mname,fname,paddr,paddrb,pob,hosp,deli,weight,dur,rdate,status,uid) values('"+str(dob)+"','"+str(tob)+"','"+str(dis)+"','"+str(gen)+"','"+str(cname)+"','"+str(mname)+"','"+str(fname)+"','"+str(paddr)+"','"+str(paddrb)+"','"+str(pob)+"','"+str(hosp)+"','"+str(deli)+"','"+str(bw)+"','"+str(dur)+"','"+str(rep)+"','"+str(status)+"','"+str(cusid)+"')"
            c.execute(me)
            con.commit()
            msg="Registration Success"
        return HttpResponseRedirect("/BirthCertificateregistration?msg="+msg)   

    return render(request,'BirthCertificateReg.html',{'d':d,'msg':msg})
def deathregistration(request):
    d=str(date.today())
    if 'submitdeath' in request.POST:
        dob=request.POST.get("n1")
        tob=request.POST.get("n2")
        dis=request.POST.get("n3")
        gen=request.POST.get("g1")
        cname=request.POST.get("fname")
        mname=request.POST.get("mname")
        
        faddr=request.POST.get("faddr")
        paddr=request.POST.get("paddr")
        paddrb=request.POST.get("paddrb")
        pob=request.POST.get("pob")
        hosp=request.POST.get("pl")
        deli=request.POST.get("house")
        bw=request.POST.get("iname")
        inf=request.POST.get("iaddr")
        status="applied"
        cusid=request.session["cid"]
        my_date =datetime.strptime(dob,"%Y-%m-%d")
        yr=my_date.year
        my_datedeath =datetime.strptime(pob,"%Y-%m-%d")
        dyr=my_datedeath.year
        print(yr,dyr)
        #dyr=pob.year()
        if yr==dyr:
            me="insert into deathcertificatelegal(dod,named,pad,gen,nof,nom,addeath,praddpa,praddtbirth,dobdesd,pod,haddrs,infoname,inadd,status,uid) values('"+str(dob)+"','"+str(tob)+"','"+str(dis)+"','"+str(gen)+"','"+str(cname)+"','"+str(mname)+"','"+str(faddr)+"','"+str(paddr)+"','"+str(paddrb)+"','"+str(pob)+"','"+str(hosp)+"','"+str(deli)+"','"+str(bw)+"','"+str(inf)+"','"+str(status)+"','"+str(cusid)+"')"
            c.execute(me)
            print(me)
            con.commit()
        elif yr>dyr:
            me="insert into deathcertificatelegal(dod,named,pad,gen,nof,nom,addeath,praddpa,praddtbirth,dobdesd,pod,haddrs,infoname,inadd,status,uid) values('"+str(dob)+"','"+str(tob)+"','"+str(dis)+"','"+str(gen)+"','"+str(cname)+"','"+str(mname)+"','"+str(faddr)+"','"+str(paddr)+"','"+str(paddrb)+"','"+str(pob)+"','"+str(hosp)+"','"+str(deli)+"','"+str(bw)+"','"+str(inf)+"','"+str(status)+"','"+str(cusid)+"')"
            c.execute(me)
            print(me)
            con.commit()
        elif dyr>yr:
            msg="date of birth should be less than date of death"
            return render(request,'DeathCertificate.html',{'d':d,'msg':msg})


    return render(request,'DeathCertificate.html',{'d':d})
def login(request):
    if 'login' in request.POST:
        rnum=request.POST.get("n1")
        pswd=request.POST.get("n2")       
        
        v="select type from login where username='"+str(rnum)+"' and password='"+str(pswd)+"'"
        c.execute(v)
        print(v)
        da=c.fetchone()
        print(v)
        
        request.session["un"]=rnum
        if not bool(da):
            msg="invalid username or password"
            return render(request,'login.html',{"msg":msg})

        if da[0]=="admin":
                 return HttpResponseRedirect("/adminhome/")

        if da[0]=="customer":
                c.execute("select name,cid from cusreg where username='"+str(rnum)+"'")
                cc=c.fetchall()
                request.session["name"]=cc[0][0]
                request.session["cid"]=cc[0][1]
                return HttpResponseRedirect("/customerhome")
        if da[0]=="Registration":
                c.execute("select head,aid from  `authorityreg` where username='"+str(rnum)+"'")
                cc=c.fetchall()
                request.session["name"]=cc[0][0]
                request.session["cid"]=cc[0][1]
                request.session["authoritytype"]="Registration"
                return HttpResponseRedirect("/Rtohome")
        if da[0]=="ElectionCommision":
                c.execute("select head,aid from  `authorityreg` where username='"+str(rnum)+"'")
                cc=c.fetchall()
                request.session["name"]=cc[0][0]
                request.session["cid"]=cc[0][1]
                request.session["authoritytype"]="ElectionCommision"
                return HttpResponseRedirect("/Rpohome")
        if da[0]=="RTO":
                c.execute("select head,aid from  `authorityreg` where username='"+str(rnum)+"'")
                cc=c.fetchall()

                print("rtooooooooooo")
                request.session["name"]=cc[0][0]
                request.session["cid"]=cc[0][1]
                request.session["authoritytype"]="RTO"
                return HttpResponseRedirect("/rtohomeorg") 
        if da[0]=="passport":
                c.execute("select head,aid from  `authorityreg` where username='"+str(rnum)+"'")
                cc=c.fetchall()

                print("rtooooooooooo")
                request.session["name"]=cc[0][0]
                request.session["cid"]=cc[0][1]
                request.session["authoritytype"]="passport"
                return HttpResponseRedirect("/passporthome")     
    return render(request,'login.html')

def authorityreg(request):
    mk="select * from district"
    c.execute(mk)
    da=c.fetchall()
    mk1="select * from authority"
    c.execute(mk1)
    dat=c.fetchall()
    if 'submit1' in request.POST:
        na=request.POST.get("district")
        dob=request.POST.get("n1")
        addr=request.POST.get("n2")
        gen=request.POST.get("n3")
        aadhar=request.POST.get("category")
        phno=request.POST.get("n5")
        pas=request.POST.get("n6")
        m="insert into authorityreg(district,head,addr,phno,category,username,password) values('"+str(na)+"','"+str(dob)+"','"+str(addr)+"','"+str(gen)+"','"+str(aadhar)+"','"+str(phno)+"','"+str(pas)+"')"
        c.execute(m)
        ty=""
        me="insert into login(username,password,type) values('"+str(phno)+"','"+str(pas)+"','"+str(aadhar)+"')"
        c.execute(me)
        print(m) 
        con.commit()
    return render(request,'AddAuthority.html',{'data':da,'auth':dat})
def feedback(request):
    mk="select * from district"
    c.execute(mk)
    da=c.fetchall()
    mk1="select * from authority"
    c.execute(mk1)
    dat=c.fetchall()
    if 'submit12' in request.POST:
        cid=request.session["cid"]
        na=request.POST.get("district")
        
        aadhar=request.POST.get("category")
        phno=request.POST.get("n5")
        date1=date.today()
        m="insert into feedback(district,authority,fb,date,uid) values('"+str(na)+"','"+str(aadhar)+"','"+str(phno)+"','"+str(date1)+"','"+str(cid)+"')"
        c.execute(m)
       
        con.commit()
    return render(request,'CustomerFeedback.html',{'data':da,'auth':dat})

def viewmarriageregistration(request):

  #  uid=request.session["cid"]
    s="applied"
    gg="select marriageregistration.*,cusreg.name,cusreg.phno,cusreg.email from marriageregistration inner join cusreg on marriageregistration.uid=cusreg.cid where marriageregistration.mstatus='"+str(s)+"'"
    c.execute(gg)
    da=c.fetchall()
    me="select marriageregistration.* ,cusreg.name,cusreg.email,cusreg.phno from marriageregistration inner join cusreg on cusreg.cid=marriageregistration.uid"
    c.execute(me)
    dat=c.fetchall()
    return render(request,'AdminViewmarriageRequests.html',{'data':da,'data1':dat})

def viewvotersidregistration(request):
    
  #  uid=request.session["cid"]
    s="applied"
    gg="select * from votersid  where status='"+str(s)+"'"
    c.execute(gg)
    da=c.fetchall()
    s2="forwarded"
    gg1="select * from votersid  where status='"+str(s2)+"'"
    c.execute(gg1)
    dat=c.fetchall()
    return render(request,'AdminViewVotersidRequest.html',{'data':da,'data1':dat})
def viewbirthregistration(request):

  #  uid=request.session["cid"]
    s="applied"
    gg="select * from birthreg  where status='"+str(s)+"'"
    c.execute(gg)
    da=c.fetchall()
    me="select marriageregistration.* ,cusreg.name,cusreg.email,cusreg.phno from marriageregistration inner join cusreg on cusreg.cid=marriageregistration.uid"
    c.execute(me)
    dat=c.fetchall()

    return render(request,'AdminViewBirthCertificate.html',{'data':da,'data1':dat})

# def viewdeathregistration(request):

#   #  uid=request.session["cid"]
#     s="applied"
#     gg="select deathcertificatelegal.*,cusreg.name,cusreg.phno,cusreg.email,cusreg.cid from deathcertificatelegal inner join cusreg on deathcertificatelegal.uid=cusreg.cid where deathcertificatelegal.status='"+str(s)+"'"
#     c.execute(gg)
#     da=c.fetchall()

#     return render(request,'AdminViewBirthCertificate.html',{'data':da})
def forwardmarriage(request):
    mid=request.GET.get("id")
    cid=request.GET.get("cusid")
    dept="Registration"
    dis="Ernakulam"
    f=date.today()
    cer="Marriage"
    st="forwarded"
    mn="insert into forward(district,authority,fdate,certid,certificate,status) values('"+str(dis)+"','"+str(dept)+"','"+str(f)+"','"+str(mid)+"','"+str(cer)+"','"+str(st)+"')"
    c.execute(mn)
    g="forwarded"
    lm="update marriageregistration set mstatus='"+str(g)+"' where mid='"+str(mid)+"'"
    c.execute(lm)
    con.commit()
    return render(request,'AdminViewapplications.html')
def forwardbirth(request):
    mid=request.GET.get("id")
    print(mid)
    cid=request.GET.get("cusid")
    dept="Registration"
    dis="Ernakulam"
    f=date.today()
    cer="Birth"
    st="forwarded"
    mn="insert into forward(district,authority,fdate,certid,certificate,status) values('"+str(dis)+"','"+str(dept)+"','"+str(f)+"','"+str(mid)+"','"+str(cer)+"','"+str(st)+"')"
    c.execute(mn)
    g="forwarded"
    lm="update birthreg set status='"+str(g)+"' where brid='"+str(mid)+"'"
    c.execute(lm)
    con.commit()
    return render(request,'AdminViewapplications.html')

def forwardvotersid(request):
    mid=request.GET.get("id")
    print(mid)
    cid=request.GET.get("cusid")
    dept="ElectionCommision"
    dis="Ernakulam"
    f=date.today()
    cer="Votersid"
    st="forwarded"
    mn="insert into forward(district,authority,fdate,certid,certificate,status) values('"+str(dis)+"','"+str(dept)+"','"+str(f)+"','"+str(mid)+"','"+str(cer)+"','"+str(st)+"')"
    c.execute(mn)
    g="forwarded"
    lm="update votersid set status='"+str(g)+"' where vid='"+str(mid)+"'"
    c.execute(lm)
    con.commit()
    return render(request,'AdminViewapplications.html')
def viewfeedback(request):
    mk="select feedback.*,cusreg.name from feedback inner join cusreg where cusreg.cid=feedback.uid"
    c.execute(mk)
    dat=c.fetchall()   
    print(dat)
    return render(request,'AdminViewFeedback.html',{'data':dat})

def forwarddeath(request):
    id=request.GET.get("id")
    cid=request.GET.get("cusid")
    dept="Registration"
    dis="Ernakulam"
    f=date.today()
    cer="Death"
    st="forwarded"
    mn="insert into forward(district,authority,fdate,certid,certificate,status) values('"+str(dis)+"','"+str(dept)+"','"+str(f)+"','"+str(id)+"','"+str(cer)+"','"+str(st)+"')"
    c.execute(mn)
    con.commit()
    g="forwarded"
    lm="update deathcertificatelegal set status='"+str(g)+"' where did='"+str(id)+"'"
    c.execute(lm)
    con.commit()
    return render(request,'AdminViewapplications.html')


def viewauthorityapplicationslink(request):
    return render(request,'AuthorityViewapplicationLink.html')

def viewauthorityapplication(request):
    a=request.session["authoritytype"]
    st="forwarded"
    cer="Marriage"
    mk="select forward.*,marriageregistration.*,cusreg.name,cusreg.phno,cusreg.email from forward inner join marriageregistration on forward.certid=marriageregistration.mid  join cusreg on cusreg.cid=marriageregistration.uid where forward.authority='"+str(a)+"' and forward.certificate='"+str(cer)+"' and marriageregistration.mstatus='"+str(st)+"'"
    c.execute(mk)
    dat=c.fetchall()  
    id=dat[0][15] 
    print(dat)
    
    
    
    return render(request,'AuthorityViewApplications.html',{'data':dat})
def issuemarriage(request):
   # id=request.GET.get("id")
    if 'submitamount' in request.POST:

        id=request.POST.get("n3")
        certype=request.POST.get("n4")
        myfile = request.FILES['n1']
        fs = FileSystemStorage()        
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)

        amt=request.POST.get("n2")

        
        # n="select uid from marriageregistration where mid='"+str(id)+"'"
        # c.execute(n)
        # print(n)
        # dw=c.fetchone()
        # print(dw)
        # cid=dw[0]
        st="not paid"
        mk="insert into certificatereg(certificate,uploadcertificate,cid,amount,status) values('"+str(certype)+"','"+str(uploaded_file_url)+"','"+str(id)+"','"+str(amt)+"','"+str(st)+"')"
        c.execute(mk)
        con.commit()
        dat=c.fetchall()   
        return render(request,'UploadCertificateauthority.html',{'data':dat})
    return render(request,'UploadCertificateauthority.html')


def issuevotersid(request):
       # id=request.GET.get("id")
    if 'submitamount' in request.POST:

        id=request.POST.get("n3")
        myfile = request.FILES['n1']
        fs = FileSystemStorage()        
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)

        amt=request.POST.get("n2")

        cer="Votersid"
        n="select vid from votersid where uid='"+str(id)+"'"
        c.execute(n)
        print(n)
        dw=c.fetchone()
        print(dw)
        cid=dw[0]
        st="not paid"
        mk="insert into certificatereg(certificate,uploadcertificate,cid,amount,status) values('"+str(cer)+"','"+str(uploaded_file_url)+"','"+str(id)+"','"+str(amt)+"','"+str(st)+"')"
        c.execute(mk)
        con.commit()
        dat=c.fetchall()   
        return render(request,'UploadCertificateauthority.html',{'data':dat})
    return render(request,'UploadCertificateauthority.html')


def customerviewcertificate(request):
    id1=request.session["cid"]
    s="not paid"
    mk="select * from certificatereg where cid='"+str(id1)+"' and status='"+str(s)+"'"
    c.execute(mk)
    dat=c.fetchall()  
    return render(request,'CustomerViewCertificate.html',{'data':dat})


def customerdownloadcertificate(request):
    id1=request.session["cid"]
    s="paid"
    mk="select * from certificatereg where cid='"+str(id1)+"' and status='"+str(s)+"'"
    c.execute(mk)
    dat=c.fetchall()  
    return render(request,'CustomerDownloadCertificate.html',{'data':dat})


def payment1(request):
    id=request.GET.get("id")
    cid=request.session["cid"]
    amt=request.GET.get("amt")
    certificate=request.GET.get("amt")
    cardno=request.POST.get("cardno")
    request.session["cardno"]=cardno
    request.session["payid"]=id
    print(amt)
    paid="paid"
    #s="update checkout set paid='"+str(paid)+"' where id='"+str(uid)+"'"
    #print(s)
    #c.execute(s)
    #con.commit()
    if request.POST:
        card=request.POST.get("test")
        cardno=request.POST.get("cardno")
        print(cardno)
        certi=request.POST.get("ceti")
        request.session["cardno"]=cardno
        request.session["amt"]=amt
        pinno=request.POST.get("pinno")

      #  ll="insert into payment(certid,certificate,cusid,amount) values('"+str(id)+"','"+str(certi)+"','"+str(cid)+"','"+str(amt)+"'"
       # c.execute(ll)
        #con.commit()
        return HttpResponseRedirect("/payment2")
    return render(request,"payment1.html")

def payment2(request):
    #cno=request.session["card_no"]
    #amount=request.session["pay"]
    cardno=request.session["cardno"]
    amount=request.session["amt"]
    payid=request.session["payid"]
    if request.POST:
        #name=request.POST.get("t1")
        #request.session["m"]=name
        #address=request.POST.get("t2")
        #email=request.POST.get("t3")
        #phno=request.POST.get("t4")
        s="paid"
        n="update certificatereg set status= '"+str(s)+"' where certiid='"+str(payid)+"'"
        print(n)
        c.execute(n)
        con.commit()
        return HttpResponseRedirect("/payment3")
    return render(request,"payment2.html",{'amount':amount,'cardno':cardno})

def payment3(request):
    return render(request,"payment3.html")

def payment4(request):
    return render(request,"payment4.html")

def payment5(request):
    #cno=request.session["card_no"]
    #today = date.today()
    #n="select * from delivery where card='"+str(cno)+"'"
    #c.execute(n)
    #data=c.fetchall()
#    return render(request,"payment5.html",{"cno":cno,"data":data,"today":today})
    return render(request,"payment5.html")
def backtohome(request):
    if 'goback' in request.POST:
        return render(request,"CustomerHome.html")

    return render(request,"payment5.html")

def viewmarriagecertificate(request):
    em=request.GET.get("em")
    mid=request.GET.get("mid")
    bb="select cid from cusreg where email='"+str(em)+"'"
    print(bb)
    c.execute(bb)
    da=c.fetchone()
    uid=da[0]
    mi="select * from marriageregistration where mid='"+str(mid)+"'"
    c.execute(mi)
    dt=c.fetchall()
    dom=dt[0][1]
    pom=dt[0][2]
    mm="select bride.name,groom.name from bride inner join groom on bride.uid=groom.uid where bride.rid='"+str(mid)+"' and groom.rid='"+str(mid)+"'"
    c.execute(mm)
    des=c.fetchall()
    print(mm)
    print(des)

    return render(request,"AuthorityUploadMarriageCertificate.html",{'data':des,'dom':dom,'pom':pom})

def viewvotersidcertificate(request):
    em=request.GET.get("em")
    fwid=request.GET.get("fwid")
    
    mi="select * from votersid where applicant='"+str(em)+"'"
    c.execute(mi)
    dt=c.fetchall()
    dom=dt[0][1]
    pom=dt[0][2]
    cer="Votersid"
    mm="select votersid.pic,votersid.applicant,votersid.fname,votersid.dob,votersid.hname,votersid.district from votersid inner join forward on forward.certid=votersid.vid where   forward.certificate='"+str(cer)+"' and forward.fwid='"+str(fwid)+"'"
    c.execute(mm)
    des=c.fetchall()
    print(des)
    return render(request,"RtoUploadVotersid.html",{'data':des})

def viewauthoritydeathapplication(request):
    a=request.session["authoritytype"]
    cer="Death"
    st="forwarded"
    mk="select forward.*,deathcertificatelegal.* from forward inner join deathcertificatelegal on forward.certid=deathcertificatelegal.did where forward.authority='"+str(a)+"' and forward.certificate='"+str(cer)+"' and deathcertificatelegal.status='"+str(st)+"'"
    c.execute(mk)
    dat=c.fetchall()
    print(dat)
    id=dat[0][22] 
    brid=dat[0][7]
    print(brid)
    hn="select * from cusreg where cid='"+str(id)+"'"
    c.execute(hn)

    da=c.fetchall()
    un=da[0][1]
    phno=da[0][4]
    em=da[0][7]
    return render(request,'AuthorityViewDeathRequests.html',{'data':dat,'uname':un,'ph':phno,'email':em})

def authorityuploaddeathapplication(request):
    em=request.GET.get("em")
    brid=request.GET.get("brid")
    # bb="select cid from cusreg where email='"+str(em)+"'"
    # print(bb)
    # c.execute(bb)
    # da=c.fetchone()
    # uid=da[0]
    # print(uid)
    cer="Death"
    mi="select * from deathcertificatelegal where uid='"+str(em)+"' and did='"+str(brid)+"'"
    c.execute(mi)
    dt=c.fetchone()
    dname=dt[2]
    ddate=dt[1]
    dplace=dt[11]
   

    return render(request,"AuthorityUploadDeathCertificate.html",{'data':dname,'dom':ddate,'pom':dplace})
def viewbirthcertificate(request):
    em=request.GET.get("em")
    brid=request.GET.get("brid")
    
    bb="select cid from cusreg where email='"+str(em)+"'"
    print(bb)
    c.execute(bb)
    da=c.fetchone()
    uid=da[0]
    mi="select * from birthreg where brid='"+str(brid)+"'"
    c.execute(mi)
    dt=c.fetchall()
    dom=dt[0][1]
    pom=dt[0][2]
    

    return render(request,"AuthorityUploadBirthCertificate.html",{'data':dt})
def viewdeathregistration(request):

  #  uid=request.session["cid"]
    s="applied"
    gg="select * from deathcertificatelegal  where status='"+str(s)+"'"
    c.execute(gg)
    da=c.fetchall()
    s1="forwarded"
    gg1="select * from deathcertificatelegal  where status='"+str(s1)+"'"
    c.execute(gg1)
    data1=c.fetchall()
    return render(request,'AdminViewDeathCertificate.html',{'data':da,'data1':data1})

def voteridreg(request):
    d=str(date.today())
    if 'votersid' in request.POST:
        n1=request.POST.get("n1")
        n2=request.POST.get("n2")
        n3=request.POST.get("n3")
        n4=request.POST.get("n4")
        n5=request.POST.get("n5")
        n6=request.POST.get("n6")
        n7=request.POST.get("n7")
        n8=request.POST.get("n8")
        n9=request.POST.get("n9")
        n10=request.POST.get("n10")
        n11=request.POST.get("n11")
        n12=request.POST.get("n12")
        n13=request.POST.get("n13")
        #n14=request.POST.get("n14")
        uploaded_file_url=""
       
        myfile=request.FILES.get("n14")
        fs=FileSystemStorage()
        filename=fs.save(myfile.name , myfile)
        uploaded_file_url = fs.url(filename)

        n15=request.POST.get("n15")
        n16=request.POST.get("n16")
        status="applied"
        cusid=request.session["cid"]
        me="insert into votersid(district,applicant,fname,age,dob,gender,hname,street,town,po,pincode,email,phno,pic,ageproof,addrproof,status,uid) values('"+str(n1)+"','"+str(n2)+"','"+str(n3)+"','"+str(n4)+"','"+str(n5)+"','"+str(n6)+"','"+str(n7)+"','"+str(n8)+"','"+str(n9)+"','"+str(n10)+"','"+str(n11)+"','"+str(n12)+"','"+str(n13)+"','"+str(uploaded_file_url)+"','"+str(n15)+"','"+str(n16)+"','"+str(status)+"','"+str(cusid)+"')"
        c.execute(me)
        print(me)
        con.commit()
        return HttpResponseRedirect("/voteridreg/")   

    return render(request,'Votersid.html',{'d':d})

def viewauthoritybirthapplication(request):
    a=request.session["authoritytype"]
    cer="Birth"
    st="forwarded"
    mk="select forward.*,birthreg.*,cusreg.name,cusreg.phno,cusreg.email from forward inner join birthreg on forward.certid=birthreg.brid  join cusreg on cusreg.cid=birthreg.uid where forward.authority='"+str(a)+"' and forward.certificate='"+str(cer)+"' and birthreg.status='"+str(st)+"'"
    c.execute(mk)
    dat=c.fetchall()
    print(dat)
    
    return render(request,'AuthorityRtoViewBirthApllication.html',{'data':dat})

def rtoviewvotersidapplication(request):
    a=request.session["authoritytype"]
    mk="select forward.*,votersid.* from forward inner join votersid on forward.certid=votersid.vid where forward.authority='"+str(a)+"'"
    c.execute(mk)
    dat=c.fetchall()  
    id=dat[0][25] 
    hn="select * from cusreg where cid='"+str(id)+"'"
    c.execute(hn)

    da=c.fetchall()
    un=da[0][1]
    phno=da[0][4]
    em=da[0][7]
    return render(request,'RtoViewVotersidApplications.html',{'data':dat,'uname':un,'ph':phno,'email':em})
def issuebirth(request):
   # id=request.GET.get("id")
    if 'submitamount' in request.POST:

        id=request.POST.get("n3")
        myfile = request.FILES['n1']
        fs = FileSystemStorage()        
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)

        amt=request.POST.get("n2")

        cer="marriage"
        n="select uid from birthreg where brid='"+str(id)+"'"
        c.execute(n)
        print(n)
        dw=c.fetchone()
        print(dw)
        cid=dw[0]
        s="not paid"
        mk="insert into certificatereg(certificate,uploadcertificate,cid,amount,status) values('"+str(cer)+"','"+str(uploaded_file_url)+"','"+str(cid)+"','"+str(amt)+"','"+str(s)+"')"
        c.execute(mk)
        con.commit()
        dat=c.fetchall()   
        return render(request,'UploadCertificateauthority.html',{'data':dat})
    return render(request,'UploadCertificateauthority.html')


def rationcardregistration(request):
    d=str(date.today())
    if 'rationsubmit' in request.POST:
        dob=request.POST.get("n1")
        tob=request.POST.get("n2")
        gen=request.POST.get("f1")
        cname=request.POST.get("n4")
        mname=request.POST.get("n5")
        fname=request.POST.get("n6")
        paddr=request.POST.get("n7")
        paddrb=request.POST.get("n8")
        pob=request.POST.get("n9")
        hosp=request.POST.get("n10")
        deli=request.POST.get("n11")
        bw=request.POST.get("n12")
        dur=request.POST.get("n13")
        
        status="applied"
        cusid=request.session["cid"]
        me="insert into rationreg values('"+str(dob)+"','"+str(tob)+"','"+str(gen)+"','"+str(cname)+"','"+str(mname)+"','"+str(fname)+"','"+str(paddr)+"','"+str(paddrb)+"','"+str(pob)+"','"+str(hosp)+"','"+str(deli)+"','"+str(bw)+"','"+str(dur)+"','"+str(status)+"','"+str(cusid)+"')"
        c.execute(me)
        con.commit()
        return HttpResponseRedirect("/rationcardregistration/")   
    return render(request,'RationShopApply.html',{'d':d})

def adminviewauthority(request):
    
    me="select *from authorityreg "
    c.execute(me)
    
    dat=c.fetchall()
    return render(request,'adminviewauthority.html',{'data':dat})

def viewmarragedetails(request):    
    me="select marriageregistration.* ,cusreg.name,cusreg.email,cusreg.phno from marriageregistration inner join cusreg on cusreg.cid=marriageregistration.uid"
    c.execute(me)
    dat=c.fetchall()
    return render(request,'adminviewmarrageregdetails.html',{'data':dat})
def rejectvotersid(request):  
    fwid=request.GET.get("fwid")  
    me="delete from forward where fwid='"+str(fwid)+"'"
    c.execute(me)
    con.commit()
    return HttpResponseRedirect("/rtoviewvotersidapplication/") 
def rejectlisence(request):  
    fwid=request.GET.get("id")  
    me="delete from licencereg where lid='"+str(fwid)+"'"
    c.execute(me)
    con.commit()
    return HttpResponseRedirect("/viewlicenceregistration/")   
def rejectpasport(request):  
    fwid=request.GET.get("id")  
    me="delete from passport where lid='"+str(fwid)+"'"
    c.execute(me)
    con.commit()
    return HttpResponseRedirect("/adminviewpassport/")
def adminrejectcustomer(request):  
    fwid=request.GET.get("id")  
    me="delete from birthreg where brid='"+str(fwid)+"'"
    c.execute(me)
    con.commit()
    return HttpResponseRedirect("/viewbirthregistration/")

def rejectdeathcertificate(request):  
    fwid=request.GET.get("brid")  
    me="delete from deathcertificatelegal where did='"+str(fwid)+"'"
    c.execute(me)
    print(me)
    con.commit()
    return HttpResponseRedirect("/viewauthoritydeathapplication/") 
def rejectmarriagecertificate(request):  
    fwid=request.GET.get("id")  
    me="delete from marriageregistration where mid='"+str(fwid)+"'"
    c.execute(me)
    me="delete from groom where rid='"+str(fwid)+"'"
    c.execute(me)
    me="delete from bride where rid='"+str(fwid)+"'"
    c.execute(me)
    con.commit()
    return HttpResponseRedirect("/viewmarriageregistration/")  

def adminrejectvotersid(request):  
    fwid=request.GET.get("id")  
    me="delete from votersid where vid='"+str(fwid)+"'"
    c.execute(me)
    con.commit()
    return HttpResponseRedirect("/viewvotersidregistration/")   
def adminaddreply(request): 
    fwid=request.GET.get("id")  
    if request.POST: 
        
        re=request.POST.get("n1")
        me="update feedback set reply='"+str(re)+"' where fid='"+str(fwid)+"'"
        c.execute(me)
        con.commit()
    return render(request,'adminaddreply.html',{'id':fwid})


def sendsms(ph,msg):
    
    sendToPhoneNumber= "+91"+ph
    userid = "2000022557"
    passwd = "54321@lcc"
    url = "http://enterprise.smsgupshup.com/GatewayAPI/rest?method=sendMessage&send_to=" + sendToPhoneNumber + "&msg=" + msg + "&userid=" + userid + "&password=" + passwd + "&v=1.1&msg_type=TEXT&auth_scheme=PLAIN"
    # contents = urllib.request.urlopen(url)
    webbrowser.open(url)



def forgot(request):
    alert=password=phno=""
    
    if 'forgot' in request.POST:
        email=request.POST.get("n1")
        phno=request.POST.get("n2")
        np=request.POST.get("n3")
        c.execute("select count(*) from cusreg where email='"+str(email) +"' and phno='"+str(phno)+"'")
        password=c.fetchone()
        print(password)
        pas1=password[0]
        # if password is None:
        #     c.execute("select password from authorityreg where phno='"+ phno +"'")
        #     password=c.fetchone()
            

        # if password is None:
        #     c.execute("select pswd from supplyco where email='"+ email +"' and phno='"+ phno +"'")
        #     password=c.fetchone()
        
        
        if pas1>0:
            c.execute("select username from cusreg where email='"+str(email)+"' and phno='"+str(phno) +"'")
            password=c.fetchone()
            
            print("hhhhhhhhhhhhhhhh")
            un=password[0]
           # c.execute("update cusreg set password='"+str(np)+"' where email='"+ str(email) +"' and phno='"+ str(phno) +"'")
            c.execute("update login set password='"+str(np)+"' where username='"+ str(un)+"'")
        else:
            alert="Invalid email and password combination"
            return HttpResponseRedirect("/forgot/")

        msg="Your Password is '"+str(np)+"'"
        sendsms(phno,msg)
    return render(request,'forgot.html',{"alert":alert})


def licencereg(request):
    d=str(date.today())
    if 'licencesubmit' in request.POST:
        dob=request.POST.get("n2")
        tob=request.POST.get("cname")
        dis=request.POST.get("n1")
        gen=request.POST.get("n3")
        cname=request.POST.get("n4")
        mname=request.POST.get("n5")
        fname=request.POST.get("n6")
        paddr=request.POST.get("g1")
        # paddrb=request.POST.get("mname")
        # pob=request.POST.get("fname")
        # hosp=request.POST.get("paddr")
        # deli=request.POST.get("p1")
        # bw=request.POST.get("sig")
        rep=request.POST.get("hosp")
        myfile = request.FILES.get("mname")
        fs = FileSystemStorage()        
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        myfile1 = request.FILES.get("fname")
        fs = FileSystemStorage()        
        filename1 = fs.save(myfile1.name, myfile1)
        uploaded_file_url1 = fs.url(filename1)
        myfile2 = request.FILES.get("paddr")
        fs = FileSystemStorage()        
        filename2 = fs.save(myfile2.name, myfile2)
        uploaded_file_url2 = fs.url(filename2)
        myfile3 = request.FILES.get("p1")
        fs = FileSystemStorage()        
        filename3 = fs.save(myfile3.name, myfile3)
        uploaded_file_url3 = fs.url(filename3)
        myfile4 = request.FILES.get("sig")
        fs = FileSystemStorage()        
        filename4 = fs.save(myfile4.name, myfile4)
        uploaded_file_url4 = fs.url(filename4)
        status="applied"
        cusid=request.session["cid"]
        my_date =datetime.strptime(dis,"%Y-%m-%d")
        yr=my_date.year
        my_datedeath =datetime.strptime(rep,"%Y-%m-%d")
        dyr=my_datedeath.year
        #dyr=pob.year()
        if yr>dyr:
            msg="please check the date....date of birth should be less than reporting date"
            return render(request,'LicenceCertificate.html',{'d':d,'msg':msg})
        else:
            me="insert into licencereg(licencenum,name,dob,district,taluk,email,phno,addr,idproof,addrproof,ageproof,pic,sig,appointment,cid,status) values('"+str(dob)+"','"+str(tob)+"','"+str(dis)+"','"+str(gen)+"','"+str(cname)+"','"+str(mname)+"','"+str(fname)+"','"+str(paddr)+"','"+str(uploaded_file_url)+"','"+str(uploaded_file_url1)+"','"+str(uploaded_file_url2)+"','"+str(uploaded_file_url3)+"','"+str(uploaded_file_url4)+"','"+str(rep)+"','"+str(cusid)+"','"+str(status)+"')"
            c.execute(me)
            con.commit()
            print(str(me))
            return HttpResponseRedirect("/licencereg/")   

    return render(request,'LicenceCertificate.html',{'d':d})

def viewlicenceregistration(request):
    
  #  uid=request.session["cid"]
    s="applied"
    gg="select * from licencereg  where status='"+str(s)+"'"
    c.execute(gg)
    da=c.fetchall()
    st="forwarded"
    
    gg="select * from licencereg  where status='"+str(st)+"'"
    c.execute(gg)
    dat=c.fetchall()

    return render(request,'adminviewlicenceapplication.html',{'data':da,'data1':dat})

def sendsms(ph,msg):
    
    sendToPhoneNumber= "+91"+ph
    userid = "2000022557"
    passwd = "54321@lcc"
    url = "http://enterprise.smsgupshup.com/GatewayAPI/rest?method=sendMessage&send_to=" + sendToPhoneNumber + "&msg=" + msg + "&userid=" + userid + "&password=" + passwd + "&v=1.1&msg_type=TEXT&auth_scheme=PLAIN"
    # contents = urllib.request.urlopen(url)
    webbrowser.open(url)

def forwardlicence(request):
    mid=request.GET.get("id")
    
    print(mid)
    cid=request.session["cid"]
    dept="Rto"
    dis="Ernakulam"
    f=date.today()
    cer="Licence"
    st="forwarded"
    mn="insert into forward(district,authority,fdate,certid,certificate,status) values('"+str(dis)+"','"+str(dept)+"','"+str(f)+"','"+str(mid)+"','"+str(cer)+"','"+str(st)+"')"
    c.execute(mn)
    fd=c.execute("select appointment from licencereg where lid='"+str(mid)+"'")
    sdata=c.fetchone()
    apdate=sdata[0]
    sta23="pending"
    typ="licence"
    mn1="insert into authorityapproval(cid,type,appdate,status) values('"+str(cid)+"','"+str(typ)+"','"+str(apdate)+"','"+str(sta23)+"')"
    c.execute(mn1)
    g="forwarded"
    lm="update licencereg set status='"+str(g)+"' where lid='"+str(mid)+"'"
    c.execute(lm)
    con.commit()
    return render(request,'AdminViewapplications.html')

def customerviewapprovals(request):
    id=request.session["cid"]
    me="select count(*) from authorityapproval where cid='"+str(id)+"'"
    c.execute(me)
    ds=c.fetchone()
    ds1=ds[0]
    if ds1>0:
        me="select * from authorityapproval where cid='"+str(id)+"'"
        c.execute(me)
        
        dat=c.fetchall()
        return render(request,'customerviewapprovals.html',{'data':dat}) 
    else:
        msg="No Applications Applied"
        return render(request,'customerviewapprovals.html',{'msg':msg}) 

    return render(request,'customerviewapprovals.html',{'data':dat}) 
def viewlicenceapplications(request):
    bb="pending"  
    ty="licence"
    vb="forwarded"
    me="select licencereg.*,authorityapproval.* from licencereg inner join authorityapproval on licencereg.cid=authorityapproval.cid inner join forward on forward.certid=licencereg.lid where authorityapproval.status='"+str(bb)+"' and authorityapproval.type='"+str(ty)+"' and forward.certificate='"+str(ty)+"' and licencereg.status='"+str(vb)+"'"
    
    
    c.execute(me)
    
    dat=c.fetchall()
    return render(request,'authorityviewlicence.html',{'data':dat}) 

def authorityapprovelicence(request):
    fwid=request.GET.get("id")  
    st="approved"
    print("licenceeeeeeeeeeeee")
    bn="select cid from authorityapproval where otherid='"+str(fwid)+"'"
    c.execute(bn)
    dd=c.fetchone()
    cid=dd[0]
    # date1=dd[1]
    # print(date1)
    bm="select phno from cusreg where cid='"+str(cid)+"'"
    c.execute(bm)
    data1=c.fetchone()
    ph=data1[0]
    
   
    me="update authorityapproval set status='"+str(st)+"' where otherid='"+str(fwid)+"'"
    c.execute(me)
    print(me)
    con.commit()
    msg="your  appointment date for licence  approved...kindly visit our site"
    sendsms(ph,msg)
  
    return HttpResponseRedirect("/viewlicenceapplications/")
def passport(request):
    d=str(date.today())
    if 'passportsubmit' in request.POST:
       
        tob=request.POST.get("cname")
        dis=request.POST.get("n1")
        gen=request.POST.get("n3")
        cname=request.POST.get("n4")
        mname=request.POST.get("n5")
        fname=request.POST.get("n6")
        paddr=request.POST.get("g1")
        qu=request.POST.get("g2")
        emp=request.POST.get("g3")
        # paddrb=request.POST.get("mname")
        # pob=request.POST.get("fname")
        # hosp=request.POST.get("paddr")
        # deli=request.POST.get("p1")
        # bw=request.POST.get("sig")
        
        myfile = request.FILES.get("mname")
        fs = FileSystemStorage()        
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        myfile1 = request.FILES.get("fname")
        fs = FileSystemStorage()        
        filename1 = fs.save(myfile1.name, myfile1)
        uploaded_file_url1 = fs.url(filename1)
        myfile2 = request.FILES.get("paddr")
        fs = FileSystemStorage()        
        filename2 = fs.save(myfile2.name, myfile2)
        uploaded_file_url2 = fs.url(filename2)
        myfile3 = request.FILES.get("p1")
        fs = FileSystemStorage()        
        filename3 = fs.save(myfile3.name, myfile3)
        uploaded_file_url3 = fs.url(filename3)
        myfile4 = request.FILES.get("sig")
        fs = FileSystemStorage()        
        filename4 = fs.save(myfile4.name, myfile4)
        uploaded_file_url4 = fs.url(filename4)
        status="applied"
        cusid=request.session["cid"]
        # my_date =datetime.strptime(dis,"%Y-%m-%d")
        # yr=my_date.year
        # my_datedeath =datetime.strptime(rep,"%Y-%m-%d")
        # dyr=my_datedeath.year
        # #dyr=pob.year()
        # if yr>dyr:
        #     msg="please check the date....date of birth should be less than reporting date"
        #     return render(request,'LicenceCertificate.html',{'d':d,'msg':msg})


        # else:
        me="insert into passport(name,dob,district,taluk,email,phno,addr,qualification,emptype,idproof,addrproof,ageproof,pic,sig,cid,status) values('"+str(tob)+"','"+str(dis)+"','"+str(gen)+"','"+str(cname)+"','"+str(mname)+"','"+str(fname)+"','"+str(paddr)+"','"+str(qu)+"','"+str(emp)+"','"+str(uploaded_file_url)+"','"+str(uploaded_file_url1)+"','"+str(uploaded_file_url2)+"','"+str(uploaded_file_url3)+"','"+str(uploaded_file_url4)+"','"+str(cusid)+"','"+str(status)+"')"
        c.execute(me)
        con.commit()
        return HttpResponseRedirect("/passport/")   

    return render(request,'passport.html',{'d':d})

def adminviewpassport(request):
    
  #  uid=request.session["cid"]
    s="applied"
    gg="select * from passport  where status='"+str(s)+"'"
    c.execute(gg)
    da=c.fetchall()
    st="forwarded"
    
    gg="select * from passport  where status='"+str(st)+"'"
    c.execute(gg)
    dat=c.fetchall()

    return render(request,'adminviewpassport.html',{'data':da,'data1':dat})

def forwardpassport(request):
    mid=request.GET.get("id")
    
    print(mid)
    # cid=request.session["cid"]
    c.execute("select cid from passport where lid='"+str(mid)+"'")
    df=c.fetchone()
    cid=df[0]
    dept="passport"
    dis="Ernakulam"
    f=date.today()
    cer="passport"
    st="forwarded"
    mn="insert into forward(district,authority,fdate,certid,certificate,status) values('"+str(dis)+"','"+str(dept)+"','"+str(f)+"','"+str(mid)+"','"+str(cer)+"','"+str(st)+"')"
    c.execute(mn)
    
    sta23="pending"
    typ="passport"
    
    mn1="insert into authorityapproval(cid,type,status) values('"+str(cid)+"','"+str(typ)+"','"+str(sta23)+"')"
    c.execute(mn1)
    g="forwarded"
    lm="update passport set status='"+str(g)+"' where lid='"+str(mid)+"'"
    c.execute(lm)
    con.commit()
    return render(request,'AdminViewapplications.html')
def viewpassportapplication(request):
    bb="pending"  
    ty="passport"
    vb="forwarded"
    me="select passport.*,authorityapproval.* from passport inner join authorityapproval on passport.cid=authorityapproval.cid inner join forward on forward.certid=passport.lid where authorityapproval.status='"+str(bb)+"' and authorityapproval.type='"+str(ty)+"' and forward.certificate='"+str(ty)+"' and passport.status='"+str(vb)+"'"
    c.execute(me)
    
    dat=c.fetchall()
    return render(request,'authorityviewpassport.html',{'data':dat}) 

def authorityapprovepassport(request):
    fwid=request.GET.get("id")  
    st="approved"
    bn="select cid from authorityapproval where otherid='"+str(fwid)+"'"
    c.execute(bn)
    dd=c.fetchone()
    cid=dd[0]
    # date1=dd[1]
    # print(date1)
    bm="select phno from cusreg where cid='"+str(cid)+"'"
    c.execute(bm)
    data1=c.fetchone()
    ph=data1[0]
    
   
    me="update authorityapproval set status='"+str(st)+"' where otherid='"+str(fwid)+"'"
    c.execute(me)
    print(me)
    con.commit()
    msg="your passport approved...kindly visit our seva"
    sendsms(ph,msg)
    return HttpResponseRedirect("/viewpassportapplication/")
def viewrationregistration(request):
    
  #  uid=request.session["cid"]
    s="applied"
    gg="select * from rationreg  where status='"+str(s)+"'"
    c.execute(gg)
    da=c.fetchall()
    st="forwarded"
    
    gg="select * from rationreg  where status='"+str(st)+"'"
    c.execute(gg)
    dat=c.fetchall()

    return render(request,'adminviewration.html',{'data':da,'data1':dat})

