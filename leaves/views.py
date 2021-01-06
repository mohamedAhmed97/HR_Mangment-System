from django.http import HttpResponse
from django.shortcuts import render
from .models import EmployeeLevel
from .forms import EmployeeLevelForm
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib import messages
from django.contrib.messages import constants
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from employees.models import User
from django.contrib.auth.decorators import login_required
from mashreq_HRMS.utils import allowed_user
from django.shortcuts import get_object_or_404


@login_required
def leaves_list(request):
    query_set = EmployeeLevel.objects.filter(confirm='w')
    return render(request, 'employee_level_list.html', {'employees': query_set})


@login_required
def create_leaves(request):
    form = EmployeeLevelForm()
    if request.method == "POST":
        form = EmployeeLevelForm(request.POST)
        if form.is_valid():
            leave = form.save(commit=False)
            if leave.emp_id ==None:
                leave.emp_id = request.user
            check_date = form.check_leave(leave.emp_id)
            if check_date == True:
                if leave.check_balance() == True:
                    # print("true")
                    leave.save()
                else:
                    messages.error(request, 'Your balance!')
                #
            else:
                messages.error(request, 'You are in aleave!')

        return HttpResponseRedirect('/leaves')
    return render(request, 'create_leaves.html', {'form': form})


@login_required
@allowed_user(allowed_roles=['Manger'])
def accept_leave(request, con_id):
    employee_level = EmployeeLevel.objects.filter(id=con_id)
    msg_html = render_to_string('emails/accept.html')
    send_mail(
        'subject',
        'body of the message',
        settings.EMAIL_HOST_USER,
        [employee_level[0].emp_id.email, ],
        html_message=msg_html
    )
    employee_level.update(confirm='a')
    new_balance = employee_level[0].emp_id.balance - \
        employee_level[0].calculate_number_of_days()
    user = User.objects.filter(
        id=employee_level[0].emp_id.id).update(balance=new_balance)
    messages.success(request, 'leave accepted!')
    return HttpResponseRedirect('/leaves')


@login_required
@allowed_user(allowed_roles=['Manger'])
def reject_leave(request, con_id):
    EmployeeLevel.objects.filter(id=con_id).update(confirm='r')
    msg_html = render_to_string('emails/reject.html')
    send_mail(
        'subject',
        'body of the message',
        settings.EMAIL_HOST_USER,
        ['mohamed.a.ramadan23@gmail.com', ],
        html_message=msg_html
    )
    messages.error(request, 'leave rejected!')
    return HttpResponseRedirect('/leaves')
