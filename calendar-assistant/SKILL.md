---
name: calendar-assistant
description: Use Calendar Manager for Google Calendar agenda, French school holidays by zone A/B/C, availability, and confirmation-gated event changes.
---

# Calendar Assistant

Use the Calendar Manager MCP tools for Google Calendar work.

For French school holidays, use `get_school_holidays` with zone `A`, `B` or `C`. The data is fetched from the official Ministry of Education open dataset; do not invent or hard-code dates. To copy those periods into Google Calendar as all-day events, use `sync_school_holidays` and follow the same confirmation flow as other writes.

## Defaults

- Use `Europe/Paris` unless the user gives another IANA time zone.
- Use RFC3339/ISO 8601 values for timed events and `YYYY-MM-DD` for all-day events.
- Keep the calendar ID as `primary` unless the user selects another calendar.

## Safety rules

- Read-only requests can use `list_events`, `search_events`, `list_calendars`, and `check_availability` immediately.
- Read-only school holiday requests can use `get_school_holidays` immediately.
- For `create_event`, `update_event`, `delete_event`, and `sync_school_holidays`, call the tool once without `confirmed=true` to obtain a human-readable preview.
- Show the preview and ask for explicit confirmation before calling the same tool again with `confirmed=true` and the exact returned `confirmationToken`.
- Never reuse a confirmation token for a different payload; tokens expire after ten minutes.

## Scheduling behavior

- When the user asks for a slot, call `check_availability` with a concrete range and duration.
- Return candidate slots in Europe/Paris, then ask which one to use before creating an event.
- Do not infer attendees or notifications that the user did not provide.
