Helpdesk (Flous Flow)
====================

Manage customer support tickets with teams, stages and tags, and link each
ticket to a physical **repair order**.

When you install this module, the standard Odoo ``repair`` module is
installed automatically (it is a dependency), and every repair order keeps a
link back to its helpdesk ticket.

Features
--------

* Helpdesk tickets with teams, stages, tags and priorities.
* Kanban view grouped by stage.
* Full lifecycle: ``New -> In Progress -> Done / Cancelled``.
* Create a repair order directly from a ticket (linked both ways).
* Chatter and activities on every ticket.
* Multi-company record rules.
* Printable ticket (PDF report).
* Public tracking link (no login) with QR code, so customers can follow
  their repair status.

Configuration
-------------

1. Install the module (it auto-installs ``repair`` and its dependencies).
2. Go to *Helpdesk -> Configuration -> Stages* and create your stages.
3. Go to *Helpdesk -> Configuration -> Tags* and create your tags.
4. Go to *Helpdesk -> Teams* and create a team (assign members and stages).

Access rights
-------------

* **Helpdesk User** (auto-granted to every internal user): create and update
  tickets.
* **Helpdesk Manager**: full access, plus Teams / Stages / Tags configuration.

Usage
-----

1. Go to *Helpdesk -> Tickets* and click **New**.
2. Fill the subject, customer, team, stage and (optionally) the product to
   repair.
3. Use **Start**, **Mark Done** and **Cancel** to move the ticket through the
   lifecycle.
4. Click **Create Repair** to create a linked ``repair.order`` (customer and
   product are pre-filled from the ticket).
5. Print the ticket from the **Print** button.

License
-------

LGPL-3.
