---
layout: page
title: Beacon Guide
categories: guides
author: Itai Smith, Connor Lafferty
parent: Guides
grand_parent: Resources
has_children: false
released: false
---

## What is Beacon?

Rather than using bCourses, we will be using our own custom learning management
system called Beacon at
[beacon.datastructur.es]({{ site.beacon_url }}). You can use Beacon
to keep track of your grades and late assignments, and you will also use it to
establish partnerships.

Lab 1 will walk you through getting started with Beacon. This guide will detail
the different tabs in Beacon and how to effectively use the system.

As we continuously work to improve Beacon, we will announce on Ed and update
this guide when we introduce new features.

## The Beacon Home Page

On the home page, you will see your name, your Berkeley email address, and
Github username. You should make sure all the information is correct, otherwise
some course functionalities will not work for you. If any of the information is
incorrect, please make a private post on Ed asking us to fix these details for
you.

Most importantly, verify that the email address you see on Beacon is the same
email used in your Gradescope account. Some assignments and extra credit
opportunities have you fill out Google forms, which record the email account
you are logged in with. Whenever you fill such form, make sure you are logged
in from the address on specified Beacon. If you change your Berkeley email
address for whatever reason during the semester, please let us know. If there
is a mismatch between your Beacon email and your Gradescope/Google form email,
your grades may not be accurate, so please be aware of this.

You will also find on this page the Discord username you should use to log into
our Discord servers for lab sections and office hours. See our
[Discord Guide](discord-guide) for more information. Note that these Discord
usernames will not be enforced for the first few weeks of class.

## The Grades Tab

Here you will see all the points you earned for the different assignments and
extra credit opportunities. Remember that CS 61B is not curved, so by making
conjectures about your performance in future assignments together with the data
on this tab, you can check what letter grade corresponds to your total points.
You can learn more about grading bins in our [Course Info page.](../../../about.md).

The grades tab gets data periodically from Gradescope. Thus, it may not be
immediately updated whenever you submit an assignment to Gradescope. You can
expect the grades tab to update every 24 hours.

The Grades tab on Beacon is the final source of truth for your grades. If your
grade on Beacon does not match what you see on Gradescope, please let us know.

## The Partnerships Tab

In this tab, you will see information about all the partnerships you have
established. In Spring 2021 students are allowed to optionally work with a
partner on lab assignments, and are required to work with a partner on
Project 3. You can learn more about the partnerships tab and partnerships in
[the Partnerships Guide.](partnerships)

## The Extensions Tab

The [extensions tab on Beacon]({{ site.beacon_url }}/extensions/) is
where you'll use slip days to extend the deadline for labs and projects. You
will not be able to request an extension for homework or project checkpoints.
You will be able to request extensions for project extra credit opportunities
other than checkpoints. Finally, you will not be able to request an extension
for Project 3 Part B.  Here's how it works:

1.  To use slip days, select the assignment you'd like to take slip days for.
    You can only select assignments that have been released.
2.  Choose your new extended due date for the assignment. If you have enough
    slip days left to cover the difference between the due date you selected
    and the normal due date of the assignment, your extension will be
    automatically approved and your slip days will decrease accordingly.
    However, per [our policies on lateness](/policies#lateness), you
    cannot request a new due date that is more than 3 days beyond the normal
    due date for an assignment.
3.  After your extension is automatically approved and your slip days have
    decreased, you **cannot** request a lesser extension on the same assignment
    (i.e. one with an earlier due date) to get slip days refunded. For example,
    if you requested 3 slip days for Project 2, and was able to submit it only
    after 1 slip day, there is no way for you to “get back” the 2 slip days
    that were applied after your original request.
4.  You **can** opt to increase your extension at the cost of more slip days.
    To do this, just repeat steps 1 and 2 above with the new, later due date
    that you want. For example, if you requested 1 slip day for Project 2, but
    were not able to finish by your new due date, you can request another
    extension for Project 2 using your leftover slip days.
5.  After you have the extension you want on Beacon for the assignment, the
    autograder for that assignment on Gradescope will now take your new,
    extended due date into account when calculating lateness. If you're going
    to use slip days, please make sure you have the approved extension on
    Beacon before submitting to the autograder, so it can use your updated due
    date. It may take a few hours before you see Gradescope updated with your
    new due date. Please let us know if it seems like your extensions are not
    being properly translated into Gradescope after this time frame.

You can use slip days for an assignment retroactively - that is, you can decide
to extend the due date for an assignment after the normal due date has already
passed. For example, if you didn’t submit Lab 5 on time, but were able to
complete it 1.5 days after the deadline, you can follow step 1 and 2 above for
this assignment even after its deadline, to have the new deadline for you to be
1.5 days after the original one. You can then submit it to Gradescope to get
credit with no late penalty.

All students have been given 6 slip days to start, and can use fractions of
slip days.

## DSP Students with Extension Accommodations

If you have DSP accommodations and your accommodations include extensions for
assignments, you will be able to request automatically-approved extensions, the
form on your extension tab will be titled "DSP Students Only". Extensions
requested through this form will not cost you slip days. Only extensions that
are 3 days or less will be automatically approved. If you want a longer
extension, you can request it, but you will be prompted to make a manual
extension request and must email us (cs61b@berkeley.edu) asking for extension
approval.

If you lose your accommodations for extensions at some point during the
semester, you will no longer see the “DSP Students Only” title in the
extensions tab, and will have to follow the process described above (steps 1-2)
to request extensions. At that point you will be granted 6 slip days to start
with.
