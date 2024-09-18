# -*- coding: utf-8 -*-
###############################################################################
#
#    OpenEduCat Inc
#    Copyright (C) 2009-TODAY OpenEduCat Inc(<https://www.openeducat.org>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################
from email.policy import default

from odoo import models, fields, api, _


class OpSubject(models.Model):
    _name = "op.subject"
    _inherit = "mail.thread"
    _description = "Subject"

    name = fields.Char('Name', size=128, required=True)
    code = fields.Char('Code', size=256, required=True)
    grade_weightage = fields.Float('Grade Weightage')
    type = fields.Selection(
        [('theory', 'Theory'), ('practical', 'Practical'),
         ('both', 'Both'), ('other', 'Other')],
        'Type', default="theory", required=True)
    subject_type = fields.Selection(
        [('compulsory', 'Compulsory'), ('elective', 'Elective')],
        'Subject Type', default="compulsory", required=True)
    department_id = fields.Many2one(
        'op.department', 'Department',
        default=lambda self:
        self.env.user.dept_id and self.env.user.dept_id.id or False)
    active = fields.Boolean(default=True)
    student_grades_ids = fields.One2many('op.subject.grade.student', 'course_id', string="Student Grades")

    _sql_constraints = [
        ('unique_subject_code',
         'unique(code)', 'Code should be unique per subject!'),
    ]

    @api.model
    def get_import_templates(self):
        return [{
            'label': _('Import Template for Subjects'),
            'template': '/openeducat_core/static/xls/op_subject.xls'
        }]


class OpSubjectGradeStudent(models.Model):
    _name = "op.subject.grade.student"
    _description = "Grade per Student per Subject"
    _inherit = ['mail.thread']

    student_id = fields.Many2one('op.student', 'Student', required=True, ondelete="cascade", tracking=True)
    subject_id = fields.Many2one('op.subject', 'Subject', required=True, ondelete="cascade", tracking=True)
    course_id = fields.Many2one('op.course', 'Course', required=True, tracking=True)
    grade = fields.Float('Grade', required=True)

    metrics_used = fields.Integer('Metricas usadas extras del final', required=False, default=0)

    metric_1 = fields.Float('Parcial', required=False, default=0)
    metric_2 = fields.Float('Final', required=False, default=0)
    metric_3 = fields.Float('Metric 3', required=False, default=0)
    metric_4 = fields.Float('Metric 4', required=False, default=0)
    metric_5 = fields.Float('Metric 5', required=False, default=0)
    metric_6 = fields.Float('Metric 6', required=False, default=0)
    metric_7 = fields.Float('Metric 7', required=False, default=0)
    metric_8 = fields.Float('Metric 8', required=False, default=0)
    metric_9 = fields.Float('Metric 9', required=False, default=0)
    metric_10 = fields.Float('Metric 10', required=False, default=0)
    metric_11 = fields.Float('Metric 11', required=False, default=0)
    metric_12 = fields.Float('Metric 12', required=False, default=0)
    metric_13 = fields.Float('Metric 13', required=False, default=0)
    metric_14 = fields.Float('Metric 14', required=False, default=0)
    metric_15 = fields.Float('Metric 15', required=False, default=0)
    metric_16 = fields.Float('Metric 16', required=False, default=0)
    metric_17 = fields.Float('Metric 17', required=False, default=0)
    metric_18 = fields.Float('Metric 18', required=False, default=0)
    metric_19 = fields.Float('Metric 19', required=False, default=0)
    metric_20 = fields.Float('Metric 20', required=False, default=0)

    metric_label_1 = fields.Char('Metric 1', required=False, default="Parcial" )
    metric_label_2 = fields.Char('Metric 2', required=False, default="Parcial 2")
    metric_label_3 = fields.Char('Metric 3', required=False, default="Metric 3")
    metric_label_4 = fields.Char('Metric 4', required=False, default="Metric 4")
    metric_label_5 = fields.Char('Metric 5', required=False, default="Metric 5")
    metric_label_6 = fields.Char('Metric 6', required=False, default="Metric 6")
    metric_label_7 = fields.Char('Metric 7', required=False, default="Metric 7")
    metric_label_8 = fields.Char('Metric 8', required=False, default="Metric 8")
    metric_label_9 = fields.Char('Metric 9', required=False, default="Metric 9")
    metric_label_10 = fields.Char('Metric 10', required=False, default="Metric 10")
    metric_label_11 = fields.Char('Metric 11', required=False, default="Metric 11")
    metric_label_12 = fields.Char('Metric 12', required=False, default="Metric 12")
    metric_label_13 = fields.Char('Metric 13', required=False, default="Metric 13")
    metric_label_14 = fields.Char('Metric 14', required=False, default="Metric 14")
    metric_label_15 = fields.Char('Metric 15', required=False, default="Metric 15")
    metric_label_16 = fields.Char('Metric 16', required=False, default="Metric 16")
    metric_label_17 = fields.Char('Metric 17', required=False, default="Metric 17")
    metric_label_18 = fields.Char('Metric 18', required=False, default="Metric 18")
    metric_label_19 = fields.Char('Metric 19', required=False, default="Metric 19")
    metric_label_20 = fields.Char('Metric 20', required=False, default="Metric 20")
    academic_year_id = fields.Many2one('op.academic.year', 'Academic Year', required=True)
    academic_term_id = fields.Many2one('op.academic.term', 'Academic Term')
    state = fields.Selection([
        ('running', 'Running'),
        ('halted', 'Halted'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
        ('pending', 'Pending')
    ], string="State", default="pending", tracking=True)
    _sql_constraints = [
        ('unique_student_subject', 'unique(student_id, subject_id, course_id, academic_year_id)',
         'The student must have a unique grade for each subject, course, and academic year.')
    ]


class WeeklySubjectAssignments(models.Model):
    _name = "weekly.subject.assignments"
    _description = "Weekly Subject Assignments"

    name = fields.Char('Name', required=True)
    description = fields.Text('Description', required=False)

    subject_id = fields.Many2one('op.subject', 'Subject', required=True, ondelete="cascade", tracking=True)
    subject_grade_student_id = fields.Many2one('op.subject.grade.student', 'Subject Grade Student', required=True,
                                               ondelete="cascade")

    # Float fields for each week (week1 to week52)
    week_1 = fields.Float('Week 1', required=False, default=0.0)
    week_2 = fields.Float('Week 2', required=False, default=0.0)
    week_3 = fields.Float('Week 3', required=False, default=0.0)
    week_4 = fields.Float('Week 4', required=False, default=0.0)
    week_5 = fields.Float('Week 5', required=False, default=0.0)
    week_6 = fields.Float('Week 6', required=False, default=0.0)
    week_7 = fields.Float('Week 7', required=False, default=0.0)
    week_8 = fields.Float('Week 8', required=False, default=0.0)
    week_9 = fields.Float('Week 9', required=False, default=0.0)
    week_10 = fields.Float('Week 10', required=False, default=0.0)
    week_11 = fields.Float('Week 11', required=False, default=0.0)
    week_12 = fields.Float('Week 12', required=False, default=0.0)
    week_13 = fields.Float('Week 13', required=False, default=0.0)
    week_14 = fields.Float('Week 14', required=False, default=0.0)
    week_15 = fields.Float('Week 15', required=False, default=0.0)
    week_16 = fields.Float('Week 16', required=False, default=0.0)
    week_17 = fields.Float('Week 17', required=False, default=0.0)
    week_18 = fields.Float('Week 18', required=False, default=0.0)
    week_19 = fields.Float('Week 19', required=False, default=0.0)
    week_20 = fields.Float('Week 20', required=False, default=0.0)
    week_21 = fields.Float('Week 21', required=False, default=0.0)
    week_22 = fields.Float('Week 22', required=False, default=0.0)
    week_23 = fields.Float('Week 23', required=False, default=0.0)
    week_24 = fields.Float('Week 24', required=False, default=0.0)
    week_25 = fields.Float('Week 25', required=False, default=0.0)
    week_26 = fields.Float('Week 26', required=False, default=0.0)
    week_27 = fields.Float('Week 27', required=False, default=0.0)
    week_28 = fields.Float('Week 28', required=False, default=0.0)
    week_29 = fields.Float('Week 29', required=False, default=0.0)
    week_30 = fields.Float('Week 30', required=False, default=0.0)
    week_31 = fields.Float('Week 31', required=False, default=0.0)
    week_32 = fields.Float('Week 32', required=False, default=0.0)
    week_33 = fields.Float('Week 33', required=False, default=0.0)
    week_34 = fields.Float('Week 34', required=False, default=0.0)
    week_35 = fields.Float('Week 35', required=False, default=0.0)
    week_36 = fields.Float('Week 36', required=False, default=0.0)
    week_37 = fields.Float('Week 37', required=False, default=0.0)
    week_38 = fields.Float('Week 38', required=False, default=0.0)
    week_39 = fields.Float('Week 39', required=False, default=0.0)
    week_40 = fields.Float('Week 40', required=False, default=0.0)
    week_41 = fields.Float('Week 41', required=False, default=0.0)
    week_42 = fields.Float('Week 42', required=False, default=0.0)
    week_43 = fields.Float('Week 43', required=False, default=0.0)
    week_44 = fields.Float('Week 44', required=False, default=0.0)
    week_45 = fields.Float('Week 45', required=False, default=0.0)
    week_46 = fields.Float('Week 46', required=False, default=0.0)
    week_47 = fields.Float('Week 47', required=False, default=0.0)
    week_48 = fields.Float('Week 48', required=False, default=0.0)
    week_49 = fields.Float('Week 49', required=False, default=0.0)
    week_50 = fields.Float('Week 50', required=False, default=0.0)
    week_51 = fields.Float('Week 51', required=False, default=0.0)
    week_52 = fields.Float('Week 52', required=False, default=0.0)


# No se usa, pero si lo eliminas anda todo mal.

class CourseMetric(models.Model):
    _name = "op.course.metric"
    _description = "Course Metric"
    _inherit = ['mail.thread']

    name = fields.Char('Metric Name', required=True, tracking=True)
    course_id = fields.Many2one('op.course', 'Course', required=True, tracking=True)
    max_grade = fields.Float('Maximum Grade', required=True, tracking=True)

    _sql_constraints = [
        ('unique_course_metric', 'unique(name, course_id)',
         'Each course must have unique metrics (assignments, exams, etc.).')
    ]


class CourseMetricStudent(models.Model):
    _name = "op.course.metric.student"
    _description = "Grade per Student per Metric"
    _inherit = ['mail.thread']

    student_id = fields.Many2one('op.student', 'Student', required=True, ondelete="cascade", tracking=True)
    course_id = fields.Many2one('op.course', 'Course', required=True, ondelete="cascade", tracking=True)
    metric_id = fields.Many2one('course.metric', 'Metric', required=True, ondelete="cascade", tracking=True)
    grade = fields.Float('Grade', required=True, tracking=True)

    academic_year_id = fields.Many2one('op.academic.year', 'Academic Year', required=True)
    academic_term_id = fields.Many2one('op.academic.term', 'Academic Term')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('graded', 'Graded'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled')
    ], string="State", default="draft", tracking=True)

    _sql_constraints = [
        ('unique_student_metric', 'unique(student_id, course_id, metric_id, academic_year_id)',
         'The student must have a unique grade for each metric, course, and academic year.')
    ]