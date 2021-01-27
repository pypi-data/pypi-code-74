from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseForbidden
from psu_base.classes.Log import Log
from psu_base.classes.ConvenientDate import ConvenientDate
from psu_scheduler.services import scheduler_service
from psu_base.services import utility_service, message_service, auth_service
from psu_base.decorators import require_authority, require_authentication
from requests_futures.sessions import FuturesSession
from psu_scheduler.models import JobDefinition, JobExecution
from psu_scheduler.decorators import scheduled_job
import secrets
import string
import re

log = Log()


@scheduled_job()
def test_job(request):
    """A test job that does nothing"""
    log.trace()
    return HttpResponse('The test job has completed.')


def run_jobs(request):
    """
    Run any scheduled jobs
    """
    log.trace()
    jobs = scheduler_service.get_jobs_to_run()
    if jobs:
        executions = []
        session = FuturesSession()

        for job in jobs:
            # Record that job is running
            je = JobExecution()
            je.job = job
            je.key = ''.join(secrets.choice(string.ascii_uppercase + string.digits) for _ in range(20))
            je.save()

            # Start job in background
            url = f"{scheduler_service.get_absolute_url(job.url())}?job_id={je.id}&job_key={je.key}"
            jr = session.get(url)

            # Hold for later
            jt = (je, jr)
            executions.append(jt)

        # Wait for completion and log each completion
        for j_tuple in executions:
            je = j_tuple[0]
            jr = j_tuple[1]
            response = jr.result()
            je.status = 'done'
            je.output = response.content
            je.save()

    return HttpResponse(f"Ran {len(jobs)} jobs")


def job_list(request):
    """
    List of defined jobs (manage schedules)
    """
    sort, page = utility_service.pagination_sort_info(request, 'title')
    jobs = JobDefinition.objects.order_by(*sort)

    return render(request, 'scheduled_jobs.html', {'jobs': jobs})


def save_job(request):
    """
    Create a new scheduled job
    """
    log.trace()
    app_code = utility_service.get_app_code()

    title = request.POST.get('title')
    endpoint = request.POST.get('endpoint')
    run_times_csv = request.POST.get('run_times_csv')
    run_frequency = request.POST.get('run_frequency')

    # get run days as a string
    run_days = request.POST.getlist('run_days')
    run_days = ''.join(sorted([day for day in list(set(run_days)) if day in '0123456'])) if run_days else None

    # Validate run times
    run_times = utility_service.csv_to_list(run_times_csv)
    validated_times = []
    if run_times:
        for hhmm in run_times:
            if re.match(r'^[012]\d[012345]\d$', hhmm):
                validated_times.append(hhmm)
            else:
                message_service.post_error(f"Invalid run time: {hhmm}")
    run_times_csv = ','.join(validated_times)
    del validated_times
    del run_times

    if run_frequency and not run_frequency.isnumeric():
        message_service.post_error("Run frequency must be a number of minutes")
        run_frequency = None

    # Optional parameters:
    start_date = request.POST.get('start_date')
    if start_date:
        start_date = ConvenientDate(start_date).datetime_instance

    end_date = request.POST.get('end_date')
    if end_date:
        end_date = ConvenientDate(end_date).datetime_instance

    performer = request.POST.get('performer')
    if performer:
        job_user = auth_service.look_up_user_cache(performer)
        if job_user:
            performer = job_user.username
        else:
            performer = None
            message_service.post_error(f"Unknown job performer: {performer}")

    job = JobDefinition()
    job.app_code = app_code
    job.title = title
    job.endpoint = endpoint
    job.performer = performer if performer else None
    job.start_date = start_date if start_date else None
    job.end_date = end_date if end_date else None
    job.run_days = run_days
    job.run_times_csv = run_times_csv
    job.run_frequency = int(run_frequency) if run_frequency else None

    errors = job.get_validation_errors()
    if errors:
        for ee in errors:
            message_service.post_error(ee)
    else:
        job.save()

    return redirect('scheduler:jobs')


