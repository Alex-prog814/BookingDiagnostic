from applications.booking.models import BookingDiagnostic


def check_is_master(master):
    if not master.is_master:
        return True
    else:
        return False


def check_date(date):
    if date.isoweekday() not in range(1, 6):
        return True
    else:
        return False


def check_master_stack(master, date, time):
    if BookingDiagnostic.objects.filter(master=master, date=date, time=time):
        return True
    else:
        return False
