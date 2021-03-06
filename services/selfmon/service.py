#!./bin/python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------
# metrics service
# ----------------------------------------------------------------------
# Copyright (C) 2007-2018 The NOC Project
# See LICENSE for details
# ----------------------------------------------------------------------

# Python modules
from threading import Thread
import operator
import time
# Third-party modules
import tornado.gen
# NOC modules
from noc.core.service.base import Service
from noc.core.debug import error_report
from noc.core.span import Span, PARENT_SAMPLE
from noc.services.selfmon.loader import iter_collectors


class SelfMonService(Service):
    name = "selfmon"

    def __init__(self):
        super(SelfMonService, self).__init__()
        self.collectors = []
        self.runner_thread = None

    @tornado.gen.coroutine
    def on_activate(self):
        self.collectors = [c(self) for c in iter_collectors() if c.is_enabled()]
        if not self.collectors:
            self.die("No collectors enabled")
        yield self.acquire_lock()
        self.reorder()
        self.runner_thread = Thread(target=self.runner)
        self.runner_thread.setDaemon(True)
        self.runner_thread.start()

    def reorder(self):
        self.collectors = sorted(self.collectors, key=operator.attrgetter("next_run"))

    def run_round(self):
        self.logger.info("Running checks")
        now = time.time()
        for c in self.collectors:
            if not c.can_run_at(now):
                break  # Done
            with Span(sample=PARENT_SAMPLE, server="selfmon", service=c.name):
                try:
                    c.run()
                except Exception:
                    error_report()
            c.schedule_next()
        self.reorder()

    def runner(self):
        """
        Runner thread worker
        :return:
        """
        self.logger.info("Starting runner thread")
        while True:
            with Span(sample=0, server="selfmon", service="run_round"):
                self.run_round()
            now = time.time()
            delta = self.collectors[0].next_run - now
            if delta > 0:
                self.logger.info("Sleeping %ss", delta)
                time.sleep(delta)


if __name__ == "__main__":
    SelfMonService().start()
