'''
Task Generator

The purpose of this class is to generate task objects and populate their
parameters randomly (within preset limits) as per our task model.

Copyright (C) 2019 KU-CSL
09-07-2019  Define task generator class
'''

import random

class Task:
    def __init__ (self, taskId, c, p, m, r, members, u = 0, n = 1, gang = False):
        ''' Initialize a task object. The task object is defined by the
        following parameters:

            Compute Time (C):     Execution time of the task in isolation.
                                  This determined randomly; ranging from 1 to
                                  the maximum allowed compute time value.

            Number of Cores (m):  Maximum degree of parallelization of the
                                  task. This value specifies the number of
                                  cores required to execute the task. It
                                  ranges from 1 to 'M' where M is the total
                                  number of cores in the system.

            Resource Demand (r):  Percentage of a critical (bottleneck)
                                  resource needed by the task

        The purpose of this class is to generate taskset parameters randomly in
        the pre-specified range and return the task object to the caller. '''

        self.fmt = 't%d' if not gang else 'g%d'
        self.n = n
        self.g = gang
        self.tid = taskId
        self.C = float (c)
        self.P = float (p)
        self.m = float (m)
        self.r = float (r)
        self.name = self.fmt % (taskId)
        self.u = u if u else (self.C * m / p)
        self.members = members if members else self.name

        return

    def copy (self):
        return Task (self.tid, self.C, self.P, self.m, self.r, self.members, self.u, self.n, self.g)

    def __str__ (self):
        return 'Task: %2s | C=%6s P=%4d m=%2d r=%2d u=%6s n=%2d <%s>' % (self.name,
                '{:4.1f}'.format (self.C), self.P, self.m, self.r,
                '{:2.3f}'.format (self.u), self.n, self.members)
