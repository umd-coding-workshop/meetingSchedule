meetingSchedule
===============

For fun. This script attempts to determine the optimal rotating schedule for coding workshop meetings.


We've agreed to meet on rotating days:

Monday (M)
Tuesday (T)
Thursday (H)
Friday (F)

We don't want to have a Friday meeting followed by a Monday meeting since it would not allow much time to complete Codeacademy lessons and other projects.

A Thursday meeting followed by Monday is not great either.

Is it possible to write a script in Python that will determine the best sequence of days?

Rules:
1. We need to meet on all days before repeating a day. (i.e., MTHF is an acceptable sequence. MTMF is not).
2. The sequence of days has to stay intact and repeat. (i.e., MTHF FHTM is not acceptable; you have to do MTHF MTHF).
3. The goal is to find the sequence with the longest minimum time between meetings. For example, MTHF MTHF has a minimum time between meetings of 3 days (Friday to Monday). MTFH MTFH would be a minimum span of 4 days (Thursday to Monday)
4. Secondary goal is to minimize the longest time between meetings. FHTM would have a span of 11 days between Monday and the following Friday.
