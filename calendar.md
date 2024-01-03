---
title: Calendar
layout: page
nav_order: 1
---

<link href='{{ "/assets/fullcalendar/calendar.css" | relative_url }}' rel='stylesheet' />
<script src='{{ "/assets/fullcalendar/calendar.js" | relative_url }}'></script>

{%- if site.under_construction -%}
<p class="warning">
This site is under construction. All dates and policies are tentative until this message goes away.
</p>
{%- endif -%}

<p class="warning">
This schedule is tentative; additional times may be added later. The existing times shouldn’t change though (pending a couple of room bookings).
</p>

All times listed are in your local time zone.

[Open in Google Calendar](https://calendar.google.com/calendar/embed?src=c_479e1ddff236af2ffc68f4639ba02ce88afc20a680106fdd7f3f4d5baa2c18b1%40group.calendar.google.com){: .btn .btn-outline .fs-3 }

<div id='calendar'></div>
<script>
/* On smaller screens, we display a day by day view. */
var isMobile = window.matchMedia("only screen and (max-width: 760px)").matches;

document.addEventListener('DOMContentLoaded', function() {
  var calendarEl = document.getElementById('calendar');
  var calendar = new FullCalendar.Calendar(calendarEl, {
    plugins: [ 'googleCalendar', 'dayGrid', 'timeGrid' ],
    googleCalendarApiKey: '{{ site.data.calendar.google_api_key }}',
    events: {
      googleCalendarId: '{{ site.data.calendar.google_calendar_id }}',
    },
    eventClick: function (e) { e.preventDefault(); },
    eventRender: function (info) {
      // Stop from clicking Google Calendar
      info.el.removeAttribute('href');

      var titleEl = info.el.querySelector('.fc-title');
      var eventLocation = info.event.extendedProps.location;
      if (typeof eventLocation !== 'undefined') {
        /* Google Calendar will return the "Location" we put, but also a list
           of rooms we reserved (separated by commas).  This looks quite
           ugly--so if there are multiple locations we will only show the
           first one.  */
        eventLocation = eventLocation.split(', ')[0];
        titleEl.innerText += ' @ ' + eventLocation;
      }
      titleEl.innerText = titleEl.innerText.replace('{{ site.data.calendar.remove_prefix }}', '');

      var titleText = titleEl.innerText;
      {% for event_type in site.data.calendar.event_types %}
      if (titleText.includes('{{ event_type.needle }}')) {
        info.el.style.backgroundColor = '{{ event_type.color }}';
        info.el.style.borderColor = '{{ event_type.color }}';
        info.el.style.color = '{{ event_type.text_color }}';
      }
      {% endfor %}

      var detailedTitleText = titleText;
      var eventDescription = info.event.extendedProps.description;
      if (typeof eventDescription !== 'undefined') {
        detailedTitleText += '. ' + eventDescription;
      }

      var tooltip = new Tooltip(info.el, {
        title: detailedTitleText,
        placement: 'top',
        trigger: 'hover',
        container: 'body'
      });
    },
    eventTextColor: '#fff',
    allDaySlot: false,
    nowIndicator: true,
    header: {
        left: 'timeGridWeek,timeGridDay',
        center: '',
        right: 'prev,next'
    },
    views: {
        timeGridWeek: {
            duration: { weeks: 1 }
        },
    },
    hiddenDays: [0, 6],
    defaultView: isMobile ? 'timeGridDay' : 'timeGridWeek',
    height: 'auto',
    minTime: '{{ site.data.calendar.min_time }}',
    maxTime: '{{ site.data.calendar.max_time }}',
    timeZone: 'local'
  });
  calendar.render();
});
</script>