from psu_scheduler.models import JobDefinition
from psu_base.classes.Log import Log
from psu_base.context_processors import util as util_context
from psu_base.services import utility_service

log = Log()


def get_jobs_to_run():
    """
    Check each defined job to see if it needs to run
    """
    log.trace()
    jobs = JobDefinition.objects.all()
    run_list = []
    if jobs:
        for jj in jobs:
            if jj.should_run():
                run_list.append(jj)
    return run_list


def get_absolute_url(job_url):
    context = util_context(utility_service.get_request())
    return f"{context['absolute_root_url']}{job_url}"
