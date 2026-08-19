from odoo.tests.common import TransactionCase


class TestHelpdesk(TransactionCase):

    def setUp(self):
        super().setUp()
        self.stage = self.env['flousflow.helpdesk.stage'].create({'name': 'New'})
        self.team = self.env['flousflow.helpdesk.team'].create({
            'name': 'Support Team',
            'stage_ids': [(4, self.stage.id)],
        })
        self.partner = self.env['res.partner'].create({'name': 'Test Customer'})
        self.product = self.env['product.product'].create({
            'name': 'Test Product',
            'type': 'consu',
        })
        self.ticket = self.env['flousflow.helpdesk.ticket'].create({
            'name': 'Broken laptop',
            'team_id': self.team.id,
            'stage_id': self.stage.id,
            'partner_id': self.partner.id,
            'product_id': self.product.id,
        })

    def test_ticket_creation(self):
        self.assertEqual(self.ticket.state, 'draft')

    def test_state_flow(self):
        self.ticket.action_start()
        self.assertEqual(self.ticket.state, 'in_progress')
        self.ticket.action_done()
        self.assertEqual(self.ticket.state, 'done')

    def test_create_repair_from_ticket(self):
        wizard = self.env['flousflow.helpdesk.create.repair.wizard'].create({
            'ticket_id': self.ticket.id,
            'partner_id': self.partner.id,
            'product_id': self.product.id,
        })
        wizard.action_create_repair()
        repair = self.ticket.repair_id
        self.assertTrue(repair)
        self.assertEqual(repair.product_id, self.product)
        self.assertEqual(repair.helpdesk_ticket_id, self.ticket)
        self.assertEqual(repair.partner_id, self.partner)
        self.assertEqual(repair.state, 'draft')

    def test_permissions(self):
        # مستخدم بوابة (بدون base.group_user) → لا يستطيع قراءة التذاكر
        portal_user = self.env['res.users'].create({
            'name': 'Portal User',
            'login': 'test_portal_user',
            'group_ids': [(6, 0, [self.env.ref('base.group_portal').id])],
        })
        with self.assertRaises(Exception):
            self.ticket.with_user(portal_user).read(['name'])
        # مستخدم داخلي (base.group_user) → ياخد helpdesk تلقائيًا عبر الـ implication
        internal_user = self.env['res.users'].create({
            'name': 'Internal User',
            'login': 'test_internal_user',
            'group_ids': [(6, 0, [self.env.ref('base.group_user').id])],
        })
        self.assertTrue(self.ticket.with_user(internal_user).read(['name']))
        # المدير يستطيع تعديل/حذف التذاكر (manager)
        manager_user = self.env['res.users'].create({
            'name': 'Manager User',
            'login': 'test_manager_user',
            'group_ids': [(6, 0, [
                self.env.ref('base.group_user').id,
                self.env.ref('flousflow_helpdesk.group_helpdesk_manager').id,
            ])],
        })
        self.assertTrue(self.ticket.with_user(manager_user).write({'priority': '2'}))
