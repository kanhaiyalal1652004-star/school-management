# School Member Management System

A comprehensive **Odoo-based ERP solution** for school management built with Python and PostgreSQL. This system handles complete school operations including student management, staff records, attendance tracking, exam management, fee/payment processing, class organization, and certificate/transcript generation.

## Features

### 📚 Student Management
- Complete student registration and profile management
- Parent/Guardian information
- Admission records and documents
- Student photo management
- Emergency contact details
- Multi-class student handling

### 👨‍🏫 Teacher/Staff Management
- Teacher information and qualification management
- Staff role assignment (Teaching/Non-Teaching)
- Salary tracking
- Department assignment
- Contact and personal details
- Subject allocation

### 📋 Attendance System
- Daily attendance marking (Present/Absent/Leave)
- Monthly and yearly attendance reports
- Attendance percentage calculation
- Automated attendance summaries
- Holiday management
- Leave request and approval workflow

### 📊 Exam & Marks Management
- Exam scheduling and planning
- Subject-wise marks entry
- Grade calculation and assignment
- Report card generation
- Exam analytics and statistics
- Multiple grading systems support

### 💰 Fee/Payment Management
- Fee structure configuration by class
- Fee collection and tracking
- Payment receipt generation
- Discount and scholarship management
- Payment reminders and reports
- Advance/installment payment handling
- Financial audit trails

### 📍 Class & Section Management
- Class creation and organization
- Section/Division management
- Student-Class assignment
- Capacity management
- Academic year management
- Time table management

### 📄 Report Generation
- **Certificates**: Achievement and completion certificates
- **Transcripts**: Complete academic record documents
- **Report Cards**: Semester/yearly performance reports
- **Attendance Reports**: Individual and class-wise attendance
- **Fee Reports**: Payment and outstanding reports
- **Audit Reports**: Complete activity tracking

## Tech Stack

- **Framework**: Odoo 18 (Python)
- **Database**: PostgreSQL
- **Frontend**: Odoo Web Interface + Custom Views
- **Backend**: Python (Odoo Models & Controllers)
- **Reports**: QWeb Templates (HTML/CSS based)
- **PDF Generation**: Odoo built-in PDF module

## Project Structure

```
school-management/
├── README.md
├── .gitignore
├── addons/                          # Odoo custom modules
│   ├── school_student/              # Student management module
│   │   ├── __init__.py
│   │   ├── __manifest__.py
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   ├── student.py
│   │   │   ├── student_parent.py
│   │   │   └── admission.py
│   │   ├── views/
│   │   │   ├── student_views.xml
│   │   │   ├── parent_views.xml
│   │   │   └── admission_views.xml
│   │   ├── reports/
│   │   │   └── student_report.xml
│   │   └── security/
│   │       └── ir.model.access.csv
│   │
│   ├── school_staff/                # Teacher/Staff management
│   │   ├── __init__.py
│   │   ├── __manifest__.py
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   ├── staff.py
│   │   │   ├── department.py
│   │   │   └── qualification.py
│   │   ├── views/
│   │   │   └── staff_views.xml
│   │   └── security/
│   │       └── ir.model.access.csv
│   │
│   ├── school_attendance/           # Attendance tracking
│   │   ├── __init__.py
│   │   ├── __manifest__.py
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   ├── attendance.py
│   │   │   └── holiday.py
│   │   ├── views/
│   │   │   └── attendance_views.xml
│   │   └── security/
│   │       └── ir.model.access.csv
│   │
│   ├── school_exam/                 # Exam & Marks management
│   │   ├── __init__.py
│   │   ├── __manifest__.py
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   ├── exam.py
│   │   │   ├── marks.py
│   │   │   └── grade.py
│   │   ├── views/
│   │   │   └── exam_views.xml
│   │   └── security/
│   │       └── ir.model.access.csv
│   │
│   ├── school_fee/                  # Fee/Payment management
│   │   ├── __init__.py
│   │   ├── __manifest__.py
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   ├── fee_structure.py
│   │   │   ├── fee_collection.py
│   │   │   ├── payment.py
│   │   │   └── discount.py
│   │   ├── views/
│   │   │   └── fee_views.xml
│   │   └── security/
│   │       └── ir.model.access.csv
│   │
│   ├── school_class/                # Class & Section management
│   │   ├── __init__.py
│   │   ├── __manifest__.py
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   ├── class_division.py
│   │   │   ├── section.py
│   │   │   └── academic_year.py
│   │   ├── views/
│   │   │   └── class_views.xml
│   │   └── security/
│   │       └── ir.model.access.csv
│   │
│   └── school_reports/              # Report generation
│       ├── __init__.py
│       ├── __manifest__.py
│       ├── models/
│       │   ├── __init__.py
│       │   └── report_generator.py
│       ├── reports/
│       │   ├── certificate_template.xml
│       │   ├── transcript_template.xml
│       │   ├── reportcard_template.xml
│       │   └── attendance_report.xml
│       └── security/
│           └── ir.model.access.csv
│
├── docs/                            # Documentation
│   ├── INSTALLATION.md
│   ├── DATABASE_SCHEMA.md
│   ├── API_DOCUMENTATION.md
│   └── USER_GUIDE.md
│
└── config/                          # Configuration files
    ├── odoo.conf
    └── db_config.yml
```

## Installation

### Prerequisites
- Python 3.8+
- PostgreSQL 12+
- Odoo 18
- pip (Python package manager)

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/kanhaiyalal1652004-star/school-management.git
   cd school-management
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Odoo**
   ```bash
   pip install odoo==18.0
   ```

4. **Setup PostgreSQL database**
   ```bash
   createdb school_management
   ```

5. **Copy addons to Odoo custom addons path**
   ```bash
   cp -r addons/* /path/to/odoo/custom_addons/
   ```

6. **Start Odoo server**
   ```bash
   odoo --config=config/odoo.conf --addons-path=/path/to/odoo/addons,./addons
   ```

7. **Access Odoo interface**
   - Open browser and go to `http://localhost:8069`
   - Create new database
   - Install the school management modules

## Module Details

### school_student
- Student information and record management
- Parent/Guardian tracking
- Admission workflow
- Student document management

### school_staff
- Complete staff directory
- Qualification and experience tracking
- Department and role assignment
- Subject specialization

### school_attendance
- Mark daily attendance
- Holiday management
- Leave request processing
- Generate attendance reports

### school_exam
- Schedule and manage exams
- Mark entry system
- Grade assignment
- Report card generation

### school_fee
- Configure fee structures by class
- Collect and track payments
- Generate fee receipts
- Manage discounts and scholarships

### school_class
- Create and manage classes
- Organize sections
- Assign students to classes
- Manage academic years

### school_reports
- Generate certificates
- Create transcripts
- Print report cards
- Generate various compliance reports

## Usage

### Quick Start Guide
1. Create an Academic Year
2. Set up Classes and Sections
3. Register Students
4. Add Staff members
5. Configure Fee Structure
6. Create Exam Schedule
7. Mark Attendance daily
8. Enter exam marks
9. Generate reports and certificates

## Database Schema

Key tables in the system:
- `school_student`: Student records
- `school_staff`: Staff/Teacher records
- `school_attendance`: Attendance logs
- `school_exam`: Exam schedules
- `school_marks`: Student marks
- `school_fee`: Fee structure and collection
- `school_class`: Class and section definitions
- `school_payment`: Payment records

## Features Roadmap

- [ ] Online admission portal
- [ ] Mobile app for parents
- [ ] SMS/Email notifications
- [ ] Advanced analytics dashboard
- [ ] Biometric attendance integration
- [ ] Integration with CBSE board
- [ ] Hostel management module
- [ ] Library management system
- [ ] Sports/Co-curricular tracking

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the LGPL-3.0 License - see the LICENSE file for details.

## Support

For issues and questions:
- Create an Issue on GitHub
- Check existing documentation
- Review database schema

## Author

**Kanhaiya Lal** - [GitHub Profile](https://github.com/kanhaiyalal1652004-star)

## Acknowledgments

- Odoo Framework
- PostgreSQL Database
- Open source community
