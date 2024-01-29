"""civilregistry URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from idcard import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cusreg/',views.cusreg,name="customer reg"),
        path('login/',views.login,name="login"),
        path('authorityreg/',views.authorityreg,name="authorityreg"),
        path('',views.home,name="home"),
        path('home/',views.home,name="home"),
        path('authorityhome/',views.authorityhome,name="authorityhome"),
        path('adminhome/',views.adminhome,name="adminhome"),
        path('customerhome/',views.customerhome,name="customerhome"),
        path('rtohomeorg/',views.rtohomeorg,name="rtohomeorg"),
        path('passporthome/',views.passporthome,name="passporthome"),

        path('applications/',views.applications,name="applications"),
        path('adminviewapplications/',views.adminviewapplications,name="adminviewapplications"),

        path('marriageregistration/',views.marriageregistration,name="marriageregistration"),
        path('BirthCertificateregistration/',views.BirthCertificateregistration,name="BirthCertificateregistration"),
        path('deathregistration/',views.deathregistration,name="deathregistration"),
        path('viewmarriageregistration/',views.viewmarriageregistration,name="viewmarriageregistration"),
        path('forwardmarriage/',views.forwardmarriage,name="forwardmarriage"),
        path('forwarddeath/',views.forwarddeath,name="forwarddeath"),
        path('adminaddreply/',views.adminaddreply,name="adminaddreply"),

        path('feedback/',views.feedback,name="feedback"),
        path('viewfeedback/',views.viewfeedback,name="viewfeedback"),
        path('viewbirthregistration/',views.viewbirthregistration,name="viewbirthregistration"),
        path('Rtohome/',views.Rtohome,name="Rtohome"),
        path('Rpohome/',views.Rpohome,name="Rpohome"),
        path('viewauthorityapplication/',views.viewauthorityapplication,name="viewauthorityapplication"),
        path('viewauthorityapplicationslink/',views.viewauthorityapplicationslink,name="viewauthorityapplicationslink"),
        path('viewvotersidcertificate/',views.viewvotersidcertificate,name="viewvotersidcertificate"),
        path('viewauthoritydeathapplication/',views.viewauthoritydeathapplication,name="viewauthoritydeathapplication"),

        path('issuemarriage/',views.issuemarriage,name="issuemarriage"),
        path('issuevotersid/',views.issuevotersid,name="issuevotersid"),

        path('customerviewcertificate/',views.customerviewcertificate,name="customerviewcertificate"),
        path('payment1/',views.payment1,name="payment1"),
        path('payment2/',views.payment2,name="payment2"),
        path('payment3/',views.payment3,name="payment3"),
        path('payment4/',views.payment4,name="payment4"),
        path('payment5/',views.payment5,name="payment5"),
        path('voteridreg/',views.voteridreg,name="voteridreg"),
        path('viewvotersidregistration/',views.viewvotersidregistration,name="viewvotersidregistration"),
        path('viewmarriagecertificate/',views.viewmarriagecertificate,name="viewmarriagecertificate"),
        path('viewdeathregistration/',views.viewdeathregistration,name="viewdeathregistration"),
        path('forwardbirth/',views.forwardbirth,name="forwardbirth"),
        path('forwardvotersid/',views.forwardvotersid,name="forwardvotersid"),
        path('rtoviewvotersidapplication/',views.rtoviewvotersidapplication,name="rtoviewvotersidapplication"),

          #  path('viewbirthapplication/',views.viewbirthapplication,name="viewbirthapplication"),
           # path('viewdeathapplication/',views.viewdeathapplication,name="viewdeathapplication"),

            path('viewauthoritybirthapplication/',views.viewauthoritybirthapplication,name="viewauthoritybirthapplication"),
            path('issuebirth/',views.issuebirth,name="issuebirth"),
            path('viewbirthcertificate/',views.viewbirthcertificate,name="viewbirthcertificate"),
            path('viewauthoritydeathapplication/',views.viewauthoritydeathapplication,name="viewauthoritydeathapplication"),

        path('contact/',views.contact,name="contact"),
        path('customerdownloadcertificate/',views.customerdownloadcertificate,name="customerdownloadcertificate"),

        path('about/',views.about,name="about"),
        path('forgot/',views.forgot,name="forgot"),
        path('licencereg/',views.licencereg,name="licencereg"),
        path('viewlicenceregistration/',views.viewlicenceregistration,name="viewlicenceregistration"),
        path('viewlicenceapplications/',views.viewlicenceapplications,name="viewlicenceapplications"),

        path('viewauthority/',views.adminviewauthority,name="viewauthority"),
        path('rejectmarriagecertificate/',views.rejectmarriagecertificate,name="rejectmarriagecertificate"),
        path('adminrejectvotersid/',views.adminrejectvotersid,name="adminrejectvotersid"),
        path('forwardlicence/',views.forwardlicence,name="forwardlicence"),
        path('viewmarragedetails/',views.viewmarragedetails,name="viewmarragedetails"),
        path('customerviewapprovals/',views.customerviewapprovals,name="customerviewapprovals"),

        path('authorityapprovelicence/',views.authorityapprovelicence,name="authorityapprovelicence"),
        path('rejectvotersid/',views.rejectvotersid,name="rejectvotersid"),
        path('authorityuploaddeathapplication/',views.authorityuploaddeathapplication,name="authorityuploaddeathapplication"),
        path('rejectdeathcertificate/',views.rejectdeathcertificate,name="rejectdeathcertificate"),

        path('passport/',views.passport,name="passport"),
        path('rejectlisence/',views.rejectlisence,name="rejectlisence"),
         path('rejectpasport/',views.rejectpasport,name="rejectpasport"),
        path('adminrejectcustomer/',views.adminrejectcustomer,name="adminrejectcustomer"),
        path('adminviewpassport/',views.adminviewpassport,name="adminviewpassport"),
        path('forwardpassport/',views.forwardpassport,name="forwardpassport"),
        path('viewpassportapplication/',views.viewpassportapplication,name="viewpassportapplication"),
        path('authorityapprovepassport/',views.authorityapprovepassport,name="authorityapprovepassport"),



]
