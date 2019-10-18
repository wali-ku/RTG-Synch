'''
Task Generator

The purpose of this class is to generate task objects and populate their
parameters randomly (within preset limits) as per our task model.

Copyright (C) 2019 KU-CSL
09-07-2019  Define task generator class
'''

import random

class Task:
    def __init__ (self, taskId, c, p, m, u = 0, n = 1, gang = False):
        ''' Initialize a task object. The task object is defined by the
        following parameters:

            Compute Time (C):       Execution time of the task in isolation.
                                    This determined randomly; ranging from 1 to
                                    the maximum allowed compute time value.

            Number of Cores (m):    Maximum degree of parallelization of the
                                    task. This value specifies the number of
                                    cores required to execute the task. It
                                    ranges from 1 to 'M' where M is the total
                                    number of cores in the system.

        The purpose of this class is to generate taskset parameters randomly in
        the pre-specified range and return the task object to the caller. '''

        self.fmt = 't%d' if not gang else 'g%d'
        self.n = n
        self.C = float (c)
        self.P = float (p)
        self.m = float (m)
        self.name = self.fmt % (taskId)
        self.u = u if u else (self.C * m / p)

        return

    def __str__ (self):
        return 'Task: %2s | C=%4.1f P=%4d m=%1d u=%.3f n=%1d' % (self.name,
                self.C, self.P, self.m, self.u, self.n)
