import random
import datetime
from court.models import Judge, Case

def get_judge(court_type,district):
    judge_queryset=Judge.objects.filter(court_type=court_type,district=district)
    print(judge_queryset)
    if judge_queryset.exists():
        ids = list(
            judge_queryset.values_list("license_no", flat=True)
        )
        print(ids)
        random_id=random.choice(ids)
        selected_judge=Judge.objects.get(license_no=random_id)
        print(selected_judge)
        return selected_judge
    else:
        return None

def get_hearingdate():
    hdate=datetime.datetime.today() + datetime.timedelta(days=5)
    return hdate