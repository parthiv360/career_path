
from django.shortcuts import redirect, render

# Create your views here.

def index(request):
    return render(request, 'main/front_page.html')


def chooseclass(request):
    if request.user.is_authenticated:
        return render(request, 'main/chooseclass.html')
    else:
        return redirect('login:login')


def stream(request):
    if request.user.is_authenticated:
        return render(request, 'main/stream.html')
    else:
        return redirect('login:login')


def streamten(request):
    if request.user.is_authenticated:
        return render(request, 'main/stream10.html')
    else:
        return redirect('login:login')


def imp_exam(request):
    if request.user.is_authenticated:
        return render(request, 'main/imp_exam_sa.html')
    else:
        return redirect('login:login')


def contact(request):
        return render(request,'main/contactus.html')


def studyabroad(request):
    if request.user.is_authenticated:
        return render(request, 'main/study_abroad.html')
    else:
        return redirect('login:login')


def sat(request):
    if request.user.is_authenticated:
        return render(request, 'main/sat.html')
    else:
        return redirect('login:login')


def gre(request):
    if request.user.is_authenticated:
        return render(request, 'main/gre.html')
    else:
        return redirect('login:login')


def gmat(request):
    if request.user.is_authenticated:
        return render(request, 'main/gmat.html')
    else:
        return redirect('login:login')


def toefl(request):
    if request.user.is_authenticated:
        return render(request, 'main/toefl.html')
    else:
        return redirect('login:login')


def science(request):
    if request.user.is_authenticated:
        return render(request, 'main/science1.html')
    else:
        return redirect('login:login')


def commerce(request):
    if request.user.is_authenticated:
        return render(request, 'main/commerce1.html')
    else:
        return redirect('login:login')


def eng(request):
    if request.user.is_authenticated:
        return render(request, 'main/engineering.html')
    else:
        return redirect('login:login')


def engbra(request):
    if request.user.is_authenticated:
        return render(request, 'main/eng_branch.html')
    else:
        return redirect('login:login')


def engexams(request):
    if request.user.is_authenticated:
        return render(request, 'main/eng_exams.html')
    else:
        return redirect('login:login')


def engcoach(request):
    if request.user.is_authenticated:
        return render(request, 'main/eng_coaching.html')
    else:
        return redirect('login:login')


def enginst(request):
    if request.user.is_authenticated:
        return render(request, 'main/eng_inst.html')
    else:
        return redirect('login:login')


def medical(request):
    if request.user.is_authenticated:
        return render(request, 'main/medical.html')
    else:
        return redirect('login:login')


def medexam(request):
    if request.user.is_authenticated:
        return render(request, 'main/med_exams.html')
    else:
        return redirect('login:login')


def medinst(request):
    if request.user.is_authenticated:
        return render(request, 'main/med_inst.html')
    else:
        return redirect('login:login')


def gensci(request):
    if request.user.is_authenticated:
        return render(request, 'main/gensci.html')
    else:
        return redirect('login:login')


def genscideg(request):
    if request.user.is_authenticated:
        return render(request, 'main/gen_degree.html')
    else:
        return redirect('login:login')


def gensciinst(request):
    if request.user.is_authenticated:
        return render(request, 'main/gen_inst.html')
    else:
        return redirect('login:login')


def arts(request):
    if request.user.is_authenticated:
        return render(request, 'main/arts1.html')
    else:
        return redirect('login:login')


def comdip(request):
    if request.user.is_authenticated:
        return render(request, 'main/com_dip.html')
    else:
        return redirect('login:login')


def commaths(request):
    if request.user.is_authenticated:
        return render(request, 'main/com_maths.html')
    else:
        return redirect('login:login')


def commathscouse(request):
    if request.user.is_authenticated:
        return render(request, 'main/com_maths_course.html')
    else:
        return redirect('login:login')


def commathinst(request):
    if request.user.is_authenticated:
        return render(request, 'main/com_maths_college.html')
    else:
        return redirect('login:login')


def comwmaths(request):
    if request.user.is_authenticated:
        return render(request, 'main/com_wmaths.html')
    else:
        return redirect('login:login')


def comwmathscol(request):
    if request.user.is_authenticated:
        return render(request, 'main/com_wmaths_college.html')
    else:
        return redirect('login:login')


def comwmathscor(request):
    if request.user.is_authenticated:
        return render(request, 'main/com_wmaths_course.html')
    else:
        return redirect('login:login')


def scienceten(request):
    if request.user.is_authenticated:
        return render(request, 'main/10science.html')
    else:
        return redirect('login:login')


def commerceten(request):
    if request.user.is_authenticated:
        return render(request, 'main/10commerce.html')
    else:
        return redirect('login:login')


def artsten(request):
    if request.user.is_authenticated:
        return render(request, 'main/10arts.html')
    else:
        return redirect('login:login')


def diplomaten(request):
    if request.user.is_authenticated:
        return render(request, 'main/10diploma.html')
    else:
        return redirect('login:login')


def artsdip(request):
    if request.user.is_authenticated:
        return render(request, 'main/arts_dip.html')
    else:
        return redirect('login:login')


def artsdeg(request):
    if request.user.is_authenticated:
        return render(request, 'main/arts_deg.html')
    else:
        return redirect('login:login')


def artsdegcol(request):
    if request.user.is_authenticated:
        return render(request, 'main/arts_deg_college.html')
    else:
        return redirect('login:login')

    
def artsdegcor(request):
    if request.user.is_authenticated:
        return render(request, 'main/arts_deg_course.html')
    else:
        return redirect('login:login')