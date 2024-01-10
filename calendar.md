---
title: Calendar
layout: page
nav_order: 1
released: true
---

<link href='{{ "/assets/fullcalendar/calendar.css" | relative_url }}' rel='stylesheet' />
<script src='{{ "/assets/fullcalendar/calendar.js" | relative_url }}'></script>

<p class="warning">
This schedule is tentative; additional times may be added later. The existing times shouldn’t change though (pending a couple of room bookings).
</p>

All times listed are in your local time zone.

{% for calendar in site.data.calendar.calendars %}
  <h2>{{ calendar.title }}</h2>

  <a href='{{ calendar.embed_link }}' class="btn btn-outline fs-3">Open in Google Calendar</a>
  <div id='{{ calendar.element_id }}'></div>
{% endfor %}

<script>
/* On smaller screens, we display a day by day view. */
var isMobile = window.matchMedia("only screen and (max-width: 760px)").matches;

document.addEventListener('DOMContentLoaded', function() {
  {% for calendar in site.data.calendar.calendars %}
    var calendarEl = document.getElementById('{{ calendar.element_id }}');
    var calendar = new FullCalendar.Calendar(calendarEl, {
      plugins: [ 'googleCalendar', 'dayGrid', 'timeGrid' ],
      googleCalendarApiKey: '{{ calendar.google_api_key }}',
      events: {
        googleCalendarId: '{{ calendar.google_calendar_id }}',
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
        titleEl.innerText = titleEl.innerText.replace('{{ calendar.remove_prefix }}', '');

        var titleText = titleEl.innerText;
        {% for event_type in calendar.event_types %}
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
      minTime: '{{ calendar.min_time }}',
      maxTime: '{{ calendar.max_time }}',
      timeZone: 'local'
    });
    calendar.render();
  {% endfor %}
});
</script>