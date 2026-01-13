# School Management System - Implementation Guide

## Quick Start: Complete File Structure & Code

Yeh guide aapko सभी modules के लिए complete code provide करता है। GitHub में files को systematically add करने के लिए follow करें।

---

## Phase 1: Core Module Setup (school_student)

### Files to Create:

#### 1. `addons/school_student/__init__.py`
```python
from . import models
```

#### 2. `addons/school_student/__manifest__.py`
```python
{
    'name': 'School Student Management',
    'version': '18.0.1.0.0',
    'category': 'School Management',
    'summary': 'Student registration, profile management, admission records',
    'author': 'Kanhaiya Lal',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/student_views.xml',
        'views/parent_views.xml',
        'views/admission_views.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
}
```

#### 3. `addons/school_student/models/__init__.py`
```python
from . import student
from . import student_parent
from . import admission
```

#### 4. `addons/school_student/models/student.py`
```python
from odoo import models, fields, api

class SchoolStudent(models.Model):
    _name = 'school.student'
    _description = 'School Student'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char('Full Name', required=True, tracking=True)
    student_id = fields.Char('Student ID', unique=True, readonly=True)
    roll_no = fields.Integer('Roll Number')
    date_of_birth = fields.Date('Date of Birth')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], 'Gender')
    email = fields.Char('Email')
    phone = fields.Char('Phone')
    address = fields.Text('Address')
    city = fields.Char('City')
    state = fields.Char('State')
    pincode = fields.Char('Pincode')
    
    # Academic Information
    class_id = fields.Many2one('school.class', 'Class', required=True)
    section_id = fields.Many2one('school.section', 'Section')
    admission_date = fields.Date('Admission Date')
    
    # Parent/Guardian Information
    parent_ids = fields.One2many('school.student.parent', 'student_id', 'Parents/Guardians')
    
    # Documents
    aadhar_number = fields.Char('Aadhar Number')
    birth_certificate = fields.Binary('Birth Certificate')
    
    # Status
    state = fields.Selection([('active', 'Active'), ('inactive', 'Inactive'), ('graduated', 'Graduated')], 
                           'Status', default='active')
    
    @api.model
    def create(self, vals):
        if not vals.get('student_id'):
            vals['student_id'] = self.env['ir.sequence'].next_by_code('school.student') or '/'
        return super().create(vals)
```

#### 5. `addons/school_student/models/student_parent.py`
```python
from odoo import models, fields

class SchoolStudentParent(models.Model):
    _name = 'school.student.parent'
    _description = 'Student Parent/Guardian'

    student_id = fields.Many2one('school.student', 'Student', required=True, ondelete='cascade')
    relation = fields.Selection([
        ('father', 'Father'),
        ('mother', 'Mother'),
        ('guardian', 'Guardian'),
        ('other', 'Other')
    ], 'Relation', required=True)
    name = fields.Char('Full Name', required=True)
    phone = fields.Char('Phone')
    email = fields.Char('Email')
    occupation = fields.Char('Occupation')
    address = fields.Text('Address')
    is_primary = fields.Boolean('Primary Contact', default=False)
```

#### 6. `addons/school_student/models/admission.py`
```python
from odoo import models, fields

class SchoolAdmission(models.Model):
    _name = 'school.admission'
    _description = 'Student Admission Record'

    student_id = fields.Many2one('school.student', 'Student', required=True, ondelete='cascade')
    admission_number = fields.Char('Admission Number', unique=True)
    admission_date = fields.Date('Admission Date', required=True)
    previous_school = fields.Char('Previous School')
    class_admitted = fields.Many2one('school.class', 'Admitted to Class', required=True)
    documents_submitted = fields.Boolean('All Documents Submitted', default=False)
    notes = fields.Text('Notes')
```

#### 7. `addons/school_student/security/ir.model.access.csv`
```csv
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_school_student,access_school_student,model_school_student,base.group_user,1,1,1,1
access_school_student_parent,access_school_student_parent,model_school_student_parent,base.group_user,1,1,1,1
access_school_admission,access_school_admission,model_school_admission,base.group_user,1,1,1,1
```

#### 8. `addons/school_student/views/student_views.xml`
```xml
<?xml version="1.0" encoding="UTF-8"?>
<odoo>
    <data>
        <!-- Student List View -->
        <record id="school_student_view_tree" model="ir.ui.view">
            <field name="name">Student List</field>
            <field name="model">school.student</field>
            <field name="arch" type="xml">
                <tree>
                    <field name="student_id"/>
                    <field name="name"/>
                    <field name="class_id"/>
                    <field name="section_id"/>
                    <field name="state"/>
                </tree>
            </field>
        </record>

        <!-- Student Form View -->
        <record id="school_student_view_form" model="ir.ui.view">
            <field name="name">Student Form</field>
            <field name="model">school.student</field>
            <field name="arch" type="xml">
                <form>
                    <sheet>
                        <group>
                            <field name="name" required="1"/>
                            <field name="student_id" readonly="1"/>
                            <field name="date_of_birth"/>
                            <field name="gender"/>
                        </group>
                        <group>
                            <field name="email"/>
                            <field name="phone"/>
                            <field name="class_id" required="1"/>
                            <field name="section_id"/>
                        </group>
                        <notebook>
                            <page string="Contact Info">
                                <group>
                                    <field name="address"/>
                                    <field name="city"/>
                                    <field name="state"/>
                                    <field name="pincode"/>
                                </group>
                            </page>
                            <page string="Parents">
                                <field name="parent_ids"/>
                            </page>
                            <page string="Documents">
                                <group>
                                    <field name="aadhar_number"/>
                                    <field name="birth_certificate"/>
                                </group>
                            </page>
                        </notebook>
                    </sheet>
                </form>
            </field>
        </record>

        <!-- Action -->
        <record id="action_school_student" model="ir.actions.act_window">
            <field name="name">Students</field>
            <field name="res_model">school.student</field>
            <field name="view_mode">tree,form</field>
        </record>

        <!-- Menu -->
        <menuitem id="menu_school_student" name="Students" parent="menu_school_root" action="action_school_student"/>
    </data>
</odoo>
```

---

## Phase 2: Supporting Modules

### Create Similar Structure for:
1. **school_staff** - Teacher/Staff Management
2. **school_class** - Class & Section Management  
3. **school_attendance** - Attendance Tracking
4. **school_exam** - Exam & Marks Management
5. **school_fee** - Fee/Payment Management
6. **school_reports** - Report Generation

Hर module के लिए same pattern follow करें:
- `models/__init__.py`
- `__init__.py`
- `__manifest__.py`
- `models/` folder with model files
- `views/` folder with XML views
- `security/ir.model.access.csv`

---

## Phase 3: Installation & Setup

### Steps to Install:

1. **Create Database:**
   ```bash
   createdb school_management_db
   ```

2. **Install Odoo 18:**
   ```bash
   pip install odoo==18.0
   ```

3. **Copy Addons:**
   ```bash
   cp -r addons/* /path/to/odoo/custom_addons/
   ```

4. **Start Odoo:**
   ```bash
   odoo --config=config/odoo.conf --addons-path=/path/to/odoo/addons,./addons
   ```

5. **Access:**
   - Open: http://localhost:8069
   - Install modules from Apps

---

## Key Database Models Summary

| Model | Purpose | Key Fields |
|-------|---------|------------|
| school.student | Student records | name, student_id, class_id, state |
| school.student.parent | Parent info | name, relation, phone, student_id |
| school.admission | Admission records | student_id, admission_date, class |
| school.staff | Teacher records | name, staff_id, department_id |
| school.class | Class records | name, class_level, section_ids |
| school.section | Section/Division | name, class_id, capacity |
| school.attendance | Attendance | student_id, date, status |
| school.exam | Exam records | name, exam_date, class_ids |
| school.marks | Student marks | student_id, exam_id, subject, marks |
| school.fee | Fee structure | class_id, fee_amount, term |
| school.payment | Payment records | student_id, amount, date, status |

---

## Next Steps

1. ✅ Create README.md (Done)
2. ✅ Setup school_student module (In Progress)
3. ⬜ Create remaining modules
4. ⬜ Add XML views
5. ⬜ Configure sequences
6. ⬜ Add sample data
7. ⬜ Create report templates

---

## Support

For each module, follow the same pattern:
- Create module folder
- Add __init__.py, __manifest__.py
- Create models, views, security files
- Test in Odoo interface

Yह guide step-by-step है। एक-एक module बना सकते हो और gradually complete कर सकते हो! 🚀
