# -*- coding: utf-8 -*-

import django.dispatch

survey_completed = django.dispatch.Signal(providing_args=["instance", "data"])
